# Python Dataviz Toolbox

Useful libraries and scripts to perform reading, postprocessing, data conversion, regridding and masking to display georeferenced data in maps. 

## 01 Data Structures
Basic data files operations are explained including: 
* [JSON to Pandas]( 
Notebooks/01-Data_Structures/00_JSON_to_PANDAS.ipynb). 
* [CSV to Pandas]( 
Notebooks/01-Data_Structures/01-CSV_to_PANDAS.ipynb). 
* [CSV to Parent/Child JSON]( 
Notebooks/01-Data_Structures/02-CSV_to_ParentChild_JSON.ipynb). 
* [Pandas Numerical Filtering]( 
Notebooks/01-Data_Structures/03-Pandas_Numerical_Filtering_Cleaning.ipynb). 
* [Pandas Text Filtering]( 
Notebooks/01-Data_Structures/04-Pandas_Text_Filtering_Cleaning.ipynb). 

## 02 Basic Plots
A quick overview of the data can be done with plots using the Matplotlib library:
* [Scatter Plot]( 
Notebooks/02-Basic_Plots/00-Scatter_Plot.ipynb). 
* [Scatter Regression]( 
Notebooks/02-Basic_Plots/01-Scatter_Regression.ipynb). 
* [Time Series]( 
Notebooks/02-Basic_Plots/02-Time_Series.ipynb). 
* [Histogram]( 
Notebooks/02-Basic_Plots/03-Histogram.ipynb). 

## 03 GeoData Formats
Model output, dataproducts and observational datasets often come in georeferenced data formats. Conversion of these formats is done through:  
* [CSV to GeoJSON]( 
Notebooks/03-GeoData_Formats/00-Convert_CSV_to_GeoJSON.ipynb). 
* [NetCDF to JSON]( 
Notebooks/03-GeoData_Formats/01-Convert_NetCDF_to_JSON.ipynb). 
* [NetCDF Contours to GeoJSON]( 
Notebooks/03-GeoData_Formats/02-Convert_NetCDF_Contours_to_GeoJSON.ipynb). 
* [NetCDF to TIF]( 
Notebooks/03-GeoData_Formats/03-Convert_NetCDF_to_TIFF.ipynb). 
* [NetCDF to DAT]( 
Notebooks/03-GeoData_Formats/04-Convert_NetCDF_to_DAT.ipynb). 
* [Open MAT]( 
Notebooks/03-GeoData_Formats/05-Open_MAT_file_format.ipynb). 
* [TIF to NetCDF]( 
Notebooks/03-GeoData_Formats/06-Convert_TIF_to_NetCDF.ipynb). 
* [SHP to GeoJSON]( 
Notebooks/03-GeoData_Formats/07-Convert_SHP_to_GeoJSON.ipynb). 

## 04 Regridding and Masking
Operating or just comparing datasets involves a common meshgrid in all input files, or just clipping certain areas of interest. Here is how: 
* [Regridding Xarray]( 
Notebooks/04-GeoData_Regridding_and_Masking/00-Regridding_Xarray.ipynb).
* [SHP into Gridpoints]( 
Notebooks/04-GeoData_Regridding_and_Masking/01-Convert_SHP_into_Discrete_Gridpoints.ipynb).
* [Mask NetCDF with SHP]( 
Notebooks/04-GeoData_Regridding_and_Masking/02-Mask_NetCDF_with_SHP.ipynb).
* [Calculate Area of SHP]( 
Notebooks/04-GeoData_Regridding_and_Masking/03-Calculate_Area_from_SHP.ipynb).
* [Seed Random dots on SHP]( 
Notebooks/04-GeoData_Regridding_and_Masking/04-Seed_Random_Dots_on_SHP.ipynb).

## 05 Mapping
Plotting georeferenced files in native Python libraries always helps to understand the data: 
* [NetCDF and SHP in Matplotlib]( 
Notebooks/05-Mapping/01-Plot_NetCDF_in_Matplotlib_plus_SHP.ipynb).
* [NetCDF in Cartopy]( 
Notebooks/05-Mapping/02-Plot_NetCDF_in_Cartopy.ipynb).
* [NetCDF Contour in Folium]( 
Notebooks/05-Mapping/03-Plot_NetCDF_Contour_in_Folium.ipynb).
* [TIF in Cartopy]( 
Notebooks/05-Mapping/04-Plot_TIF_in_Cartopy.ipynb).
* [TIF in Matplotlib]( 
Notebooks/05-Mapping/05-Plot_TIF_in_Matplotlib.ipynb).
* [Multiple SHP in Matplotlib]( 
Notebooks/05-Mapping/06-Plot_Multiple_SHP_in_Matplotlib.ipynb).
* [SHP in Folium]( 
Notebooks/05-Mapping/07-Plot_SHP_in_Folium.ipynb).

## 06 Text Analysis
NLTK is a simple yet powerful library to extract basic metrics in text based datasets: 
* [Keyword Rank and Frequency]( 
Notebooks/06-Text_Analysis/00-Word_Frequency_in_JSON.ipynb).