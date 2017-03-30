"""
Author: Alfred Hubbard
Version: 1.0
Start Date: 3/5/17
Description: This script demonstrates basic concepts of ArcPy.
"""

import arcpy

workdir = "C:\\Users\\abhubba1\\Documents\\Python Scripts\\DEVELOP_class"
arcpy.env.workspace = workdir
arcpy.env.mask = "Virginia.shp"
arcpy.env.overwriteOutput = True

arcpy.CheckOutExtension("spatial")

scale = 0.02
thres = 15
out_cellsize = 231.6563583
MODIS_files = ["MOD11A2.A2016017.h11v05.006.2016234002041.hdf", 
               "MOD11A2.A2016105.h11v05.006.2016242152502.hdf", 
               "MOD11A2.A2016201.h11v05.006.2016242234243.hdf", 
               "MOD11A2.A2016289.h11v05.006.2016302010943.hdf"]

for f in MODIS_files:
    
    #Extract from HDF
    day_LST = f.rstrip(".hdf") + "_dayLST.tif"
    arcpy.ExtractSubDataset_management(f, day_LST, subdataset_index=0)
    night_LST = f.rstrip(".hdf") + "_nightLST.tif"
    arcpy.ExtractSubDataset_management(f, night_LST, subdataset_index=4)
    
    #Scale
    day_LST_sc = arcpy.Raster(day_LST) * scale
    night_LST_sc = arcpy.Raster(night_LST) * scale
    
    #Perform subtraction
    diff = day_LST_sc - night_LST_sc
    diff.save(f.rstrip(".hdf")+"_diff.tif")
    
    #Apply conditional
    diff_thres = arcpy.sa.Con(diff > thres, 1, 0)
    diff_thres.save(f.rstrip(".hdf")+"_thres.tif")
    
    #Resample
    res = f.rstrip(".hdf") + "_res.tif"
    arcpy.Resample_management(diff_thres, res, cell_size=out_cellsize)
    
    #Clear variables to avoid locks
    day_LST_sc = None
    night_LST_sc = None
    diff = None
    diff_thres = None
    
arcpy.CheckInExtension("spatial")

#Empty environment settings to prevent them operating on subsequent 
#runs in the same Python session
arcpy.env.workspace = None
arcpy.env.overwriteOutput = None
arcpy.env.mask = None