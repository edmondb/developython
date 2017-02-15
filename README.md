# developython
Python Training for the DEVELOP program.

# Setup Instructions

1. [Download](https://www.continuum.io/downloads) and install __Anaconda for Windows 32-Bit (Python 2.7)__
2. Do not make it your default Python (possible conflicts with other Python versions or if using arcPy).
3. Start -> All Programs -> Anaconda 2 (32-Bit) -> Anaconda Prompt
4. _Create script for this:_ `Copy C:\Python27\ArcGIS10.3\Lib\site-packages\Desktop10.3.pth C:\Users\`__username__`\AppData\Local\Continuum\Anaconda2\site_packages\`
5. `conda update conda`
6. `conda install gdal netCDF4`

_To Do:_ Correct GDAL_DATA env var to be `C:\Users\`__username__`\AppData\Local\Continuum\Anaconda2\Library\share\gdal`
