## Importing Modules/Packages


```python
#Error due to use of sqrt() method of math module without importing the module
sqrt(16)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_1940/244926836.py in <module>
    ----> 1 sqrt(16)
    

    NameError: name 'sqrt' is not defined



```python
import math
```


```python
math.sqrt(16)
```




    4.0




```python
#import pandas package by renaming it
import pandas as pd
```


```python
#importing specific function/method instead of whole module
from math import sqrt
```


```python
sqrt(4)
```




    2.0




```python
#import of submodule inside a module after renaming it
import matplotlib.pyplot as plt
```

## Creation of DataFrame/Series from scratch


```python
#Creation of Pandas Series by passing a list of values
dams = pd.Series(['Bhakra','Almatti','Indira Sagar','Hirakud','Mettur','Tehri'],name="Dams")
```


```python
type(dams)
```




    pandas.core.series.Series




```python
dams
```




    0          Bhakra
    1         Almatti
    2    Indira Sagar
    3         Hirakud
    4          Mettur
    5           Tehri
    Name: Dams, dtype: object




```python
river = pd.Series(['Sutlej','Krishna','Narmada','Mahanadi','Cauvery','Bhagirathi'],name="River")
```


```python
river
```




    0        Sutlej
    1       Krishna
    2       Narmada
    3      Mahanadi
    4       Cauvery
    5    Bhagirathi
    Name: River, dtype: object




```python
state = pd.Series(['HP','Karnataka','MP','Odisha','Tamil Nadu','Uttarakhand'],name='State')
```


```python
year_of_completion = pd.Series([1963,2000,2006,1956,1934,2006],name='Year')
```


```python
year_of_completion
```




    0    1963
    1    2000
    2    2006
    3    1956
    4    1934
    5    2006
    Name: Year, dtype: int64




```python
height_of_dam = pd.Series([225.5,49.3,91.4,60.9,70.4,260.5],name="Height")
```


```python
height_of_dam
```




    0    225.5
    1     49.3
    2     91.4
    3     60.9
    4     70.4
    5    260.5
    Name: Height, dtype: float64




```python
#creation of empty Pandas Dataframe
Dam_Register = pd.DataFrame()
```


```python
type(Dam_Register)
```




    pandas.core.frame.DataFrame




```python
Dam_Register
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
#creation of a dictionary with intended column headers as keys and Pandas Series as values 
dictionary1 = {"Dams":dams,"River":river,"State":state,"Year":year_of_completion,"Height(m)":height_of_dam}
```


```python
dictionary1
```




    {'Dams': 0          Bhakra
     1         Almatti
     2    Indira Sagar
     3         Hirakud
     4          Mettur
     5           Tehri
     Name: Dams, dtype: object,
     'River': 0        Sutlej
     1       Krishna
     2       Narmada
     3      Mahanadi
     4       Cauvery
     5    Bhagirathi
     Name: River, dtype: object,
     'State': 0             HP
     1      Karnataka
     2             MP
     3         Odisha
     4     Tamil Nadu
     5    Uttarakhand
     Name: State, dtype: object,
     'Year': 0    1963
     1    2000
     2    2006
     3    1956
     4    1934
     5    2006
     Name: Year, dtype: int64,
     'Height(m)': 0    225.5
     1     49.3
     2     91.4
     3     60.9
     4     70.4
     5    260.5
     Name: Height, dtype: float64}




```python
#creation of Pandas DataFrame by passing a dictionary of Pandas Series 
Dam_Register = pd.DataFrame(dictionary1)
```


```python
Dam_Register
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dams</th>
      <th>River</th>
      <th>State</th>
      <th>Year</th>
      <th>Height(m)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bhakra</td>
      <td>Sutlej</td>
      <td>HP</td>
      <td>1963</td>
      <td>225.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Almatti</td>
      <td>Krishna</td>
      <td>Karnataka</td>
      <td>2000</td>
      <td>49.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Indira Sagar</td>
      <td>Narmada</td>
      <td>MP</td>
      <td>2006</td>
      <td>91.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hirakud</td>
      <td>Mahanadi</td>
      <td>Odisha</td>
      <td>1956</td>
      <td>60.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mettur</td>
      <td>Cauvery</td>
      <td>Tamil Nadu</td>
      <td>1934</td>
      <td>70.4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Tehri</td>
      <td>Bhagirathi</td>
      <td>Uttarakhand</td>
      <td>2006</td>
      <td>260.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(Dam_Register)
```




    pandas.core.frame.DataFrame




```python
#describe() method for printing basic statistics of numerical data contained in the Pandas DataFrame
Dam_Register.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Height(m)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>6.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1977.500000</td>
      <td>126.333333</td>
    </tr>
    <tr>
      <th>std</th>
      <td>30.644739</td>
      <td>92.086105</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1934.000000</td>
      <td>49.300000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1957.750000</td>
      <td>63.275000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1981.500000</td>
      <td>80.900000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2004.500000</td>
      <td>191.975000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2006.000000</td>
      <td>260.500000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#printing columns attribute of Pandas DataFrame 
Dam_Register.columns
```




    Index(['Dams', 'River', 'State', 'Year', 'Height(m)'], dtype='object')




```python
#printing index attribute of Pandas Dataframe
Dam_Register.index
```




    RangeIndex(start=0, stop=6, step=1)




```python
#By default head() method prints first 5 rows of Pandas DataFrame 
Dam_Register.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dams</th>
      <th>River</th>
      <th>State</th>
      <th>Year</th>
      <th>Height(m)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bhakra</td>
      <td>Sutlej</td>
      <td>HP</td>
      <td>1963</td>
      <td>225.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Almatti</td>
      <td>Krishna</td>
      <td>Karnataka</td>
      <td>2000</td>
      <td>49.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Indira Sagar</td>
      <td>Narmada</td>
      <td>MP</td>
      <td>2006</td>
      <td>91.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hirakud</td>
      <td>Mahanadi</td>
      <td>Odisha</td>
      <td>1956</td>
      <td>60.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mettur</td>
      <td>Cauvery</td>
      <td>Tamil Nadu</td>
      <td>1934</td>
      <td>70.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
#head() method with parameter passed into it prints same number of header rows of the Pandas DataFrame 
Dam_Register.head(4)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dams</th>
      <th>River</th>
      <th>State</th>
      <th>Year</th>
      <th>Height(m)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bhakra</td>
      <td>Sutlej</td>
      <td>HP</td>
      <td>1963</td>
      <td>225.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Almatti</td>
      <td>Krishna</td>
      <td>Karnataka</td>
      <td>2000</td>
      <td>49.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Indira Sagar</td>
      <td>Narmada</td>
      <td>MP</td>
      <td>2006</td>
      <td>91.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hirakud</td>
      <td>Mahanadi</td>
      <td>Odisha</td>
      <td>1956</td>
      <td>60.9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#tail() method with parameter passed into it prints same number of tail rows of the Pandas DataFrame
Dam_Register.tail(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dams</th>
      <th>River</th>
      <th>State</th>
      <th>Year</th>
      <th>Height(m)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Tehri</td>
      <td>Bhagirathi</td>
      <td>Uttarakhand</td>
      <td>2006</td>
      <td>260.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
#info() method prints basic information about the Pandas DataFrame
Dam_Register.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6 entries, 0 to 5
    Data columns (total 5 columns):
     #   Column     Non-Null Count  Dtype  
    ---  ------     --------------  -----  
     0   Dams       6 non-null      object 
     1   River      6 non-null      object 
     2   State      6 non-null      object 
     3   Year       6 non-null      int64  
     4   Height(m)  6 non-null      float64
    dtypes: float64(1), int64(1), object(3)
    memory usage: 368.0+ bytes
    


```python
#Import of modules for file path handling
import pathlib
import os
home = pathlib.Path.home()
home
```




    WindowsPath('C:/Users/COMP109')




```python
#file path to csv file 
fp = home / "PythonWRM" / "Data" / "Gauge_Discharge_data.csv"
fp
```




    WindowsPath('C:/Users/COMP109/PythonWRM/Data/Gauge_Discharge_data.csv')




```python
#Pandas provides read_*.() to read data from multiple formats
Gauge_Discharge_data = pd.read_csv(fp)
```


```python
type(Gauge_Discharge_data)
```




    pandas.core.frame.DataFrame




```python
Gauge_Discharge_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Day</th>
      <th>Data Type</th>
      <th>Mean Gauge (m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01-01-2005</td>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.473</td>
      <td>O</td>
    </tr>
    <tr>
      <th>1</th>
      <td>02-01-2005</td>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.270</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>03-01-2005</td>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.033</td>
      <td>O</td>
    </tr>
    <tr>
      <th>3</th>
      <td>04-01-2005</td>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.476</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4</th>
      <td>05-01-2005</td>
      <td>HZS</td>
      <td>3.020</td>
      <td>58.202</td>
      <td>O</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4012</th>
      <td>27-12-2015</td>
      <td>HHS</td>
      <td>258.040</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4013</th>
      <td>28-12-2015</td>
      <td>HZS</td>
      <td>3.040</td>
      <td>55.259</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4014</th>
      <td>29-12-2015</td>
      <td>HZS</td>
      <td>3.005</td>
      <td>51.204</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4015</th>
      <td>30-12-2015</td>
      <td>HZS</td>
      <td>3.000</td>
      <td>50.639</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4016</th>
      <td>31-12-2015</td>
      <td>HZS</td>
      <td>2.905</td>
      <td>41.459</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
<p>4017 rows × 5 columns</p>
</div>




```python
help(pd.read_csv)
```

    Help on function read_csv in module pandas.io.parsers.readers:
    
    read_csv(filepath_or_buffer: 'FilePathOrBuffer', sep=<no_default>, delimiter=None, header='infer', names=<no_default>, index_col=None, usecols=None, squeeze=False, prefix=<no_default>, mangle_dupe_cols=True, dtype: 'DtypeArg | None' = None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal: 'str' = '.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors: 'str | None' = 'strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options: 'StorageOptions' = None)
        Read a comma-separated values (csv) file into DataFrame.
        
        Also supports optionally iterating or breaking of the file
        into chunks.
        
        Additional help can be found in the online docs for
        `IO Tools <https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html>`_.
        
        Parameters
        ----------
        filepath_or_buffer : str, path object or file-like object
            Any valid string path is acceptable. The string could be a URL. Valid
            URL schemes include http, ftp, s3, gs, and file. For file URLs, a host is
            expected. A local file could be: file://localhost/path/to/table.csv.
        
            If you want to pass in a path object, pandas accepts any ``os.PathLike``.
        
            By file-like object, we refer to objects with a ``read()`` method, such as
            a file handle (e.g. via builtin ``open`` function) or ``StringIO``.
        sep : str, default ','
            Delimiter to use. If sep is None, the C engine cannot automatically detect
            the separator, but the Python parsing engine can, meaning the latter will
            be used and automatically detect the separator by Python's builtin sniffer
            tool, ``csv.Sniffer``. In addition, separators longer than 1 character and
            different from ``'\s+'`` will be interpreted as regular expressions and
            will also force the use of the Python parsing engine. Note that regex
            delimiters are prone to ignoring quoted data. Regex example: ``'\r\t'``.
        delimiter : str, default ``None``
            Alias for sep.
        header : int, list of int, default 'infer'
            Row number(s) to use as the column names, and the start of the
            data.  Default behavior is to infer the column names: if no names
            are passed the behavior is identical to ``header=0`` and column
            names are inferred from the first line of the file, if column
            names are passed explicitly then the behavior is identical to
            ``header=None``. Explicitly pass ``header=0`` to be able to
            replace existing names. The header can be a list of integers that
            specify row locations for a multi-index on the columns
            e.g. [0,1,3]. Intervening rows that are not specified will be
            skipped (e.g. 2 in this example is skipped). Note that this
            parameter ignores commented lines and empty lines if
            ``skip_blank_lines=True``, so ``header=0`` denotes the first line of
            data rather than the first line of the file.
        names : array-like, optional
            List of column names to use. If the file contains a header row,
            then you should explicitly pass ``header=0`` to override the column names.
            Duplicates in this list are not allowed.
        index_col : int, str, sequence of int / str, or False, default ``None``
          Column(s) to use as the row labels of the ``DataFrame``, either given as
          string name or column index. If a sequence of int / str is given, a
          MultiIndex is used.
        
          Note: ``index_col=False`` can be used to force pandas to *not* use the first
          column as the index, e.g. when you have a malformed file with delimiters at
          the end of each line.
        usecols : list-like or callable, optional
            Return a subset of the columns. If list-like, all elements must either
            be positional (i.e. integer indices into the document columns) or strings
            that correspond to column names provided either by the user in `names` or
            inferred from the document header row(s). For example, a valid list-like
            `usecols` parameter would be ``[0, 1, 2]`` or ``['foo', 'bar', 'baz']``.
            Element order is ignored, so ``usecols=[0, 1]`` is the same as ``[1, 0]``.
            To instantiate a DataFrame from ``data`` with element order preserved use
            ``pd.read_csv(data, usecols=['foo', 'bar'])[['foo', 'bar']]`` for columns
            in ``['foo', 'bar']`` order or
            ``pd.read_csv(data, usecols=['foo', 'bar'])[['bar', 'foo']]``
            for ``['bar', 'foo']`` order.
        
            If callable, the callable function will be evaluated against the column
            names, returning names where the callable function evaluates to True. An
            example of a valid callable argument would be ``lambda x: x.upper() in
            ['AAA', 'BBB', 'DDD']``. Using this parameter results in much faster
            parsing time and lower memory usage.
        squeeze : bool, default False
            If the parsed data only contains one column then return a Series.
        prefix : str, optional
            Prefix to add to column numbers when no header, e.g. 'X' for X0, X1, ...
        mangle_dupe_cols : bool, default True
            Duplicate columns will be specified as 'X', 'X.1', ...'X.N', rather than
            'X'...'X'. Passing in False will cause data to be overwritten if there
            are duplicate names in the columns.
        dtype : Type name or dict of column -> type, optional
            Data type for data or columns. E.g. {'a': np.float64, 'b': np.int32,
            'c': 'Int64'}
            Use `str` or `object` together with suitable `na_values` settings
            to preserve and not interpret dtype.
            If converters are specified, they will be applied INSTEAD
            of dtype conversion.
        engine : {'c', 'python'}, optional
            Parser engine to use. The C engine is faster while the python engine is
            currently more feature-complete.
        converters : dict, optional
            Dict of functions for converting values in certain columns. Keys can either
            be integers or column labels.
        true_values : list, optional
            Values to consider as True.
        false_values : list, optional
            Values to consider as False.
        skipinitialspace : bool, default False
            Skip spaces after delimiter.
        skiprows : list-like, int or callable, optional
            Line numbers to skip (0-indexed) or number of lines to skip (int)
            at the start of the file.
        
            If callable, the callable function will be evaluated against the row
            indices, returning True if the row should be skipped and False otherwise.
            An example of a valid callable argument would be ``lambda x: x in [0, 2]``.
        skipfooter : int, default 0
            Number of lines at bottom of file to skip (Unsupported with engine='c').
        nrows : int, optional
            Number of rows of file to read. Useful for reading pieces of large files.
        na_values : scalar, str, list-like, or dict, optional
            Additional strings to recognize as NA/NaN. If dict passed, specific
            per-column NA values.  By default the following values are interpreted as
            NaN: '', '#N/A', '#N/A N/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN', '-nan',
            '1.#IND', '1.#QNAN', '<NA>', 'N/A', 'NA', 'NULL', 'NaN', 'n/a',
            'nan', 'null'.
        keep_default_na : bool, default True
            Whether or not to include the default NaN values when parsing the data.
            Depending on whether `na_values` is passed in, the behavior is as follows:
        
            * If `keep_default_na` is True, and `na_values` are specified, `na_values`
              is appended to the default NaN values used for parsing.
            * If `keep_default_na` is True, and `na_values` are not specified, only
              the default NaN values are used for parsing.
            * If `keep_default_na` is False, and `na_values` are specified, only
              the NaN values specified `na_values` are used for parsing.
            * If `keep_default_na` is False, and `na_values` are not specified, no
              strings will be parsed as NaN.
        
            Note that if `na_filter` is passed in as False, the `keep_default_na` and
            `na_values` parameters will be ignored.
        na_filter : bool, default True
            Detect missing value markers (empty strings and the value of na_values). In
            data without any NAs, passing na_filter=False can improve the performance
            of reading a large file.
        verbose : bool, default False
            Indicate number of NA values placed in non-numeric columns.
        skip_blank_lines : bool, default True
            If True, skip over blank lines rather than interpreting as NaN values.
        parse_dates : bool or list of int or names or list of lists or dict, default False
            The behavior is as follows:
        
            * boolean. If True -> try parsing the index.
            * list of int or names. e.g. If [1, 2, 3] -> try parsing columns 1, 2, 3
              each as a separate date column.
            * list of lists. e.g.  If [[1, 3]] -> combine columns 1 and 3 and parse as
              a single date column.
            * dict, e.g. {'foo' : [1, 3]} -> parse columns 1, 3 as date and call
              result 'foo'
        
            If a column or index cannot be represented as an array of datetimes,
            say because of an unparsable value or a mixture of timezones, the column
            or index will be returned unaltered as an object data type. For
            non-standard datetime parsing, use ``pd.to_datetime`` after
            ``pd.read_csv``. To parse an index or column with a mixture of timezones,
            specify ``date_parser`` to be a partially-applied
            :func:`pandas.to_datetime` with ``utc=True``. See
            :ref:`io.csv.mixed_timezones` for more.
        
            Note: A fast-path exists for iso8601-formatted dates.
        infer_datetime_format : bool, default False
            If True and `parse_dates` is enabled, pandas will attempt to infer the
            format of the datetime strings in the columns, and if it can be inferred,
            switch to a faster method of parsing them. In some cases this can increase
            the parsing speed by 5-10x.
        keep_date_col : bool, default False
            If True and `parse_dates` specifies combining multiple columns then
            keep the original columns.
        date_parser : function, optional
            Function to use for converting a sequence of string columns to an array of
            datetime instances. The default uses ``dateutil.parser.parser`` to do the
            conversion. Pandas will try to call `date_parser` in three different ways,
            advancing to the next if an exception occurs: 1) Pass one or more arrays
            (as defined by `parse_dates`) as arguments; 2) concatenate (row-wise) the
            string values from the columns defined by `parse_dates` into a single array
            and pass that; and 3) call `date_parser` once for each row using one or
            more strings (corresponding to the columns defined by `parse_dates`) as
            arguments.
        dayfirst : bool, default False
            DD/MM format dates, international and European format.
        cache_dates : bool, default True
            If True, use a cache of unique, converted dates to apply the datetime
            conversion. May produce significant speed-up when parsing duplicate
            date strings, especially ones with timezone offsets.
        
            .. versionadded:: 0.25.0
        iterator : bool, default False
            Return TextFileReader object for iteration or getting chunks with
            ``get_chunk()``.
        
            .. versionchanged:: 1.2
        
               ``TextFileReader`` is a context manager.
        chunksize : int, optional
            Return TextFileReader object for iteration.
            See the `IO Tools docs
            <https://pandas.pydata.org/pandas-docs/stable/io.html#io-chunking>`_
            for more information on ``iterator`` and ``chunksize``.
        
            .. versionchanged:: 1.2
        
               ``TextFileReader`` is a context manager.
        compression : {'infer', 'gzip', 'bz2', 'zip', 'xz', None}, default 'infer'
            For on-the-fly decompression of on-disk data. If 'infer' and
            `filepath_or_buffer` is path-like, then detect compression from the
            following extensions: '.gz', '.bz2', '.zip', or '.xz' (otherwise no
            decompression). If using 'zip', the ZIP file must contain only one data
            file to be read in. Set to None for no decompression.
        thousands : str, optional
            Thousands separator.
        decimal : str, default '.'
            Character to recognize as decimal point (e.g. use ',' for European data).
        lineterminator : str (length 1), optional
            Character to break file into lines. Only valid with C parser.
        quotechar : str (length 1), optional
            The character used to denote the start and end of a quoted item. Quoted
            items can include the delimiter and it will be ignored.
        quoting : int or csv.QUOTE_* instance, default 0
            Control field quoting behavior per ``csv.QUOTE_*`` constants. Use one of
            QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3).
        doublequote : bool, default ``True``
           When quotechar is specified and quoting is not ``QUOTE_NONE``, indicate
           whether or not to interpret two consecutive quotechar elements INSIDE a
           field as a single ``quotechar`` element.
        escapechar : str (length 1), optional
            One-character string used to escape other characters.
        comment : str, optional
            Indicates remainder of line should not be parsed. If found at the beginning
            of a line, the line will be ignored altogether. This parameter must be a
            single character. Like empty lines (as long as ``skip_blank_lines=True``),
            fully commented lines are ignored by the parameter `header` but not by
            `skiprows`. For example, if ``comment='#'``, parsing
            ``#empty\na,b,c\n1,2,3`` with ``header=0`` will result in 'a,b,c' being
            treated as the header.
        encoding : str, optional
            Encoding to use for UTF when reading/writing (ex. 'utf-8'). `List of Python
            standard encodings
            <https://docs.python.org/3/library/codecs.html#standard-encodings>`_ .
        
            .. versionchanged:: 1.2
        
               When ``encoding`` is ``None``, ``errors="replace"`` is passed to
               ``open()``. Otherwise, ``errors="strict"`` is passed to ``open()``.
               This behavior was previously only the case for ``engine="python"``.
        
            .. versionchanged:: 1.3.0
        
               ``encoding_errors`` is a new argument. ``encoding`` has no longer an
               influence on how encoding errors are handled.
        
        encoding_errors : str, optional, default "strict"
            How encoding errors are treated. `List of possible values
            <https://docs.python.org/3/library/codecs.html#error-handlers>`_ .
        
            .. versionadded:: 1.3.0
        
        dialect : str or csv.Dialect, optional
            If provided, this parameter will override values (default or not) for the
            following parameters: `delimiter`, `doublequote`, `escapechar`,
            `skipinitialspace`, `quotechar`, and `quoting`. If it is necessary to
            override values, a ParserWarning will be issued. See csv.Dialect
            documentation for more details.
        error_bad_lines : bool, default ``None``
            Lines with too many fields (e.g. a csv line with too many commas) will by
            default cause an exception to be raised, and no DataFrame will be returned.
            If False, then these "bad lines" will be dropped from the DataFrame that is
            returned.
        
            .. deprecated:: 1.3.0
               The ``on_bad_lines`` parameter should be used instead to specify behavior upon
               encountering a bad line instead.
        warn_bad_lines : bool, default ``None``
            If error_bad_lines is False, and warn_bad_lines is True, a warning for each
            "bad line" will be output.
        
            .. deprecated:: 1.3.0
               The ``on_bad_lines`` parameter should be used instead to specify behavior upon
               encountering a bad line instead.
        on_bad_lines : {'error', 'warn', 'skip'}, default 'error'
            Specifies what to do upon encountering a bad line (a line with too many fields).
            Allowed values are :
        
                - 'error', raise an Exception when a bad line is encountered.
                - 'warn', raise a warning when a bad line is encountered and skip that line.
                - 'skip', skip bad lines without raising or warning when they are encountered.
        
            .. versionadded:: 1.3.0
        
        delim_whitespace : bool, default False
            Specifies whether or not whitespace (e.g. ``' '`` or ``'    '``) will be
            used as the sep. Equivalent to setting ``sep='\s+'``. If this option
            is set to True, nothing should be passed in for the ``delimiter``
            parameter.
        low_memory : bool, default True
            Internally process the file in chunks, resulting in lower memory use
            while parsing, but possibly mixed type inference.  To ensure no mixed
            types either set False, or specify the type with the `dtype` parameter.
            Note that the entire file is read into a single DataFrame regardless,
            use the `chunksize` or `iterator` parameter to return the data in chunks.
            (Only valid with C parser).
        memory_map : bool, default False
            If a filepath is provided for `filepath_or_buffer`, map the file object
            directly onto memory and access the data directly from there. Using this
            option can improve performance because there is no longer any I/O overhead.
        float_precision : str, optional
            Specifies which converter the C engine should use for floating-point
            values. The options are ``None`` or 'high' for the ordinary converter,
            'legacy' for the original lower precision pandas converter, and
            'round_trip' for the round-trip converter.
        
            .. versionchanged:: 1.2
        
        storage_options : dict, optional
            Extra options that make sense for a particular storage connection, e.g.
            host, port, username, password, etc. For HTTP(S) URLs the key-value pairs
            are forwarded to ``urllib`` as header options. For other URLs (e.g.
            starting with "s3://", and "gcs://") the key-value pairs are forwarded to
            ``fsspec``. Please see ``fsspec`` and ``urllib`` for more details.
        
            .. versionadded:: 1.2
        
        Returns
        -------
        DataFrame or TextParser
            A comma-separated values (csv) file is returned as two-dimensional
            data structure with labeled axes.
        
        See Also
        --------
        DataFrame.to_csv : Write DataFrame to a comma-separated values (csv) file.
        read_csv : Read a comma-separated values (csv) file into DataFrame.
        read_fwf : Read a table of fixed-width formatted lines into DataFrame.
        
        Examples
        --------
        >>> pd.read_csv('data.csv')  # doctest: +SKIP
    
    


```python
#built-in len() function of Python gives the number of rows in the Pandas DataFrame
len(Gauge_Discharge_data)
```




    4017




```python
#shape attribute of Pandas DataFrame prints the number of rows and columns in the Panda DataFrame
Gauge_Discharge_data.shape
```




    (4017, 5)




```python
#printing of first 10 rows of the Pandas DataFrame
Gauge_Discharge_data.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Day</th>
      <th>Data Type</th>
      <th>Mean Gauge (m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01-01-2005</td>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.473</td>
      <td>O</td>
    </tr>
    <tr>
      <th>1</th>
      <td>02-01-2005</td>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.270</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>03-01-2005</td>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.033</td>
      <td>O</td>
    </tr>
    <tr>
      <th>3</th>
      <td>04-01-2005</td>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.476</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4</th>
      <td>05-01-2005</td>
      <td>HZS</td>
      <td>3.020</td>
      <td>58.202</td>
      <td>O</td>
    </tr>
    <tr>
      <th>5</th>
      <td>06-01-2005</td>
      <td>HZS</td>
      <td>2.975</td>
      <td>52.496</td>
      <td>O</td>
    </tr>
    <tr>
      <th>6</th>
      <td>07-01-2005</td>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.435</td>
      <td>O</td>
    </tr>
    <tr>
      <th>7</th>
      <td>08-01-2005</td>
      <td>HZS</td>
      <td>2.950</td>
      <td>49.122</td>
      <td>O</td>
    </tr>
    <tr>
      <th>8</th>
      <td>09-01-2005</td>
      <td>HZS</td>
      <td>2.870</td>
      <td>37.550</td>
      <td>C</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10-01-2005</td>
      <td>HZS</td>
      <td>2.820</td>
      <td>31.271</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
</div>




```python
#printing of last 10 rows of the Pandas DataFrame
Gauge_Discharge_data.tail(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Day</th>
      <th>Data Type</th>
      <th>Mean Gauge (m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4007</th>
      <td>22-12-2015</td>
      <td>HZS</td>
      <td>3.120</td>
      <td>68.564</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4008</th>
      <td>23-12-2015</td>
      <td>HZS</td>
      <td>3.095</td>
      <td>63.098</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4009</th>
      <td>24-12-2015</td>
      <td>HHS</td>
      <td>258.060</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4010</th>
      <td>25-12-2015</td>
      <td>HHS</td>
      <td>258.060</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4011</th>
      <td>26-12-2015</td>
      <td>HZS</td>
      <td>3.055</td>
      <td>58.272</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4012</th>
      <td>27-12-2015</td>
      <td>HHS</td>
      <td>258.040</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4013</th>
      <td>28-12-2015</td>
      <td>HZS</td>
      <td>3.040</td>
      <td>55.259</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4014</th>
      <td>29-12-2015</td>
      <td>HZS</td>
      <td>3.005</td>
      <td>51.204</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4015</th>
      <td>30-12-2015</td>
      <td>HZS</td>
      <td>3.000</td>
      <td>50.639</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4016</th>
      <td>31-12-2015</td>
      <td>HZS</td>
      <td>2.905</td>
      <td>41.459</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
</div>




```python
#dtypes attribute prints the datatypes of all columns of Pandas DataFrame
data_type = Gauge_Discharge_data.dtypes
data_type
```




    Day                    object
    Data Type              object
    Mean Gauge (m)        float64
    Discharge (cumecs)    float64
    Observed/Computed      object
    dtype: object




```python
#dtypes attribute creates a Pandas Series of data types
type(data_type)
```




    pandas.core.series.Series




```python
#printing basic information about the Pandas DataFrame using info() method
Gauge_Discharge_data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4017 entries, 0 to 4016
    Data columns (total 5 columns):
     #   Column              Non-Null Count  Dtype  
    ---  ------              --------------  -----  
     0   Day                 4017 non-null   object 
     1   Data Type           4017 non-null   object 
     2   Mean Gauge (m)      4017 non-null   float64
     3   Discharge (cumecs)  3976 non-null   float64
     4   Observed/Computed   3976 non-null   object 
    dtypes: float64(2), object(3)
    memory usage: 157.0+ KB
    


```python
#printing basic statistics of the numerical data contained in the Pandas DataFrame
Gauge_Discharge_data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mean Gauge (m)</th>
      <th>Discharge (cumecs)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4017.000000</td>
      <td>3976.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.099982</td>
      <td>213.980590</td>
    </tr>
    <tr>
      <th>std</th>
      <td>25.653807</td>
      <td>321.737338</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.540000</td>
      <td>10.210000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.970000</td>
      <td>47.418750</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3.247000</td>
      <td>94.279000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.865000</td>
      <td>260.189250</td>
    </tr>
    <tr>
      <th>max</th>
      <td>259.660000</td>
      <td>3883.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#columns attribute of Pandas DataFrame
Gauge_Discharge_data.columns
```




    Index(['Day', 'Data Type', 'Mean Gauge (m)', 'Discharge (cumecs)',
           'Observed/Computed'],
          dtype='object')




```python
#columns attribute creates a new Index object
type(Gauge_Discharge_data.columns)
```




    pandas.core.indexes.base.Index




```python
#columns.values attribute prints an array of column headers
Gauge_Discharge_data.columns.values
```




    array(['Day', 'Data Type', 'Mean Gauge (m)', 'Discharge (cumecs)',
           'Observed/Computed'], dtype=object)




```python
type(Gauge_Discharge_data.columns.values)
```




    numpy.ndarray




```python
help(Gauge_Discharge_data.to_excel)
```

    Help on method to_excel in module pandas.core.generic:
    
    to_excel(excel_writer, sheet_name: 'str' = 'Sheet1', na_rep: 'str' = '', float_format: 'str | None' = None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, storage_options: 'StorageOptions' = None) -> 'None' method of pandas.core.frame.DataFrame instance
        Write object to an Excel sheet.
        
        To write a single object to an Excel .xlsx file it is only necessary to
        specify a target file name. To write to multiple sheets it is necessary to
        create an `ExcelWriter` object with a target file name, and specify a sheet
        in the file to write to.
        
        Multiple sheets may be written to by specifying unique `sheet_name`.
        With all data written to the file it is necessary to save the changes.
        Note that creating an `ExcelWriter` object with a file name that already
        exists will result in the contents of the existing file being erased.
        
        Parameters
        ----------
        excel_writer : path-like, file-like, or ExcelWriter object
            File path or existing ExcelWriter.
        sheet_name : str, default 'Sheet1'
            Name of sheet which will contain DataFrame.
        na_rep : str, default ''
            Missing data representation.
        float_format : str, optional
            Format string for floating point numbers. For example
            ``float_format="%.2f"`` will format 0.1234 to 0.12.
        columns : sequence or list of str, optional
            Columns to write.
        header : bool or list of str, default True
            Write out the column names. If a list of string is given it is
            assumed to be aliases for the column names.
        index : bool, default True
            Write row names (index).
        index_label : str or sequence, optional
            Column label for index column(s) if desired. If not specified, and
            `header` and `index` are True, then the index names are used. A
            sequence should be given if the DataFrame uses MultiIndex.
        startrow : int, default 0
            Upper left cell row to dump data frame.
        startcol : int, default 0
            Upper left cell column to dump data frame.
        engine : str, optional
            Write engine to use, 'openpyxl' or 'xlsxwriter'. You can also set this
            via the options ``io.excel.xlsx.writer``, ``io.excel.xls.writer``, and
            ``io.excel.xlsm.writer``.
        
            .. deprecated:: 1.2.0
        
                As the `xlwt <https://pypi.org/project/xlwt/>`__ package is no longer
                maintained, the ``xlwt`` engine will be removed in a future version
                of pandas.
        
        merge_cells : bool, default True
            Write MultiIndex and Hierarchical Rows as merged cells.
        encoding : str, optional
            Encoding of the resulting excel file. Only necessary for xlwt,
            other writers support unicode natively.
        inf_rep : str, default 'inf'
            Representation for infinity (there is no native representation for
            infinity in Excel).
        verbose : bool, default True
            Display more information in the error logs.
        freeze_panes : tuple of int (length 2), optional
            Specifies the one-based bottommost row and rightmost column that
            is to be frozen.
        storage_options : dict, optional
            Extra options that make sense for a particular storage connection, e.g.
            host, port, username, password, etc. For HTTP(S) URLs the key-value pairs
            are forwarded to ``urllib`` as header options. For other URLs (e.g.
            starting with "s3://", and "gcs://") the key-value pairs are forwarded to
            ``fsspec``. Please see ``fsspec`` and ``urllib`` for more details.
        
            .. versionadded:: 1.2.0
        
        See Also
        --------
        to_csv : Write DataFrame to a comma-separated values (csv) file.
        ExcelWriter : Class for writing DataFrame objects into excel sheets.
        read_excel : Read an Excel file into a pandas DataFrame.
        read_csv : Read a comma-separated values (csv) file into DataFrame.
        
        Notes
        -----
        For compatibility with :meth:`~DataFrame.to_csv`,
        to_excel serializes lists and dicts to strings before writing.
        
        Once a workbook has been saved it is not possible to write further
        data without rewriting the whole workbook.
        
        Examples
        --------
        
        Create, write to and save a workbook:
        
        >>> df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
        ...                    index=['row 1', 'row 2'],
        ...                    columns=['col 1', 'col 2'])
        >>> df1.to_excel("output.xlsx")  # doctest: +SKIP
        
        To specify the sheet name:
        
        >>> df1.to_excel("output.xlsx",
        ...              sheet_name='Sheet_name_1')  # doctest: +SKIP
        
        If you wish to write to more than one sheet in the workbook, it is
        necessary to specify an ExcelWriter object:
        
        >>> df2 = df1.copy()
        >>> with pd.ExcelWriter('output.xlsx') as writer:  # doctest: +SKIP
        ...     df1.to_excel(writer, sheet_name='Sheet_name_1')
        ...     df2.to_excel(writer, sheet_name='Sheet_name_2')
        
        ExcelWriter can also be used to append to an existing Excel file:
        
        >>> with pd.ExcelWriter('output.xlsx',
        ...                     mode='a') as writer:  # doctest: +SKIP
        ...     df.to_excel(writer, sheet_name='Sheet_name_3')
        
        To set the library that is used to write the Excel file,
        you can pass the `engine` keyword (the default engine is
        automatically chosen depending on the file extension):
        
        >>> df1.to_excel('output1.xlsx', engine='xlsxwriter')  # doctest: +SKIP
    
    


```python
#writing data from Pandas DataFrame into excel file use to_*() method
# writing to excel file doesn't happen due to unavailability of openpyxl module
Gauge_Discharge_data.to_excel('GD_data.xlsx')
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_1940/1217027935.py in <module>
    ----> 1 Gauge_Discharge_data.to_excel('GD_data.xlsx')
    

    ~\anaconda3\envs\python-wrm\lib\site-packages\pandas\core\generic.py in to_excel(self, excel_writer, sheet_name, na_rep, float_format, columns, header, index, index_label, startrow, startcol, engine, merge_cells, encoding, inf_rep, verbose, freeze_panes, storage_options)
       2282             inf_rep=inf_rep,
       2283         )
    -> 2284         formatter.write(
       2285             excel_writer,
       2286             sheet_name=sheet_name,
    

    ~\anaconda3\envs\python-wrm\lib\site-packages\pandas\io\formats\excel.py in write(self, writer, sheet_name, startrow, startcol, freeze_panes, engine, storage_options)
        832             # error: Cannot instantiate abstract class 'ExcelWriter' with abstract
        833             # attributes 'engine', 'save', 'supported_extensions' and 'write_cells'
    --> 834             writer = ExcelWriter(  # type: ignore[abstract]
        835                 writer, engine=engine, storage_options=storage_options
        836             )
    

    ~\anaconda3\envs\python-wrm\lib\site-packages\pandas\io\excel\_openpyxl.py in __init__(self, path, engine, date_format, datetime_format, mode, storage_options, if_sheet_exists, engine_kwargs, **kwargs)
         46     ):
         47         # Use the openpyxl module as the Excel writer.
    ---> 48         from openpyxl.workbook import Workbook
         49 
         50         engine_kwargs = combine_kwargs(engine_kwargs, kwargs)
    

    ModuleNotFoundError: No module named 'openpyxl'



```python
#openpyxl module has to be installed in python-wrm environment first using conda installer/navigator
import openpyxl
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_1940/1020030620.py in <module>
    ----> 1 import openpyxl
    

    ModuleNotFoundError: No module named 'openpyxl'



```python
import openpyxl
```


```python
#setting index parameter to false removes the row indices in the excel file generated
Gauge_Discharge_data.to_excel('GD_data.xlsx',index = False)
```


```python

```


<iframe width="560" height="315" src="https://www.youtube.com/embed/URDTyIrD5Pg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Lecture Visualization

<embed src="pdfs/Session7_Working_with_Pandas_1.pdf" type="application/pdf" width="100%" height="600px" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />

<p align="center"><a href="pdfs/Session7_Working_with_Pandas_1.pdf" class="md-button md-button--primary">Download Lecture Slides</a></p>

??? info "View Full Lecture Transcript"
    The following content is extracted from the lecture slides.

    Working with Pandas

    -

    I

    Chaitanya K S

    Deputy Director

    National Water Academy

    Central Water Commission, Pune

    Why Pandas?

    • Pandas is a fast, powerful, flexible and easy to use open-source

    data analysis and manipulation tool, built on top of the Python

    programming language. https://pandas.pydata.org/

    • Makes working with ‘relational’ or ‘labeled’ data both easy and

    intuitive

    • Two primary data structures - Series(1-D) and DataFrame(2-D) .

    Each Column in a DataFrame is a Series

    Why Pandas? (contd.)

    • Easy handling of missing data

    • Size mutability: columns can be inserted and deleted

    • Automatic and explicit data alignment

    • group by functionality for aggregating and transforming data

    • Differently indexed data in other Python data structures can be

    easily converted into DataFrame objects

    • Intelligent label-based slicing, fancy indexing, and subsetting of

    large data sets

    • Intuitive merging and joining data sets

    • Flexible reshaping and pivoting of data sets

    • Hierarchical labelling of axes

    • Robust IO tools for loading data from various formats

    • Time series-specific functionality

    For data scientists, working with data is typically divided into multiple stages: munging and

    cleaning data, analyzing / modeling it, then organizing the results of the analysis into a form

    suitable for plotting or tabular display. pandas is the ideal tool for all of these tasks.

    https://pandas.pydata.org/docs/getting_started/overview.html

    Thank you



<iframe width="560" height="315" src="https://www.youtube.com/embed/URDTyIrD5Pg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Lecture Visualization

<embed src="pdfs/Session7_Working_with_Pandas_1.pdf" type="application/pdf" width="100%" height="600px" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />

<p align="center"><a href="pdfs/Session7_Working_with_Pandas_1.pdf" class="md-button md-button--primary">Download Lecture Slides</a></p>

??? info "View Full Lecture Transcript"
    The following content is extracted from the lecture slides.

    Working with Pandas

    -

    I

    Chaitanya K S

    Deputy Director

    National Water Academy

    Central Water Commission, Pune

    Why Pandas?

    • Pandas is a fast, powerful, flexible and easy to use open-source

    data analysis and manipulation tool, built on top of the Python

    programming language. https://pandas.pydata.org/

    • Makes working with ‘relational’ or ‘labeled’ data both easy and

    intuitive

    • Two primary data structures - Series(1-D) and DataFrame(2-D) .

    Each Column in a DataFrame is a Series

    Why Pandas? (contd.)

    • Easy handling of missing data

    • Size mutability: columns can be inserted and deleted

    • Automatic and explicit data alignment

    • group by functionality for aggregating and transforming data

    • Differently indexed data in other Python data structures can be

    easily converted into DataFrame objects

    • Intelligent label-based slicing, fancy indexing, and subsetting of

    large data sets

    • Intuitive merging and joining data sets

    • Flexible reshaping and pivoting of data sets

    • Hierarchical labelling of axes

    • Robust IO tools for loading data from various formats

    • Time series-specific functionality

    For data scientists, working with data is typically divided into multiple stages: munging and

    cleaning data, analyzing / modeling it, then organizing the results of the analysis into a form

    suitable for plotting or tabular display. pandas is the ideal tool for all of these tasks.

    https://pandas.pydata.org/docs/getting_started/overview.html

    Thank you

