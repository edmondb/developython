# developython
Python Training for the DEVELOP program.

# Setup Instructions (User Account & GDAL)

1. [Download](http://www.continuum.io/downloads#_windows) and install Anaconda for Windows 64-Bit (Python 2.7)
2. Do not make it your default Python (possible conflicts with other Python versions or if using arcPy).
3. Do not add it to your path (can change depending upon use with GDAL).
4. Start -> All Programs -> Anaconda 2 (64-Bit) -> Anaconda Prompt
5. `conda install gdal netCDF4 basemap`
6. `conda upgrade numpy`

TODO:

1. Edit and set GDAL_DATA env variable (for reprojections; gcs.csv file).
2. Connect arcpy with Anaconda exterior to ArcGIS.
