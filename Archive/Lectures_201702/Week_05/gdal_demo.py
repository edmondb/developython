"""
Author: Alfred Hubbard
Version: 1.0
Start Date: 3/7/17
Description: This script demonstrates basic applications of GDAL.
"""

import subprocess
import os

import numpy as np
from osgeo import gdal

workdir = "C:\\Users\\abhubba1\\Documents\\Python Scripts\\DEVELOP_class"
os.chdir(workdir)

#By default the GDAL Python API does not return errors to the Python 
#console; this reverses that setting
gdal.UseExceptions()

scale = 0.02
thres = 15
out_cellsize = '231.6563583'
MODIS_files = ["MOD11A2.A2016017.h11v05.006.2016234002041.hdf", 
               "MOD11A2.A2016105.h11v05.006.2016242152502.hdf", 
               "MOD11A2.A2016201.h11v05.006.2016242234243.hdf", 
               "MOD11A2.A2016289.h11v05.006.2016302010943.hdf"]

for f in MODIS_files:

    #Extract single subdataset from HDF and save as GeoTIFF
    dayLST_fname = f.rstrip('.hdf')+'_GDAL_dayLST.tif'
    trans_day_cmd = ['gdal_translate', 'HDF4_EOS:EOS_GRID:"'+f+\
                     '":MODIS_Grid_8Day_1km_LST:LST_Day_1km', dayLST_fname]
    p_trans_day = subprocess.Popen(trans_day_cmd, stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
    for line in p_trans_day.communicate():
        print(line)
    nightLST_fname = f.rstrip('.hdf')+'_GDAL_nightLST.tif'
    trans_night_cmd = ['gdal_translate', 'HDF4_EOS:EOS_GRID:"'+f+\
                       '":MODIS_Grid_8Day_1km_LST:LST_Night_1km', 
                       nightLST_fname]
    p_trans_night = subprocess.Popen(trans_night_cmd, stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
    for line in p_trans_night.communicate():
        print(line)
    
    #Register driver for this file type
    driver = gdal.GetDriverByName("GTiff")
    driver.Register()
    #Open raster as GDAL dataset
    dayLST_dataset = gdal.Open(dayLST_fname)
    #Get geotransform and projection from GDAL dataset. These contain 
    #the geospatial information of the data, and we will need them 
    #later to write the array back to a raster file.
    geotrans = dayLST_dataset.GetGeoTransform()
    proj = dayLST_dataset.GetProjection()
    #Open the only band in the dataset. Note that band numbering 
    #starts from 1 as far as GDAL is concerned.
    dayLST_band = dayLST_dataset.GetRasterBand(1)
    #Pull data from band into a NumPy array
    dayLST_array = dayLST_band.ReadAsArray()
    #Get the NoData value for this band
    fillval = dayLST_band.GetNoDataValue()
    #Create a new masked array, where all areas of NoData are masked 
    #out
    dayLST_ma_array = np.ma.masked_equal(dayLST_array, fillval)
    #Empty band and dataset objects to avoid lock issues later. Be 
    #sure to empty the band object first, as there can be problems 
    #otherwise.
    dayLST_band = None
    dayLST_dataset = None
    
    nightLST_dataset = gdal.Open(nightLST_fname)
    nightLST_band = nightLST_dataset.GetRasterBand(1)
    nightLST_array = nightLST_band.ReadAsArray()
    nightLST_ma_array = np.ma.masked_equal(nightLST_array, fillval)
    nightLST_band = None
    nightLST_dataset = None
    
    #Apply scale factor
    dayLST_array_sc = dayLST_ma_array * scale
    nightLST_array_sc = nightLST_ma_array * scale
    
    #Compute difference
    diff = dayLST_array_sc - nightLST_array_sc
    
    #Apply conditional
    diff_thres = np.ma.where(diff>thres, 1, 0)
    new_fillval = 7
    diff_thres[diff_thres.mask] = new_fillval
    
    #Create new dataset to contain output
    thres_fname = f.rstrip('.hdf')+'_GDAL_thres.tif'
    out_dataset = driver.Create(thres_fname, diff_thres.shape[1], 
                                diff_thres.shape[0])
    #Set geotransform and projection of output dataset
    out_dataset.SetGeoTransform(geotrans)
    out_dataset.SetProjection(proj)
    #Create a band for our data
    out_band = out_dataset.GetRasterBand(1)
    #Write our data to the band
    out_band.WriteArray(diff_thres)
    #Tell the raster which value signifies NoData
    out_band.SetNoDataValue(new_fillval)
    #Write the data from memory to disk. Not strictly necessary, as 
    #this should occur anyway at some point, but it is good practice.
    out_band.FlushCache()
    #Clear band and dataset to avoid lock problems
    out_band = None
    out_dataset = None
    
    #Resample
    res_fname = f.rstrip('.hdf')+'_GDAL_res.tif'
    res_cmd = ['gdal_translate', '-tr', out_cellsize, out_cellsize, 
               thres_fname, res_fname]
    p_res = subprocess.Popen(res_cmd, stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE)
    for line in p_res.communicate():
        print(line)