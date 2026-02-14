# Time Series Data Handling and Analysis

## Introduction to Time Series Data
Time series data is a sequence of data points recorded at specific time intervals. In hydrology, this could include rainfall data, river discharge data, soil moisture, ET etc.

### Key Concepts:
- **Temporal ordering**: Time series data is ordered in time.
- **Frequency**: The time interval between data points (e.g., daily, monthly).
- **Trends and seasonality**: Long-term increase or decrease and regular patterns that repeat over time.

## Working with Dates and Times in Python
Python's `datetime` module and `pandas` library provide powerful tools for working with date and time data.


```python
import pandas as pd
import numpy as np

```


```python
# Example of creating a datetime object
date_str = '2024-12-14'

print (type(date_str))
print (date_str)
```


```python
# Convert String object to datetime object

from datetime import datetime
date_obj = datetime.strptime(date_str, '%Y-%m-%d')
print (type(date_obj))
print (date_obj)
```

### Learn more about strptime https://www.geeksforgeeks.org/python-datetime-strptime-function/


```python
# Understading the format
date1 = '09-11-2001' # MM-DD-YYYY
date2 = '09-11-2001' # DD-MM-YYYY

date3 = "09-NOV-2001"
date4 = "09/NOV/2001"
date5 = "09/NOV/2001 15:30:00"


date1 = datetime.strptime(date1, '%m-%d-%Y')
date2 = datetime.strptime(date2, '%d-%m-%Y')
date3 = datetime.strptime(date3, "%d-%b-%Y")
date4 = datetime.strptime(date4, "%d/%b/%Y")
date5 = datetime.strptime(date5, "%d/%b/%Y %H:%M:%S")


print (date1)
print (date2)
print (date3)
print (date4)
print (date5)
```

## Creating and Manipulating Time Series Data
Pandas makes it easy to create and manipulate time series data. Let's start by creating a simple time series of daily rainfall data.


```python
# Creating a date range with daily frequecny 
date_range = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')

# Creating a time series with random rainfall data
rainfall_data = np.random.randint(0, 100, size=len(date_range))
rainfall_series = pd.Series(data=rainfall_data, index=date_range)
rainfall_series
```


```python
# Plotting the data series
rainfall_series.plot()
```

### Reading a time series data from CSV file


```python
# Read the CSV file
file_path = r'D:\NIH\Training\Python for water\Slides\Day-4\TRMM_3H_2000_2018_Delhi_1.csv'
rainfall_data = pd.read_csv(file_path)
print (rainfall_data.dtypes)
rainfall_data
```


```python
# Converting colomn type to datetime object

rainfall_data['Dates'] = pd.to_datetime(rainfall_data['Dates'], format='%Y-%m-%d %H:%M:%S')
print (rainfall_data.dtypes)
rainfall_data
```


```python
rainfall_data.plot()
```


```python
# To plot the data change the date colomn as index colomn
rainfall_data.set_index('Dates', inplace=True)
rainfall_data.plot()
```

## Resampling and Aggregating Time Series Data
Resampling involves changing the frequency of your time series observations. Common resampling operations include downsampling (reducing frequency) and upsampling (increasing frequency).
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html


```python
# Resampling the 3 Houlry data rainfall data to daily and monthly sums

daily_rainfall = rainfall_data.resample('D').sum()
monthly_rainfall = rainfall_data.resample('M').sum()
monthly_rainfall
```


```python
monthly_rainfall.plot()
```

## Time Series Indexing and Slicing
Datetime indexing: Allows selecting data by specifying dates.


```python
# Slicing Year-wise: All values for the year 2015
monthly_rainfall_2015 = monthly_rainfall.loc['2015']
monthly_rainfall_2015

```


```python
# Slicing Month-wise: From June 2015 to September 2015
df_june_sept_2015 = monthly_rainfall.loc['2015-06':'2015-09']
df_june_sept_2015
```


```python
# Slicing Month-wise: All January values
df_jan_all_years = monthly_rainfall[monthly_rainfall.index.month == 1]
df_jan_all_years
```


```python
# Extracting all June to sept values
monsoon_rainfall = monthly_rainfall[monthly_rainfall.index.month.isin([6, 7, 8, 9])]
monsoon_rainfall
```


```python
# Slicing Date-wise: From 01-01-2003 to 14-10-2005
df_specific_dates = monthly_rainfall.loc['2003-01-01':'2005-10-14']
df_specific_dates
```


```python

# Datetime properties: Extract year, month, day, etc., which can be useful for feature engineering.

daily_rainfall['year'] = daily_rainfall.index.year
daily_rainfall['month'] = daily_rainfall.index.month
daily_rainfall['day'] = daily_rainfall.index.day
daily_rainfall['day_of_week'] = daily_rainfall.index.dayofweek

daily_rainfall
```


```python
# Delete the index colomn

daily_rainfall.reset_index(drop=True, inplace=True)
daily_rainfall
```


```python
# Create date colomn and convert it into datetime format
daily_rainfall['dates'] = pd.to_datetime(daily_rainfall[['year','month','day']])

# Make the date colomn as index colomn
daily_rainfall.set_index('dates', inplace=True)

daily_rainfall
```


<iframe width="560" height="315" src="https://www.youtube.com/embed/vHaJttWUCNg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Lecture Visualization

<embed src="pdfs/Time Series in Python.pdf" type="application/pdf" width="100%" height="600px" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />

<p align="center"><a href="pdfs/Time Series in Python.pdf" class="md-button md-button--primary">Download Lecture Slides</a></p>

??? info "View Full Lecture Transcript"
    The following content is extracted from the lecture slides.

    Time Series Analysis

    using Python

    Sukant Jain,

    Scientist C

    National Institute of Hydrology,

    Roorkee

    sukant.nihr@gov.in

    Gridded Format for Storing Climate Data

    What is Gridded Data?

    Definition

    Gridded data organizes

    spatial and temporal

    information into a

    structured grid, where

    each cell represents a

    specific location or time

    interval.

    Structure

    Each cell in the grid

    contains data values

    such as temperature,

    precipitation, or wind

    speed, providing a

    comprehensive

    representation of

    environmental

    conditions.

    Applications

    Gridded data is widely

    used in climate

    modeling, weather

    forecasting, and

    environmental

    monitoring, providing

    valuable insights into

    climate change and its

    impacts.

    What is Gridded Data?

    Efficiency of Gridded Data Storage

    CSV Files

    CSV files are simple and easy to use, but they suffer from data redundancy,

    large file sizes, and slow access times, making them inefficient for storing

    large datasets.

    Gridded Data Formats

    Gridded data formats are designed for efficient storage, reducing redundancy

    and enabling faster access times. They are well-suited for handling massive

    datasets.

    Advantages

    Gridded data formats provide improved data organization, efficient storage,

    reduced redundancy, and enhanced accessibility, making them ideal for large-

    scale climate data analysis.

    Disadvantages

    Specialized software is required to access and manipulate data in gridded

    formats, necessitating specific skills and tools for efficient utilization.

    Different Formats of Gridded Data

    • NetCDF (Network Common Data Form) is widely used in climate and meteorological

    data, supporting large, multi-dimensional arrays of data.

    • HDF5 (Hierarchical Data Format) is a flexible and self-describing format that is well-

    suited for storing complex data hierarchies.

    • GRIB (GRIdded Binary) is a widely used format for storing meteorological data. It is

    standardized by the WMO

    • GeoTIFF (Geographic Tagged Image File Format) is a standard format for storing

    georeferenced raster data. It supports a wide range of spatial data types, including

    elevation, land cover, and precipitation.

    Tools for Extracting Data from Gridded Formats

    Type Tools Description

    Python Libraries netCDF4, h5py, xarray Python libraries provide functionalities for reading

    and writing NetCDF, HDF5, and other gridded data

    formats.

    Command Line Tools ncdump, h5dump,

    cdo

    Command line tools offer efficient ways to extract

    data from gridded formats, convert data between

    formats, and perform basic data manipulations.

    Software Applications Panoply, ArcGIS, QGIS Specialized software applications provide interactive

    environments for visualizing, analyzing, and

    manipulating gridded data.

    Cloud Computing

    Platform

    Google Earth Engine Very easy to play around the gridded data hosted in

    that platform

    PYTHON PACKAGE

    A Python package or module is a collection of Python code, such as functions and classes, organized to perform

    specific tasks or solve problems efficiently.

    • xarray: Provides data structures for multi-dimensional arrays, enabling efficient manipulation and analysis of

    labeled data.

    • pandas: Offers powerful data structures like DataFrames for data manipulation and analysis, making it a staple

    for data science.

    • numpy: Provides support for large, multi-dimensional arrays and matrices, along with a collection of

    mathematical functions to operate on them.



<iframe width="560" height="315" src="https://www.youtube.com/embed/vHaJttWUCNg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Lecture Visualization

<embed src="pdfs/Time Series in Python.pdf" type="application/pdf" width="100%" height="600px" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />

<p align="center"><a href="pdfs/Time Series in Python.pdf" class="md-button md-button--primary">Download Lecture Slides</a></p>

??? info "View Full Lecture Transcript"
    The following content is extracted from the lecture slides.

    Time Series Analysis

    using Python

    Sukant Jain,

    Scientist C

    National Institute of Hydrology,

    Roorkee

    sukant.nihr@gov.in

    Gridded Format for Storing Climate Data

    What is Gridded Data?

    Definition

    Gridded data organizes

    spatial and temporal

    information into a

    structured grid, where

    each cell represents a

    specific location or time

    interval.

    Structure

    Each cell in the grid

    contains data values

    such as temperature,

    precipitation, or wind

    speed, providing a

    comprehensive

    representation of

    environmental

    conditions.

    Applications

    Gridded data is widely

    used in climate

    modeling, weather

    forecasting, and

    environmental

    monitoring, providing

    valuable insights into

    climate change and its

    impacts.

    What is Gridded Data?

    Efficiency of Gridded Data Storage

    CSV Files

    CSV files are simple and easy to use, but they suffer from data redundancy,

    large file sizes, and slow access times, making them inefficient for storing

    large datasets.

    Gridded Data Formats

    Gridded data formats are designed for efficient storage, reducing redundancy

    and enabling faster access times. They are well-suited for handling massive

    datasets.

    Advantages

    Gridded data formats provide improved data organization, efficient storage,

    reduced redundancy, and enhanced accessibility, making them ideal for large-

    scale climate data analysis.

    Disadvantages

    Specialized software is required to access and manipulate data in gridded

    formats, necessitating specific skills and tools for efficient utilization.

    Different Formats of Gridded Data

    • NetCDF (Network Common Data Form) is widely used in climate and meteorological

    data, supporting large, multi-dimensional arrays of data.

    • HDF5 (Hierarchical Data Format) is a flexible and self-describing format that is well-

    suited for storing complex data hierarchies.

    • GRIB (GRIdded Binary) is a widely used format for storing meteorological data. It is

    standardized by the WMO

    • GeoTIFF (Geographic Tagged Image File Format) is a standard format for storing

    georeferenced raster data. It supports a wide range of spatial data types, including

    elevation, land cover, and precipitation.

    Tools for Extracting Data from Gridded Formats

    Type Tools Description

    Python Libraries netCDF4, h5py, xarray Python libraries provide functionalities for reading

    and writing NetCDF, HDF5, and other gridded data

    formats.

    Command Line Tools ncdump, h5dump,

    cdo

    Command line tools offer efficient ways to extract

    data from gridded formats, convert data between

    formats, and perform basic data manipulations.

    Software Applications Panoply, ArcGIS, QGIS Specialized software applications provide interactive

    environments for visualizing, analyzing, and

    manipulating gridded data.

    Cloud Computing

    Platform

    Google Earth Engine Very easy to play around the gridded data hosted in

    that platform

    PYTHON PACKAGE

    A Python package or module is a collection of Python code, such as functions and classes, organized to perform

    specific tasks or solve problems efficiently.

    • xarray: Provides data structures for multi-dimensional arrays, enabling efficient manipulation and analysis of

    labeled data.

    • pandas: Offers powerful data structures like DataFrames for data manipulation and analysis, making it a staple

    for data science.

    • numpy: Provides support for large, multi-dimensional arrays and matrices, along with a collection of

    mathematical functions to operate on them.

