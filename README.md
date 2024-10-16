# Python Dataviz Toolbox

Useful libraries and scripts to perform reading, postprocessing and data conversion to display georeferenced data in maps. 

## 00 Coding Framework
In the first module we learn how to install a basic Python interpreter such as Anaconda. 

## 01 Data Structures
Basic data structures are explained with simple examples, including: 
* Array
* List
* Dictionary
* Pandas

## 02 Basic Matplotlib Plots
A quick overview of the data can be done with plots using the Matplotlib library
* Scatter Plot
* Time Series
* Historgram
* Bar Chart
* Error Bars
* Legend
* Shapes
* Text on Plots

## 03 GeoData Formats
Model output, dataproducts and observational datasets often come in georeferenced data formats, such as: 
* .NetCDF
* .TIFF
* .GeoTIFF
* .GRIB
* .SHP
* .IMG

Basic operations can be performed at this stage like: 
* Masking
* Clipping

Dataviz output aim at lightweigth, javascript based libraries, hence a conversion into other formats is necessary. This includes: 
* Xarray
* Geopandas
* .JSON
* .GeoJSON
* .DAT

Conversion among formats is done via: 
[Convert .CSV to .JSON](
Notebooks/03/Convert_CSV_to_JSON.ipynb).  


## 04 Mapping
Mapping largely involves representation of either: 
* Discrete elements
* Contour plots and areas
* Binning via hexagons or other polygons

Different techniques are explored to plot the data using a variety of libraries: 
* D3.js
* Leaflet
* Folium
* Kepler
  
## 05 Web Editing
Once the data is shown in web-based platforms, some basic web editing is sometimes desirable on: 
* HTML
* CSS
