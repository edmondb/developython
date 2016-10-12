from osgeo import gdal
import numpy as np

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
