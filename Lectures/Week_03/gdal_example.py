from osgeo import gdal
import numpy as np
import os

# Create a list of files in the direcroty for any .tif files with "clip" 
files = [x for x in os.listdir(os.getcwd()) if "clip" in x and x.endswith(".tif")]

# From the list we just created, create new ones with each band
band_1 = [x for x in files if "b01" in x]
band_2 = [x for x in files if "b02" in x]

# Convert those lists to strings
band_1 = "".join(band_1)
band_2 = "".join(band_2)

# Read the geotiffs as arrays 
b_01 = gdal.Open(band_1)
b_02 = gdal.Open(band_2)

b_01_arr = np.array(b_01.GetRasterBand(1).ReadAsArray())
b_02_arr = np.array(b_02.GetRasterBand(1).ReadAsArray())

# Print some stuff about the array 
print(b_01_arr) # What are the crazy negative values? 
print(b_01_arr.dtype)
print(type(b_01_arr))
print(b_01_arr.shape)

# Change the data type from int to float
b_01_arr = b_01_arr.astype(np.float64)
b_02_arr = b_02_arr.astype(np.float64)

# See that the type has changed
print(b_01_arr.dtype)
print(np.min(b_01_arr))
print(np.mean(b_01_arr))
print(np.max(b_01_arr))

# Eliminate the nodata values 
b_01_arr[b_01_arr < 0] = np.nan
b_02_arr[b_02_arr < 0] = np.nan

# Look at the array to see the changes you've made
print(b_01_arr) # The crazy negative values are replaced with NaNs
print(np.nanmin(b_01_arr))
print(np.nanmean(b_01_arr))
print(np.nanmax(b_01_arr))


# Do something useful! Calculate the NDVI 
ndvi = np.divide(np.subtract(b_02_arr, b_01_arr), np.add(b_01_arr,b_02_arr))
print(ndvi)
print(np.nanmin(ndvi))
print(np.nanmean(ndvi))
print(np.nanmax(ndvi))

# Write the NDVI array to a raster. This is a function to convert an array to a raster, based on a reference raster. 
 
def array2raster(rasterfn,newRasterfn,array): # rasterfn is your reference raster 
	raster = gdal.Open(rasterfn)
	geotransform = raster.GetGeoTransform()
	proj = raster.GetProjection()
	originX = geotransform[0]
	originY = geotransform[3]
	pixelWidth = geotransform[1]
	pixelHeight = geotransform[5]
	cols = raster.RasterXSize
	rows = raster.RasterYSize

	driver = gdal.GetDriverByName('GTiff')
	outRaster = driver.Create(newRasterfn, cols, rows, 1, gdal.GDT_Float32) # Change dtype here
	outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
	outband = outRaster.GetRasterBand(1)
	outband.WriteArray(array)
		
	outRaster.SetProjection(proj)
	outband.FlushCache()

array2raster("b01_clip.tif", "ndvi.tif", ndvi) # Check your downloads directory for the ndvi file 

# Water typically has NDVI values of < 0. Let's classify the image to see if we can detect surface water
surface_water= np.where(1,ndvi<0.0,0)
array2raster("b01_clip.tif", "surface_water.tif", surface_water) # Check your downloads directory for the ndvi file 

