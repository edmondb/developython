# developython
Python Training for the DEVELOP program.

# Setup Instructions (User Account & GDAL)

1. [Download](http://www.continuum.io/downloads#_windows) and install Anaconda for Windows 64-Bit (Python 2.7)
2. Do not make it your default Python (possible conflicts with other Python versions or if using arcPy).
3. Do not add it to your path (can change depending upon use with GDAL).
4. Start -> All Programs -> Anaconda 2 (64-Bit) -> Anaconda Prompt
5. `conda install netCDF4 basemap`
7. `conda install -c conda-forge gdal`
8. `conda update gdal`
9. `set GDAL_DATA = C:\Users\TEMP\AppData\Local\Continuum\Anaconda2\Lib\site-packages\gdal-2.1.1-np111py27_2\Library\Share\gdal`
10. Test GDAL install: 
	10.1 Download this [file](https://drive.google.com/file/d/0B9m0kGaHo6cnM0JxbkM5aFZvN28/view?usp=sharing)
	10.2 `cd` to Downloads directory
	10.3 `gdalwarp -t_srs "EPSG:32645" 1400412014302_to_1400412014206.tif test.tif`

TODO:
1. Connect arcpy with Anaconda exterior to ArcGIS.
