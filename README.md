# developython
Python Training for the DEVELOP program.

# Setup Instructions (User Account & GDAL)

1. [Download](http://www.continuum.io/downloads#_windows) and install Anaconda for Windows 64-Bit (Python 2.7)
2. Do not make it your default Python (possible conflicts with other Python versions or if using arcPy).
3. Do not add it to your path (can change depending upon use with GDAL).
4. Start -> All Programs -> Anaconda 2 (64-Bit) -> Anaconda Prompt
5. `conda install netCDF4 basemap`
6. `conda install -c conda-forge gdal`
    no `conda upgrade numpy`?
7. `conda update gdal` __(mine was already updated)__
8. `set GDAL_DATA = C:\Users\TEMP\AppData\Local\Continuum\Anaconda2\Lib\site-packages\gdal-2.1.1-np111py27_2\Library\Share\gdal` __(didn't have to set this)__

To Test GDAL install: 
1. Download this [file](https://drive.google.com/file/d/0B9m0kGaHo6cnM0JxbkM5aFZvN28/view?usp=sharing)
2. `cd` to Downloads directory
3. `gdalwarp -t_srs "EPSG:32645" 1400412014302_to_1400412014206.tif test.tif`

How do we know it worked?
I got this output:

    gdalwarp -t_srs "EPSG:32645" Downloads\1400412014302_to_1400412014206.tif test.tif
    0...10...20...30...40...50...60...70...80...90...100 - done.

# TODO:
1. Connect arcpy with Anaconda exterior to ArcGIS.
