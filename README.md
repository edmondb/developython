# developython
Python Training for the DEVELOP program.

# Setup Instructions

1. [Download](https://www.continuum.io/downloads) and install __Anaconda for Windows 32-Bit (Python 2.7)__
2. Do not make it your default Python (possible conflicts with other Python versions or if using arcPy).
3. Start -> All Programs -> Anaconda 2 (32-Bit) -> Anaconda Prompt
4. _Create script for this:_ `Copy C:\Python27\ArcGIS10.3\Lib\site-packages\Desktop10.3.pth C:\Users\`__username__`\AppData\Local\Continuum\Anaconda2\site_packages\`

---

1. [Download](http://www.continuum.io/downloads#_windows) and install Anaconda for Windows 64-Bit (Python 2.7)
2. Do not make it your default Python (possible conflicts with other Python versions or if using arcPy).
3. Do not add it to your path (can change depending upon use with GDAL).
4. Start -> All Programs -> Anaconda 2 (64-Bit) -> Anaconda Prompt
5. `conda install netCDF4 basemap`
6. `conda install conda=4.1.11`
7. `conda install -c conda-forge gdal`
8. `conda install h5py`
8. Close your Anaconda Prompt to retain the changes and then open again to test installation.

### And if all else fails:

1. `conda install conda=4.1.11`
2. Exit Anaconda Prompt
3. `conda create -n GDAL python=2.7 gdal -c conda-forge`
4. `activate GDAL`

To Test GDAL install:

1. Download this [file](https://drive.google.com/file/d/0B9m0kGaHo6cnM0JxbkM5aFZvN28/view?usp=sharing)
2. `cd` to Downloads directory
3. `gdalwarp -t_srs "EPSG:32645" 1400412014302_to_1400412014206.tif test.tif`

# TODO:
1. Connect arcpy with Anaconda exterior to ArcGIS.
