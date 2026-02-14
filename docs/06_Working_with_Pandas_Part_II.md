```python
#import of modules 
import pathlib
import os
import pandas as pd
```


```python
#Defining filepaths to data files
fp_GD_data = pathlib.Path.home() / "PythonWRM" / "Data" /'Gauge_Discharge_data.csv'
fp_rainfall_data = pathlib.Path.home() / "PythonWRM" / "Data" / 'imd_district-wise_rainfalldata_2004-2010.xls'
fp_Dams_data = pathlib.Path.home() / "PythonWRM" / "Data" / 'Maharashtra_Dams_NRLD.csv'
fp_Reservoir_data = pathlib.Path.home() / "PythonWRM" / "Data" / 'Reservoir_Level_Storage.xlsx'

```


```python
#Creation of Pandas DataFrame by reading data from a csv file
df_GD = pd.read_csv(fp_GD_data)
```


```python
df_GD
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
#Renaming of DataFrame columns using rename() method
df_GD = df_GD.rename(columns={'Data Type': 'Datatype', 'Mean Gauge (m)':'Gauge(m)'})
```


```python
#selection of a column of a Pandas DataFrame
pdSeries1=df_GD["Gauge(m)"]
pdSeries1
```




    0         2.990
    1         2.990
    2         2.990
    3         3.000
    4         3.020
             ...   
    4012    258.040
    4013      3.040
    4014      3.005
    4015      3.000
    4016      2.905
    Name: Gauge(m), Length: 4017, dtype: float64




```python
#Any column of a Pandas DataFrame is a Pandas Series
type(pdSeries1)
```




    pandas.core.series.Series




```python
#Creation of Pandas Series from a list
pdSeries2=pd.Series([1,2,3,4])
pdSeries2
```




    0    1
    1    2
    2    3
    3    4
    dtype: int64




```python
#Creation of Pandas Series with customized index
pdSeries3=pd.Series([1,2,3,4], index = ['a','b','c','d'])
pdSeries3

```




    a    1
    b    2
    c    3
    d    4
    dtype: int64




```python
#Resetting the indices to default integer indices using reset_index() method
pdSeries3 = pdSeries3.reset_index(drop=True)
pdSeries3
```




    0    1
    1    2
    2    3
    3    4
    dtype: int64




```python
#Selection of multiple columns of a DataFrame
df_GD[['Gauge(m)','Discharge (cumecs)']]
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
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.990</td>
      <td>54.473</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.990</td>
      <td>54.270</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.990</td>
      <td>54.033</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.000</td>
      <td>55.476</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.020</td>
      <td>58.202</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4012</th>
      <td>258.040</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4013</th>
      <td>3.040</td>
      <td>55.259</td>
    </tr>
    <tr>
      <th>4014</th>
      <td>3.005</td>
      <td>51.204</td>
    </tr>
    <tr>
      <th>4015</th>
      <td>3.000</td>
      <td>50.639</td>
    </tr>
    <tr>
      <th>4016</th>
      <td>2.905</td>
      <td>41.459</td>
    </tr>
  </tbody>
</table>
<p>4017 rows × 2 columns</p>
</div>




```python
#Selection of multiple columns of a DataFrame creates another Dataframe
type(df_GD[['Gauge(m)','Discharge (cumecs)']])
```




    pandas.core.frame.DataFrame




```python
#selection of specific rows/columns using .loc operator
#.loc operator goes along with row/column labels
df_GD.loc[0]
```




    Day                   01-01-2005
    Datatype                     HZS
    Gauge(m)                    2.99
    Discharge (cumecs)        54.473
    Observed/Computed              O
    Name: 0, dtype: object




```python
type(df_GD.loc[0])
```




    pandas.core.series.Series




```python
df_GD.loc[0:2]
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01-01-2005</td>
      <td>HZS</td>
      <td>2.99</td>
      <td>54.473</td>
      <td>O</td>
    </tr>
    <tr>
      <th>1</th>
      <td>02-01-2005</td>
      <td>HZS</td>
      <td>2.99</td>
      <td>54.270</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>03-01-2005</td>
      <td>HZS</td>
      <td>2.99</td>
      <td>54.033</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(df_GD.loc[0:2])
```




    pandas.core.frame.DataFrame




```python
df_GD.loc[0:2,'Gauge(m)':'Discharge (cumecs)']
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
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.99</td>
      <td>54.473</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.99</td>
      <td>54.270</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.99</td>
      <td>54.033</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_GD.loc[:,"Gauge(m)"]
```




    0         2.990
    1         2.990
    2         2.990
    3         3.000
    4         3.020
             ...   
    4012    258.040
    4013      3.040
    4014      3.005
    4015      3.000
    4016      2.905
    Name: Gauge(m), Length: 4017, dtype: float64




```python
type(df_GD.loc[:,"Gauge(m)"])
```




    pandas.core.series.Series




```python
df_GD.loc[:,'Datatype':]
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.473</td>
      <td>O</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.270</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.033</td>
      <td>O</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.476</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4</th>
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
    </tr>
    <tr>
      <th>4012</th>
      <td>HHS</td>
      <td>258.040</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4013</th>
      <td>HZS</td>
      <td>3.040</td>
      <td>55.259</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4014</th>
      <td>HZS</td>
      <td>3.005</td>
      <td>51.204</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4015</th>
      <td>HZS</td>
      <td>3.000</td>
      <td>50.639</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4016</th>
      <td>HZS</td>
      <td>2.905</td>
      <td>41.459</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
<p>4017 rows × 4 columns</p>
</div>




```python
df_GD.loc[:50,:'Discharge (cumecs)']
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01-01-2005</td>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.473</td>
    </tr>
    <tr>
      <th>1</th>
      <td>02-01-2005</td>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.270</td>
    </tr>
    <tr>
      <th>2</th>
      <td>03-01-2005</td>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.033</td>
    </tr>
    <tr>
      <th>3</th>
      <td>04-01-2005</td>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.476</td>
    </tr>
    <tr>
      <th>4</th>
      <td>05-01-2005</td>
      <td>HZS</td>
      <td>3.020</td>
      <td>58.202</td>
    </tr>
    <tr>
      <th>5</th>
      <td>06-01-2005</td>
      <td>HZS</td>
      <td>2.975</td>
      <td>52.496</td>
    </tr>
    <tr>
      <th>6</th>
      <td>07-01-2005</td>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.435</td>
    </tr>
    <tr>
      <th>7</th>
      <td>08-01-2005</td>
      <td>HZS</td>
      <td>2.950</td>
      <td>49.122</td>
    </tr>
    <tr>
      <th>8</th>
      <td>09-01-2005</td>
      <td>HZS</td>
      <td>2.870</td>
      <td>37.550</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10-01-2005</td>
      <td>HZS</td>
      <td>2.820</td>
      <td>31.271</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11-01-2005</td>
      <td>HZS</td>
      <td>2.850</td>
      <td>34.691</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12-01-2005</td>
      <td>HZS</td>
      <td>2.830</td>
      <td>32.516</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13-01-2005</td>
      <td>HZS</td>
      <td>2.920</td>
      <td>45.137</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14-01-2005</td>
      <td>HZS</td>
      <td>2.920</td>
      <td>44.140</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15-01-2005</td>
      <td>HZS</td>
      <td>2.940</td>
      <td>45.742</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16-01-2005</td>
      <td>HZS</td>
      <td>2.870</td>
      <td>37.550</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17-01-2005</td>
      <td>HZS</td>
      <td>2.810</td>
      <td>30.830</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18-01-2005</td>
      <td>HZS</td>
      <td>2.870</td>
      <td>37.723</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19-01-2005</td>
      <td>HZS</td>
      <td>2.890</td>
      <td>40.268</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20-01-2005</td>
      <td>HZS</td>
      <td>2.900</td>
      <td>40.728</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21-01-2005</td>
      <td>HZS</td>
      <td>2.950</td>
      <td>48.350</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22-01-2005</td>
      <td>HZS</td>
      <td>2.920</td>
      <td>45.185</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23-01-2005</td>
      <td>HZS</td>
      <td>2.950</td>
      <td>48.350</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24-01-2005</td>
      <td>HZS</td>
      <td>2.920</td>
      <td>45.154</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25-01-2005</td>
      <td>HZS</td>
      <td>2.850</td>
      <td>34.760</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26-01-2005</td>
      <td>HZS</td>
      <td>2.810</td>
      <td>30.370</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27-01-2005</td>
      <td>HZS</td>
      <td>2.850</td>
      <td>34.799</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28-01-2005</td>
      <td>HZS</td>
      <td>2.830</td>
      <td>31.845</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29-01-2005</td>
      <td>HZS</td>
      <td>2.860</td>
      <td>35.480</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30-01-2005</td>
      <td>HZS</td>
      <td>2.800</td>
      <td>29.250</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31-01-2005</td>
      <td>HZS</td>
      <td>2.795</td>
      <td>29.203</td>
    </tr>
    <tr>
      <th>31</th>
      <td>01-02-2005</td>
      <td>HZS</td>
      <td>2.800</td>
      <td>29.229</td>
    </tr>
    <tr>
      <th>32</th>
      <td>02-02-2005</td>
      <td>HZS</td>
      <td>2.820</td>
      <td>30.082</td>
    </tr>
    <tr>
      <th>33</th>
      <td>03-02-2005</td>
      <td>HZS</td>
      <td>2.940</td>
      <td>45.648</td>
    </tr>
    <tr>
      <th>34</th>
      <td>04-02-2005</td>
      <td>HZS</td>
      <td>3.010</td>
      <td>57.621</td>
    </tr>
    <tr>
      <th>35</th>
      <td>05-02-2005</td>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.793</td>
    </tr>
    <tr>
      <th>36</th>
      <td>06-02-2005</td>
      <td>HZS</td>
      <td>2.940</td>
      <td>46.920</td>
    </tr>
    <tr>
      <th>37</th>
      <td>07-02-2005</td>
      <td>HZS</td>
      <td>2.920</td>
      <td>45.136</td>
    </tr>
    <tr>
      <th>38</th>
      <td>08-02-2005</td>
      <td>HZS</td>
      <td>2.875</td>
      <td>39.145</td>
    </tr>
    <tr>
      <th>39</th>
      <td>09-02-2005</td>
      <td>HZS</td>
      <td>2.900</td>
      <td>42.837</td>
    </tr>
    <tr>
      <th>40</th>
      <td>10-02-2005</td>
      <td>HZS</td>
      <td>2.880</td>
      <td>40.439</td>
    </tr>
    <tr>
      <th>41</th>
      <td>11-02-2005</td>
      <td>HZS</td>
      <td>2.820</td>
      <td>30.292</td>
    </tr>
    <tr>
      <th>42</th>
      <td>12-02-2005</td>
      <td>HZS</td>
      <td>2.850</td>
      <td>34.722</td>
    </tr>
    <tr>
      <th>43</th>
      <td>13-02-2005</td>
      <td>HZS</td>
      <td>2.860</td>
      <td>36.300</td>
    </tr>
    <tr>
      <th>44</th>
      <td>14-02-2005</td>
      <td>HZS</td>
      <td>2.780</td>
      <td>27.279</td>
    </tr>
    <tr>
      <th>45</th>
      <td>15-02-2005</td>
      <td>HZS</td>
      <td>2.790</td>
      <td>29.522</td>
    </tr>
    <tr>
      <th>46</th>
      <td>16-02-2005</td>
      <td>HZS</td>
      <td>2.775</td>
      <td>25.450</td>
    </tr>
    <tr>
      <th>47</th>
      <td>17-02-2005</td>
      <td>HZS</td>
      <td>2.840</td>
      <td>35.050</td>
    </tr>
    <tr>
      <th>48</th>
      <td>18-02-2005</td>
      <td>HZS</td>
      <td>2.800</td>
      <td>29.332</td>
    </tr>
    <tr>
      <th>49</th>
      <td>19-02-2005</td>
      <td>HZS</td>
      <td>2.810</td>
      <td>30.567</td>
    </tr>
    <tr>
      <th>50</th>
      <td>20-02-2005</td>
      <td>HZS</td>
      <td>2.750</td>
      <td>23.960</td>
    </tr>
  </tbody>
</table>
</div>




```python
#selection of specific rows/columns using .iloc operator
df_GD.iloc[0:4,0:3]
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01-01-2005</td>
      <td>HZS</td>
      <td>2.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>02-01-2005</td>
      <td>HZS</td>
      <td>2.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>03-01-2005</td>
      <td>HZS</td>
      <td>2.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>04-01-2005</td>
      <td>HZS</td>
      <td>3.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_GD.iloc[[0,1,2,3,4],:]
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01-01-2005</td>
      <td>HZS</td>
      <td>2.99</td>
      <td>54.473</td>
      <td>O</td>
    </tr>
    <tr>
      <th>1</th>
      <td>02-01-2005</td>
      <td>HZS</td>
      <td>2.99</td>
      <td>54.270</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>03-01-2005</td>
      <td>HZS</td>
      <td>2.99</td>
      <td>54.033</td>
      <td>O</td>
    </tr>
    <tr>
      <th>3</th>
      <td>04-01-2005</td>
      <td>HZS</td>
      <td>3.00</td>
      <td>55.476</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4</th>
      <td>05-01-2005</td>
      <td>HZS</td>
      <td>3.02</td>
      <td>58.202</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_GD.iloc[[0,365],:]
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
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
      <th>365</th>
      <td>01-01-2006</td>
      <td>HZS</td>
      <td>3.425</td>
      <td>141.900</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_GD.loc[[0,365],:]
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
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
      <th>365</th>
      <td>01-01-2006</td>
      <td>HZS</td>
      <td>3.425</td>
      <td>141.900</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>




```python
#selection of last row of the DataFrame
df_GD.iloc[-1]
```




    Day                   31-12-2015
    Datatype                     HZS
    Gauge(m)                   2.905
    Discharge (cumecs)        41.459
    Observed/Computed              O
    Name: 4016, dtype: object




```python
#selection of specific element of DataFrame using at() method by specifying the row and column labels
df_GD.at[4012,"Gauge(m)"]
```




    258.04




```python
#dropping of columns along axis 1 with drop() method
df_GD.drop(['Datatype','Observed/Computed'
],axis=1)
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
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01-01-2005</td>
      <td>2.990</td>
      <td>54.473</td>
    </tr>
    <tr>
      <th>1</th>
      <td>02-01-2005</td>
      <td>2.990</td>
      <td>54.270</td>
    </tr>
    <tr>
      <th>2</th>
      <td>03-01-2005</td>
      <td>2.990</td>
      <td>54.033</td>
    </tr>
    <tr>
      <th>3</th>
      <td>04-01-2005</td>
      <td>3.000</td>
      <td>55.476</td>
    </tr>
    <tr>
      <th>4</th>
      <td>05-01-2005</td>
      <td>3.020</td>
      <td>58.202</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4012</th>
      <td>27-12-2015</td>
      <td>258.040</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4013</th>
      <td>28-12-2015</td>
      <td>3.040</td>
      <td>55.259</td>
    </tr>
    <tr>
      <th>4014</th>
      <td>29-12-2015</td>
      <td>3.005</td>
      <td>51.204</td>
    </tr>
    <tr>
      <th>4015</th>
      <td>30-12-2015</td>
      <td>3.000</td>
      <td>50.639</td>
    </tr>
    <tr>
      <th>4016</th>
      <td>31-12-2015</td>
      <td>2.905</td>
      <td>41.459</td>
    </tr>
  </tbody>
</table>
<p>4017 rows × 3 columns</p>
</div>




```python
#dropping of a row along axis 0 with drop() method
df_GD.drop([4016
],axis=0)
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
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
  </tbody>
</table>
<p>4016 rows × 5 columns</p>
</div>




```python
#Selection of rows based on conditional expression
#Operation of conditional expression on any single column creates a Pandas Series of boolean datatype
df_GD["Discharge (cumecs)"]>100
```




    0       False
    1       False
    2       False
    3       False
    4       False
            ...  
    4012    False
    4013    False
    4014    False
    4015    False
    4016    False
    Name: Discharge (cumecs), Length: 4017, dtype: bool




```python
type(df_GD["Discharge (cumecs)"]>100)
```




    pandas.core.series.Series




```python
#only those rows returning True in the above Boolean datatype series are part of the selection
df_GD[df_GD["Discharge (cumecs)"]>100]
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>97</th>
      <td>08-04-2005</td>
      <td>HZS</td>
      <td>3.300</td>
      <td>112.100</td>
      <td>C</td>
    </tr>
    <tr>
      <th>155</th>
      <td>05-06-2005</td>
      <td>HZS</td>
      <td>3.240</td>
      <td>109.300</td>
      <td>C</td>
    </tr>
    <tr>
      <th>187</th>
      <td>07-07-2005</td>
      <td>HZS</td>
      <td>3.280</td>
      <td>108.077</td>
      <td>O</td>
    </tr>
    <tr>
      <th>188</th>
      <td>08-07-2005</td>
      <td>HZS</td>
      <td>4.425</td>
      <td>484.813</td>
      <td>O</td>
    </tr>
    <tr>
      <th>189</th>
      <td>09-07-2005</td>
      <td>HZS</td>
      <td>4.345</td>
      <td>450.334</td>
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
      <th>3988</th>
      <td>03-12-2015</td>
      <td>HZS</td>
      <td>3.705</td>
      <td>238.708</td>
      <td>O</td>
    </tr>
    <tr>
      <th>3989</th>
      <td>04-12-2015</td>
      <td>HZS</td>
      <td>3.735</td>
      <td>242.218</td>
      <td>O</td>
    </tr>
    <tr>
      <th>3990</th>
      <td>05-12-2015</td>
      <td>HZS</td>
      <td>3.560</td>
      <td>173.310</td>
      <td>O</td>
    </tr>
    <tr>
      <th>3992</th>
      <td>07-12-2015</td>
      <td>HZS</td>
      <td>3.390</td>
      <td>129.035</td>
      <td>O</td>
    </tr>
    <tr>
      <th>3993</th>
      <td>08-12-2015</td>
      <td>HZS</td>
      <td>3.225</td>
      <td>106.866</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
<p>1927 rows × 5 columns</p>
</div>




```python
discharge_above_100cumecs = df_GD[df_GD["Discharge (cumecs)"]>100]
```


```python
#indices of rows selected based on conditional expression can be reset with reset_index() method
discharge_above_100cumecs.reset_index(drop=True)
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>08-04-2005</td>
      <td>HZS</td>
      <td>3.300</td>
      <td>112.100</td>
      <td>C</td>
    </tr>
    <tr>
      <th>1</th>
      <td>05-06-2005</td>
      <td>HZS</td>
      <td>3.240</td>
      <td>109.300</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>07-07-2005</td>
      <td>HZS</td>
      <td>3.280</td>
      <td>108.077</td>
      <td>O</td>
    </tr>
    <tr>
      <th>3</th>
      <td>08-07-2005</td>
      <td>HZS</td>
      <td>4.425</td>
      <td>484.813</td>
      <td>O</td>
    </tr>
    <tr>
      <th>4</th>
      <td>09-07-2005</td>
      <td>HZS</td>
      <td>4.345</td>
      <td>450.334</td>
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
      <th>1922</th>
      <td>03-12-2015</td>
      <td>HZS</td>
      <td>3.705</td>
      <td>238.708</td>
      <td>O</td>
    </tr>
    <tr>
      <th>1923</th>
      <td>04-12-2015</td>
      <td>HZS</td>
      <td>3.735</td>
      <td>242.218</td>
      <td>O</td>
    </tr>
    <tr>
      <th>1924</th>
      <td>05-12-2015</td>
      <td>HZS</td>
      <td>3.560</td>
      <td>173.310</td>
      <td>O</td>
    </tr>
    <tr>
      <th>1925</th>
      <td>07-12-2015</td>
      <td>HZS</td>
      <td>3.390</td>
      <td>129.035</td>
      <td>O</td>
    </tr>
    <tr>
      <th>1926</th>
      <td>08-12-2015</td>
      <td>HZS</td>
      <td>3.225</td>
      <td>106.866</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
<p>1927 rows × 5 columns</p>
</div>




```python
#creation of Pandas DataFrame by reading data from a csv file
df_Dams = pd.read_csv(fp_Dams_data)
```


```python
df_Dams
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
      <th>Sr.No\tPIC\tName of Dam\tLatitude\tLongitude\tYear of Completion\tRiver Basin\tRiver\tNeareast City\tSeismic Zone\tDam Type\tHeight above Lowest Foundation Level\tDam Length\tVolume Content of Dam\tGross Storage Capacity\tReservoir Area\tEffective Storage Capacity\tPurpose\tDesigned Spillway Capacity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100\tMH09VH0100\tKOYNA\t17.40194444\t73.752222...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>590\tMH09HH0597\tJAYAKWADI\t19.48575\t75.36888...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>833\tMH09HH0843\tUJJANI\t18.07472222\t75.12111...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1216\tMH09HH1229\tTOTLADOH\t21.65888889\t79.23...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>936\tMH09HH0947\tISAPUR\t19.7175\t77.42555556\...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2382</th>
      <td>2378\tMH09HH2416\tKalgaon\t17.3175\t73.8916666...</td>
    </tr>
    <tr>
      <th>2383</th>
      <td>2379\tMH09MH2417\tKinkhed\t20.40833333\t77.504...</td>
    </tr>
    <tr>
      <th>2384</th>
      <td>2380\tMH09MH2418\tDahegaon\t20.19194444\t78.70...</td>
    </tr>
    <tr>
      <th>2385</th>
      <td>2383\tMH09MH2421\tGunjarga K T Weir\t18.05\t76...</td>
    </tr>
    <tr>
      <th>2386</th>
      <td>2388\tMH09MH2426\tJalkot St\t17.78333333\t76.1...</td>
    </tr>
  </tbody>
</table>
<p>2387 rows × 1 columns</p>
</div>




```python
#passing of sep parameter '\t' as the csv file is tab seperated file
df_Dams = pd.read_csv(fp_Dams_data, sep='\t')
```


```python
df_Dams
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
      <th>Sr.No</th>
      <th>PIC</th>
      <th>Name of Dam</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Year of Completion</th>
      <th>River Basin</th>
      <th>River</th>
      <th>Neareast City</th>
      <th>Seismic Zone</th>
      <th>Dam Type</th>
      <th>Height above Lowest Foundation Level</th>
      <th>Dam Length</th>
      <th>Volume Content of Dam</th>
      <th>Gross Storage Capacity</th>
      <th>Reservoir Area</th>
      <th>Effective Storage Capacity</th>
      <th>Purpose</th>
      <th>Designed Spillway Capacity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>MH09VH0100</td>
      <td>KOYNA</td>
      <td>17.401944</td>
      <td>73.752222</td>
      <td>1964.0</td>
      <td>Krishna</td>
      <td>Koyna.</td>
      <td>Patan.</td>
      <td>IV</td>
      <td>Composite_Concrete_and_Masonry</td>
      <td>103.02</td>
      <td>807.72</td>
      <td>1.555000e+06</td>
      <td>2.980680e+09</td>
      <td>1.196881e+08</td>
      <td>2.835540e+09</td>
      <td>I/H</td>
      <td>5082.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>590</td>
      <td>MH09HH0597</td>
      <td>JAYAKWADI</td>
      <td>19.485750</td>
      <td>75.368889</td>
      <td>1976.0</td>
      <td>Godavari</td>
      <td>Godavari.</td>
      <td>Paithan</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>41.30</td>
      <td>10415.00</td>
      <td>1.341000e+07</td>
      <td>2.909000e+09</td>
      <td>3.500000e+09</td>
      <td>2.170930e+09</td>
      <td>I/H</td>
      <td>18153.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>833</td>
      <td>MH09HH0843</td>
      <td>UJJANI</td>
      <td>18.074722</td>
      <td>75.121111</td>
      <td>1980.0</td>
      <td>Krishna</td>
      <td>Bhima</td>
      <td>Madha.</td>
      <td>III</td>
      <td>Other</td>
      <td>56.40</td>
      <td>3141.40</td>
      <td>3.320000e+06</td>
      <td>3.320010e+09</td>
      <td>2.900000e+08</td>
      <td>1.517200e+09</td>
      <td>I/S</td>
      <td>18010.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1216</td>
      <td>MH09HH1229</td>
      <td>TOTLADOH</td>
      <td>21.658889</td>
      <td>79.231944</td>
      <td>1989.0</td>
      <td>Godavari</td>
      <td>Pench</td>
      <td>Ramtek</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>74.50</td>
      <td>3061.00</td>
      <td>9.720000e+05</td>
      <td>1.166930e+09</td>
      <td>7.771000e+07</td>
      <td>1.016930e+09</td>
      <td>H</td>
      <td>12072.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>936</td>
      <td>MH09HH0947</td>
      <td>ISAPUR</td>
      <td>19.717500</td>
      <td>77.425556</td>
      <td>1982.0</td>
      <td>Godavari</td>
      <td>Penganga</td>
      <td>Pusad</td>
      <td>II</td>
      <td>Other</td>
      <td>48.00</td>
      <td>4088.50</td>
      <td>1.170000e+05</td>
      <td>1.279000e+09</td>
      <td>9.627000e+07</td>
      <td>9.640000e+08</td>
      <td>I</td>
      <td>10480.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2382</th>
      <td>2378</td>
      <td>MH09HH2416</td>
      <td>Kalgaon</td>
      <td>17.317500</td>
      <td>73.891667</td>
      <td>NaN</td>
      <td>Krishna</td>
      <td>Local Nala</td>
      <td>Karad</td>
      <td>IV</td>
      <td>Earthfill_Embankment</td>
      <td>32.26</td>
      <td>383.50</td>
      <td>6.197440e+02</td>
      <td>2.563000e+00</td>
      <td>2.118500e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>199.64</td>
    </tr>
    <tr>
      <th>2383</th>
      <td>2379</td>
      <td>MH09MH2417</td>
      <td>Kinkhed</td>
      <td>20.408333</td>
      <td>77.504167</td>
      <td>2016.0</td>
      <td>Area of Inland Drainage in Rajasthan</td>
      <td>Ghataprabha</td>
      <td>Karanja</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>17.74</td>
      <td>420.00</td>
      <td>NaN</td>
      <td>2.328000e+03</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>I</td>
      <td>248.00</td>
    </tr>
    <tr>
      <th>2384</th>
      <td>2380</td>
      <td>MH09MH2418</td>
      <td>Dahegaon</td>
      <td>20.191944</td>
      <td>78.701389</td>
      <td>2016.0</td>
      <td>Godavari</td>
      <td>Local Nalla</td>
      <td>Ralegaon</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>17.35</td>
      <td>1235.00</td>
      <td>NaN</td>
      <td>3.390000e+03</td>
      <td>8.030000e+08</td>
      <td>NaN</td>
      <td>I</td>
      <td>406.41</td>
    </tr>
    <tr>
      <th>2385</th>
      <td>2383</td>
      <td>MH09MH2421</td>
      <td>Gunjarga K T Weir</td>
      <td>18.050000</td>
      <td>76.819444</td>
      <td>2016.0</td>
      <td>Godavari</td>
      <td>Terna</td>
      <td>Nilanga</td>
      <td>III</td>
      <td>Earthfill_Embankment</td>
      <td>19.95</td>
      <td>101.00</td>
      <td>8.440000e+00</td>
      <td>1.368000e+03</td>
      <td>7.724000e+07</td>
      <td>NaN</td>
      <td>I</td>
      <td>4713.14</td>
    </tr>
    <tr>
      <th>2386</th>
      <td>2388</td>
      <td>MH09MH2426</td>
      <td>Jalkot St</td>
      <td>17.783333</td>
      <td>76.166667</td>
      <td>1999.0</td>
      <td>Godavari</td>
      <td>Local Nalla</td>
      <td>Tuljapur</td>
      <td>III</td>
      <td>Earthfill_Embankment</td>
      <td>15.30</td>
      <td>915.00</td>
      <td>NaN</td>
      <td>1.850000e+03</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>I</td>
      <td>416.55</td>
    </tr>
  </tbody>
</table>
<p>2387 rows × 19 columns</p>
</div>




```python
#renaming of selected columns of DataFrame with rename() method
df_Dams = df_Dams.rename(columns={'Height above Lowest Foundation Level': 'Height(m)', 'Gross Storage Capacity':'Capacity(m3)'})
```


```python
df_Dams
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
      <th>Sr.No</th>
      <th>PIC</th>
      <th>Name of Dam</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Year of Completion</th>
      <th>River Basin</th>
      <th>River</th>
      <th>Neareast City</th>
      <th>Seismic Zone</th>
      <th>Dam Type</th>
      <th>Height(m)</th>
      <th>Dam Length</th>
      <th>Volume Content of Dam</th>
      <th>Capacity(m3)</th>
      <th>Reservoir Area</th>
      <th>Effective Storage Capacity</th>
      <th>Purpose</th>
      <th>Designed Spillway Capacity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>MH09VH0100</td>
      <td>KOYNA</td>
      <td>17.401944</td>
      <td>73.752222</td>
      <td>1964.0</td>
      <td>Krishna</td>
      <td>Koyna.</td>
      <td>Patan.</td>
      <td>IV</td>
      <td>Composite_Concrete_and_Masonry</td>
      <td>103.02</td>
      <td>807.72</td>
      <td>1.555000e+06</td>
      <td>2.980680e+09</td>
      <td>1.196881e+08</td>
      <td>2.835540e+09</td>
      <td>I/H</td>
      <td>5082.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>590</td>
      <td>MH09HH0597</td>
      <td>JAYAKWADI</td>
      <td>19.485750</td>
      <td>75.368889</td>
      <td>1976.0</td>
      <td>Godavari</td>
      <td>Godavari.</td>
      <td>Paithan</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>41.30</td>
      <td>10415.00</td>
      <td>1.341000e+07</td>
      <td>2.909000e+09</td>
      <td>3.500000e+09</td>
      <td>2.170930e+09</td>
      <td>I/H</td>
      <td>18153.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>833</td>
      <td>MH09HH0843</td>
      <td>UJJANI</td>
      <td>18.074722</td>
      <td>75.121111</td>
      <td>1980.0</td>
      <td>Krishna</td>
      <td>Bhima</td>
      <td>Madha.</td>
      <td>III</td>
      <td>Other</td>
      <td>56.40</td>
      <td>3141.40</td>
      <td>3.320000e+06</td>
      <td>3.320010e+09</td>
      <td>2.900000e+08</td>
      <td>1.517200e+09</td>
      <td>I/S</td>
      <td>18010.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1216</td>
      <td>MH09HH1229</td>
      <td>TOTLADOH</td>
      <td>21.658889</td>
      <td>79.231944</td>
      <td>1989.0</td>
      <td>Godavari</td>
      <td>Pench</td>
      <td>Ramtek</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>74.50</td>
      <td>3061.00</td>
      <td>9.720000e+05</td>
      <td>1.166930e+09</td>
      <td>7.771000e+07</td>
      <td>1.016930e+09</td>
      <td>H</td>
      <td>12072.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>936</td>
      <td>MH09HH0947</td>
      <td>ISAPUR</td>
      <td>19.717500</td>
      <td>77.425556</td>
      <td>1982.0</td>
      <td>Godavari</td>
      <td>Penganga</td>
      <td>Pusad</td>
      <td>II</td>
      <td>Other</td>
      <td>48.00</td>
      <td>4088.50</td>
      <td>1.170000e+05</td>
      <td>1.279000e+09</td>
      <td>9.627000e+07</td>
      <td>9.640000e+08</td>
      <td>I</td>
      <td>10480.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2382</th>
      <td>2378</td>
      <td>MH09HH2416</td>
      <td>Kalgaon</td>
      <td>17.317500</td>
      <td>73.891667</td>
      <td>NaN</td>
      <td>Krishna</td>
      <td>Local Nala</td>
      <td>Karad</td>
      <td>IV</td>
      <td>Earthfill_Embankment</td>
      <td>32.26</td>
      <td>383.50</td>
      <td>6.197440e+02</td>
      <td>2.563000e+00</td>
      <td>2.118500e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>199.64</td>
    </tr>
    <tr>
      <th>2383</th>
      <td>2379</td>
      <td>MH09MH2417</td>
      <td>Kinkhed</td>
      <td>20.408333</td>
      <td>77.504167</td>
      <td>2016.0</td>
      <td>Area of Inland Drainage in Rajasthan</td>
      <td>Ghataprabha</td>
      <td>Karanja</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>17.74</td>
      <td>420.00</td>
      <td>NaN</td>
      <td>2.328000e+03</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>I</td>
      <td>248.00</td>
    </tr>
    <tr>
      <th>2384</th>
      <td>2380</td>
      <td>MH09MH2418</td>
      <td>Dahegaon</td>
      <td>20.191944</td>
      <td>78.701389</td>
      <td>2016.0</td>
      <td>Godavari</td>
      <td>Local Nalla</td>
      <td>Ralegaon</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>17.35</td>
      <td>1235.00</td>
      <td>NaN</td>
      <td>3.390000e+03</td>
      <td>8.030000e+08</td>
      <td>NaN</td>
      <td>I</td>
      <td>406.41</td>
    </tr>
    <tr>
      <th>2385</th>
      <td>2383</td>
      <td>MH09MH2421</td>
      <td>Gunjarga K T Weir</td>
      <td>18.050000</td>
      <td>76.819444</td>
      <td>2016.0</td>
      <td>Godavari</td>
      <td>Terna</td>
      <td>Nilanga</td>
      <td>III</td>
      <td>Earthfill_Embankment</td>
      <td>19.95</td>
      <td>101.00</td>
      <td>8.440000e+00</td>
      <td>1.368000e+03</td>
      <td>7.724000e+07</td>
      <td>NaN</td>
      <td>I</td>
      <td>4713.14</td>
    </tr>
    <tr>
      <th>2386</th>
      <td>2388</td>
      <td>MH09MH2426</td>
      <td>Jalkot St</td>
      <td>17.783333</td>
      <td>76.166667</td>
      <td>1999.0</td>
      <td>Godavari</td>
      <td>Local Nalla</td>
      <td>Tuljapur</td>
      <td>III</td>
      <td>Earthfill_Embankment</td>
      <td>15.30</td>
      <td>915.00</td>
      <td>NaN</td>
      <td>1.850000e+03</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>I</td>
      <td>416.55</td>
    </tr>
  </tbody>
</table>
<p>2387 rows × 19 columns</p>
</div>




```python
#Selection of rows based on conditional expressions
df_Dams["Height(m)"]>100
```




    0        True
    1       False
    2       False
    3       False
    4       False
            ...  
    2382    False
    2383    False
    2384    False
    2385    False
    2386    False
    Name: Height(m), Length: 2387, dtype: bool




```python
df_Dams["Capacity(m3)"]>2.0e+09
```




    0        True
    1        True
    2        True
    3       False
    4       False
            ...  
    2382    False
    2383    False
    2384    False
    2385    False
    2386    False
    Name: Capacity(m3), Length: 2387, dtype: bool




```python
#conditional expressions can be combined with and(&), or(|) operators
(df_Dams["Height(m)"]>100)&(df_Dams["Capacity(m3)"]>2.0e+09)
```




    0        True
    1       False
    2       False
    3       False
    4       False
            ...  
    2382    False
    2383    False
    2384    False
    2385    False
    2386    False
    Length: 2387, dtype: bool




```python
#our own definition of very big dams based on height of the dam and gross storage of the reservoir
Very_Big_dams = df_Dams[(df_Dams["Height(m)"]>100)&(df_Dams["Capacity(m3)"]>2.0e+09)]
```


```python
Very_Big_dams
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
      <th>Sr.No</th>
      <th>PIC</th>
      <th>Name of Dam</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Year of Completion</th>
      <th>River Basin</th>
      <th>River</th>
      <th>Neareast City</th>
      <th>Seismic Zone</th>
      <th>Dam Type</th>
      <th>Height(m)</th>
      <th>Dam Length</th>
      <th>Volume Content of Dam</th>
      <th>Capacity(m3)</th>
      <th>Reservoir Area</th>
      <th>Effective Storage Capacity</th>
      <th>Purpose</th>
      <th>Designed Spillway Capacity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>MH09VH0100</td>
      <td>KOYNA</td>
      <td>17.401944</td>
      <td>73.752222</td>
      <td>1964.0</td>
      <td>Krishna</td>
      <td>Koyna.</td>
      <td>Patan.</td>
      <td>IV</td>
      <td>Composite_Concrete_and_Masonry</td>
      <td>103.02</td>
      <td>807.72</td>
      <td>1555000.0</td>
      <td>2.980680e+09</td>
      <td>119688100.0</td>
      <td>2.835540e+09</td>
      <td>I/H</td>
      <td>5082.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
Big_dams = df_Dams[(df_Dams["Height(m)"]>50)&(df_Dams["Capacity(m3)"]>1.0e+09)]
Big_dams
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
      <th>Sr.No</th>
      <th>PIC</th>
      <th>Name of Dam</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Year of Completion</th>
      <th>River Basin</th>
      <th>River</th>
      <th>Neareast City</th>
      <th>Seismic Zone</th>
      <th>Dam Type</th>
      <th>Height(m)</th>
      <th>Dam Length</th>
      <th>Volume Content of Dam</th>
      <th>Capacity(m3)</th>
      <th>Reservoir Area</th>
      <th>Effective Storage Capacity</th>
      <th>Purpose</th>
      <th>Designed Spillway Capacity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>MH09VH0100</td>
      <td>KOYNA</td>
      <td>17.401944</td>
      <td>73.752222</td>
      <td>1964.0</td>
      <td>Krishna</td>
      <td>Koyna.</td>
      <td>Patan.</td>
      <td>IV</td>
      <td>Composite_Concrete_and_Masonry</td>
      <td>103.02</td>
      <td>807.72</td>
      <td>1555000.0</td>
      <td>2.980680e+09</td>
      <td>119688100.0</td>
      <td>2.835540e+09</td>
      <td>I/H</td>
      <td>5082.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>833</td>
      <td>MH09HH0843</td>
      <td>UJJANI</td>
      <td>18.074722</td>
      <td>75.121111</td>
      <td>1980.0</td>
      <td>Krishna</td>
      <td>Bhima</td>
      <td>Madha.</td>
      <td>III</td>
      <td>Other</td>
      <td>56.40</td>
      <td>3141.40</td>
      <td>3320000.0</td>
      <td>3.320010e+09</td>
      <td>290000000.0</td>
      <td>1.517200e+09</td>
      <td>I/S</td>
      <td>18010.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1216</td>
      <td>MH09HH1229</td>
      <td>TOTLADOH</td>
      <td>21.658889</td>
      <td>79.231944</td>
      <td>1989.0</td>
      <td>Godavari</td>
      <td>Pench</td>
      <td>Ramtek</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>74.50</td>
      <td>3061.00</td>
      <td>972000.0</td>
      <td>1.166930e+09</td>
      <td>77710000.0</td>
      <td>1.016930e+09</td>
      <td>H</td>
      <td>12072.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Dams in the list satisfying either of the conditions
Somewhat_Big_dams = df_Dams[(df_Dams["Height(m)"]>100)|(df_Dams["Capacity(m3)"]>2.0e+09)]
Somewhat_Big_dams 
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
      <th>Sr.No</th>
      <th>PIC</th>
      <th>Name of Dam</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Year of Completion</th>
      <th>River Basin</th>
      <th>River</th>
      <th>Neareast City</th>
      <th>Seismic Zone</th>
      <th>Dam Type</th>
      <th>Height(m)</th>
      <th>Dam Length</th>
      <th>Volume Content of Dam</th>
      <th>Capacity(m3)</th>
      <th>Reservoir Area</th>
      <th>Effective Storage Capacity</th>
      <th>Purpose</th>
      <th>Designed Spillway Capacity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>MH09VH0100</td>
      <td>KOYNA</td>
      <td>17.401944</td>
      <td>73.752222</td>
      <td>1964.0</td>
      <td>Krishna</td>
      <td>Koyna.</td>
      <td>Patan.</td>
      <td>IV</td>
      <td>Composite_Concrete_and_Masonry</td>
      <td>103.02</td>
      <td>807.72</td>
      <td>1555000.0</td>
      <td>2.980680e+09</td>
      <td>1.196881e+08</td>
      <td>2.835540e+09</td>
      <td>I/H</td>
      <td>5082.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>590</td>
      <td>MH09HH0597</td>
      <td>JAYAKWADI</td>
      <td>19.485750</td>
      <td>75.368889</td>
      <td>1976.0</td>
      <td>Godavari</td>
      <td>Godavari.</td>
      <td>Paithan</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>41.30</td>
      <td>10415.00</td>
      <td>13410000.0</td>
      <td>2.909000e+09</td>
      <td>3.500000e+09</td>
      <td>2.170930e+09</td>
      <td>I/H</td>
      <td>18153.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>833</td>
      <td>MH09HH0843</td>
      <td>UJJANI</td>
      <td>18.074722</td>
      <td>75.121111</td>
      <td>1980.0</td>
      <td>Krishna</td>
      <td>Bhima</td>
      <td>Madha.</td>
      <td>III</td>
      <td>Other</td>
      <td>56.40</td>
      <td>3141.40</td>
      <td>3320000.0</td>
      <td>3.320010e+09</td>
      <td>2.900000e+08</td>
      <td>1.517200e+09</td>
      <td>I/S</td>
      <td>18010.00</td>
    </tr>
    <tr>
      <th>56</th>
      <td>1813</td>
      <td>MH09VH1852</td>
      <td>Middle Vaitarna</td>
      <td>19.705556</td>
      <td>73.433889</td>
      <td>2012.0</td>
      <td>West Flowing Rivers from Tapi to Tadri</td>
      <td>Vaitarna</td>
      <td>Mal</td>
      <td>III</td>
      <td>Earthfill_Embankment</td>
      <td>102.40</td>
      <td>565.00</td>
      <td>1604000.0</td>
      <td>2.021000e+08</td>
      <td>6.400000e+06</td>
      <td>1.935300e+08</td>
      <td>S</td>
      <td>6348.00</td>
    </tr>
    <tr>
      <th>1226</th>
      <td>815</td>
      <td>MH09MH0824</td>
      <td>ADIVALI</td>
      <td>19.431389</td>
      <td>73.525278</td>
      <td>1980.0</td>
      <td>West Flowing Rivers from Tapi to Tadri</td>
      <td>Local Nala</td>
      <td>Shahapur</td>
      <td>III</td>
      <td>Earthfill_Embankment</td>
      <td>125.52</td>
      <td>386.00</td>
      <td>149000.0</td>
      <td>2.221000e+06</td>
      <td>3.070000e+05</td>
      <td>2.030000e+06</td>
      <td>I</td>
      <td>245.56</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_GD
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
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
#Selection of rows based on conditional expression
GD_HHS = df_GD[df_GD["Gauge(m)"]>200]
```


```python
#check the size with shape attribute of Pandas DataFrame
GD_HHS.shape
```




    (41, 5)




```python
GD_HHS
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3809</th>
      <td>07-06-2015</td>
      <td>HHS</td>
      <td>258.50</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3816</th>
      <td>14-06-2015</td>
      <td>HHS</td>
      <td>257.88</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3823</th>
      <td>21-06-2015</td>
      <td>HHS</td>
      <td>257.95</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3828</th>
      <td>26-06-2015</td>
      <td>HHS</td>
      <td>259.13</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3830</th>
      <td>28-06-2015</td>
      <td>HHS</td>
      <td>259.33</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3837</th>
      <td>05-07-2015</td>
      <td>HHS</td>
      <td>258.56</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3844</th>
      <td>12-07-2015</td>
      <td>HHS</td>
      <td>258.44</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3850</th>
      <td>18-07-2015</td>
      <td>HHS</td>
      <td>258.45</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3851</th>
      <td>19-07-2015</td>
      <td>HHS</td>
      <td>258.88</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3858</th>
      <td>26-07-2015</td>
      <td>HHS</td>
      <td>259.14</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3865</th>
      <td>02-08-2015</td>
      <td>HHS</td>
      <td>258.54</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3871</th>
      <td>08-08-2015</td>
      <td>HHS</td>
      <td>258.25</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3878</th>
      <td>15-08-2015</td>
      <td>HHS</td>
      <td>258.80</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3879</th>
      <td>16-08-2015</td>
      <td>HHS</td>
      <td>258.93</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3886</th>
      <td>23-08-2015</td>
      <td>HHS</td>
      <td>259.32</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3893</th>
      <td>30-08-2015</td>
      <td>HHS</td>
      <td>258.74</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3900</th>
      <td>06-09-2015</td>
      <td>HHS</td>
      <td>258.50</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3907</th>
      <td>13-09-2015</td>
      <td>HHS</td>
      <td>258.39</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3911</th>
      <td>17-09-2015</td>
      <td>HHS</td>
      <td>258.18</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3914</th>
      <td>20-09-2015</td>
      <td>HHS</td>
      <td>258.36</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3919</th>
      <td>25-09-2015</td>
      <td>HHS</td>
      <td>259.04</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3921</th>
      <td>27-09-2015</td>
      <td>HHS</td>
      <td>259.66</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3926</th>
      <td>02-10-2015</td>
      <td>HHS</td>
      <td>258.74</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3928</th>
      <td>04-10-2015</td>
      <td>HHS</td>
      <td>258.74</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3935</th>
      <td>11-10-2015</td>
      <td>HHS</td>
      <td>258.36</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3942</th>
      <td>18-10-2015</td>
      <td>HHS</td>
      <td>258.20</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3946</th>
      <td>22-10-2015</td>
      <td>HHS</td>
      <td>258.38</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3948</th>
      <td>24-10-2015</td>
      <td>HHS</td>
      <td>258.40</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3949</th>
      <td>25-10-2015</td>
      <td>HHS</td>
      <td>258.37</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3956</th>
      <td>01-11-2015</td>
      <td>HHS</td>
      <td>258.55</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3963</th>
      <td>08-11-2015</td>
      <td>HHS</td>
      <td>258.78</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3966</th>
      <td>11-11-2015</td>
      <td>HHS</td>
      <td>259.48</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3970</th>
      <td>15-11-2015</td>
      <td>HHS</td>
      <td>258.66</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3977</th>
      <td>22-11-2015</td>
      <td>HHS</td>
      <td>258.83</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3984</th>
      <td>29-11-2015</td>
      <td>HHS</td>
      <td>258.45</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3991</th>
      <td>06-12-2015</td>
      <td>HHS</td>
      <td>258.46</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3998</th>
      <td>13-12-2015</td>
      <td>HHS</td>
      <td>258.18</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4005</th>
      <td>20-12-2015</td>
      <td>HHS</td>
      <td>258.15</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4009</th>
      <td>24-12-2015</td>
      <td>HHS</td>
      <td>258.06</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4010</th>
      <td>25-12-2015</td>
      <td>HHS</td>
      <td>258.06</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4012</th>
      <td>27-12-2015</td>
      <td>HHS</td>
      <td>258.04</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_Dams
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
      <th>Sr.No</th>
      <th>PIC</th>
      <th>Name of Dam</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Year of Completion</th>
      <th>River Basin</th>
      <th>River</th>
      <th>Neareast City</th>
      <th>Seismic Zone</th>
      <th>Dam Type</th>
      <th>Height(m)</th>
      <th>Dam Length</th>
      <th>Volume Content of Dam</th>
      <th>Capacity(m3)</th>
      <th>Reservoir Area</th>
      <th>Effective Storage Capacity</th>
      <th>Purpose</th>
      <th>Designed Spillway Capacity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>MH09VH0100</td>
      <td>KOYNA</td>
      <td>17.401944</td>
      <td>73.752222</td>
      <td>1964.0</td>
      <td>Krishna</td>
      <td>Koyna.</td>
      <td>Patan.</td>
      <td>IV</td>
      <td>Composite_Concrete_and_Masonry</td>
      <td>103.02</td>
      <td>807.72</td>
      <td>1.555000e+06</td>
      <td>2.980680e+09</td>
      <td>1.196881e+08</td>
      <td>2.835540e+09</td>
      <td>I/H</td>
      <td>5082.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>590</td>
      <td>MH09HH0597</td>
      <td>JAYAKWADI</td>
      <td>19.485750</td>
      <td>75.368889</td>
      <td>1976.0</td>
      <td>Godavari</td>
      <td>Godavari.</td>
      <td>Paithan</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>41.30</td>
      <td>10415.00</td>
      <td>1.341000e+07</td>
      <td>2.909000e+09</td>
      <td>3.500000e+09</td>
      <td>2.170930e+09</td>
      <td>I/H</td>
      <td>18153.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>833</td>
      <td>MH09HH0843</td>
      <td>UJJANI</td>
      <td>18.074722</td>
      <td>75.121111</td>
      <td>1980.0</td>
      <td>Krishna</td>
      <td>Bhima</td>
      <td>Madha.</td>
      <td>III</td>
      <td>Other</td>
      <td>56.40</td>
      <td>3141.40</td>
      <td>3.320000e+06</td>
      <td>3.320010e+09</td>
      <td>2.900000e+08</td>
      <td>1.517200e+09</td>
      <td>I/S</td>
      <td>18010.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1216</td>
      <td>MH09HH1229</td>
      <td>TOTLADOH</td>
      <td>21.658889</td>
      <td>79.231944</td>
      <td>1989.0</td>
      <td>Godavari</td>
      <td>Pench</td>
      <td>Ramtek</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>74.50</td>
      <td>3061.00</td>
      <td>9.720000e+05</td>
      <td>1.166930e+09</td>
      <td>7.771000e+07</td>
      <td>1.016930e+09</td>
      <td>H</td>
      <td>12072.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>936</td>
      <td>MH09HH0947</td>
      <td>ISAPUR</td>
      <td>19.717500</td>
      <td>77.425556</td>
      <td>1982.0</td>
      <td>Godavari</td>
      <td>Penganga</td>
      <td>Pusad</td>
      <td>II</td>
      <td>Other</td>
      <td>48.00</td>
      <td>4088.50</td>
      <td>1.170000e+05</td>
      <td>1.279000e+09</td>
      <td>9.627000e+07</td>
      <td>9.640000e+08</td>
      <td>I</td>
      <td>10480.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2382</th>
      <td>2378</td>
      <td>MH09HH2416</td>
      <td>Kalgaon</td>
      <td>17.317500</td>
      <td>73.891667</td>
      <td>NaN</td>
      <td>Krishna</td>
      <td>Local Nala</td>
      <td>Karad</td>
      <td>IV</td>
      <td>Earthfill_Embankment</td>
      <td>32.26</td>
      <td>383.50</td>
      <td>6.197440e+02</td>
      <td>2.563000e+00</td>
      <td>2.118500e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>199.64</td>
    </tr>
    <tr>
      <th>2383</th>
      <td>2379</td>
      <td>MH09MH2417</td>
      <td>Kinkhed</td>
      <td>20.408333</td>
      <td>77.504167</td>
      <td>2016.0</td>
      <td>Area of Inland Drainage in Rajasthan</td>
      <td>Ghataprabha</td>
      <td>Karanja</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>17.74</td>
      <td>420.00</td>
      <td>NaN</td>
      <td>2.328000e+03</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>I</td>
      <td>248.00</td>
    </tr>
    <tr>
      <th>2384</th>
      <td>2380</td>
      <td>MH09MH2418</td>
      <td>Dahegaon</td>
      <td>20.191944</td>
      <td>78.701389</td>
      <td>2016.0</td>
      <td>Godavari</td>
      <td>Local Nalla</td>
      <td>Ralegaon</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>17.35</td>
      <td>1235.00</td>
      <td>NaN</td>
      <td>3.390000e+03</td>
      <td>8.030000e+08</td>
      <td>NaN</td>
      <td>I</td>
      <td>406.41</td>
    </tr>
    <tr>
      <th>2385</th>
      <td>2383</td>
      <td>MH09MH2421</td>
      <td>Gunjarga K T Weir</td>
      <td>18.050000</td>
      <td>76.819444</td>
      <td>2016.0</td>
      <td>Godavari</td>
      <td>Terna</td>
      <td>Nilanga</td>
      <td>III</td>
      <td>Earthfill_Embankment</td>
      <td>19.95</td>
      <td>101.00</td>
      <td>8.440000e+00</td>
      <td>1.368000e+03</td>
      <td>7.724000e+07</td>
      <td>NaN</td>
      <td>I</td>
      <td>4713.14</td>
    </tr>
    <tr>
      <th>2386</th>
      <td>2388</td>
      <td>MH09MH2426</td>
      <td>Jalkot St</td>
      <td>17.783333</td>
      <td>76.166667</td>
      <td>1999.0</td>
      <td>Godavari</td>
      <td>Local Nalla</td>
      <td>Tuljapur</td>
      <td>III</td>
      <td>Earthfill_Embankment</td>
      <td>15.30</td>
      <td>915.00</td>
      <td>NaN</td>
      <td>1.850000e+03</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>I</td>
      <td>416.55</td>
    </tr>
  </tbody>
</table>
<p>2387 rows × 19 columns</p>
</div>




```python
#sorting of values of a column of DataFrame using sort_values() method
df_Dams.sort_values(by = 'Height(m)', ascending = False)
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
      <th>Sr.No</th>
      <th>PIC</th>
      <th>Name of Dam</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Year of Completion</th>
      <th>River Basin</th>
      <th>River</th>
      <th>Neareast City</th>
      <th>Seismic Zone</th>
      <th>Dam Type</th>
      <th>Height(m)</th>
      <th>Dam Length</th>
      <th>Volume Content of Dam</th>
      <th>Capacity(m3)</th>
      <th>Reservoir Area</th>
      <th>Effective Storage Capacity</th>
      <th>Purpose</th>
      <th>Designed Spillway Capacity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1226</th>
      <td>815</td>
      <td>MH09MH0824</td>
      <td>ADIVALI</td>
      <td>19.431389</td>
      <td>73.525278</td>
      <td>1980.0</td>
      <td>West Flowing Rivers from Tapi to Tadri</td>
      <td>Local Nala</td>
      <td>Shahapur</td>
      <td>III</td>
      <td>Earthfill_Embankment</td>
      <td>125.52</td>
      <td>386.00</td>
      <td>149000.0</td>
      <td>2.221000e+06</td>
      <td>307000.0</td>
      <td>2.030000e+06</td>
      <td>I</td>
      <td>245.56</td>
    </tr>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>MH09VH0100</td>
      <td>KOYNA</td>
      <td>17.401944</td>
      <td>73.752222</td>
      <td>1964.0</td>
      <td>Krishna</td>
      <td>Koyna.</td>
      <td>Patan.</td>
      <td>IV</td>
      <td>Composite_Concrete_and_Masonry</td>
      <td>103.02</td>
      <td>807.72</td>
      <td>1555000.0</td>
      <td>2.980680e+09</td>
      <td>119688100.0</td>
      <td>2.835540e+09</td>
      <td>I/H</td>
      <td>5082.00</td>
    </tr>
    <tr>
      <th>56</th>
      <td>1813</td>
      <td>MH09VH1852</td>
      <td>Middle Vaitarna</td>
      <td>19.705556</td>
      <td>73.433889</td>
      <td>2012.0</td>
      <td>West Flowing Rivers from Tapi to Tadri</td>
      <td>Vaitarna</td>
      <td>Mal</td>
      <td>III</td>
      <td>Earthfill_Embankment</td>
      <td>102.40</td>
      <td>565.00</td>
      <td>1604000.0</td>
      <td>2.021000e+08</td>
      <td>6400000.0</td>
      <td>1.935300e+08</td>
      <td>S</td>
      <td>6348.00</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1528</td>
      <td>MH09HH1542</td>
      <td>WARANA</td>
      <td>19.514722</td>
      <td>76.667778</td>
      <td>2000.0</td>
      <td>Krishna</td>
      <td>Warna river</td>
      <td>Shahuwadi</td>
      <td>IV</td>
      <td>Composite_Concrete_and_Earth_fill</td>
      <td>88.80</td>
      <td>1580.00</td>
      <td>21219000.0</td>
      <td>9.741880e+08</td>
      <td>2889000.0</td>
      <td>7.793480e+08</td>
      <td>I/H/S</td>
      <td>3222.00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>999</td>
      <td>MH09HH1011</td>
      <td>BHATSA</td>
      <td>19.513056</td>
      <td>73.417500</td>
      <td>1983.0</td>
      <td>West Flowing Rivers from Tapi to Tadri</td>
      <td>Bhatsa and Chorna</td>
      <td>Shahapur</td>
      <td>III</td>
      <td>Other</td>
      <td>88.50</td>
      <td>959.00</td>
      <td>18250000.0</td>
      <td>9.761000e+08</td>
      <td>27250000.0</td>
      <td>9.421000e+08</td>
      <td>I</td>
      <td>5342.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2363</th>
      <td>1743</td>
      <td>MH09HH1770</td>
      <td>SARANG KHEDA</td>
      <td>21.426944</td>
      <td>74.530000</td>
      <td>NaN</td>
      <td>Tapi</td>
      <td>Tapi</td>
      <td>Shahada</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2365</th>
      <td>1797</td>
      <td>MH09MH1838</td>
      <td>MAHIND</td>
      <td>17.368056</td>
      <td>73.903611</td>
      <td>NaN</td>
      <td>Krishna</td>
      <td>Koyna.</td>
      <td>Patan</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2366</th>
      <td>1803</td>
      <td>MH09LH1825</td>
      <td>SHIRASWADI</td>
      <td>17.499444</td>
      <td>74.443611</td>
      <td>1973.0</td>
      <td>To Be Confirmed</td>
      <td>Local</td>
      <td>Sambalpur</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2367</th>
      <td>1804</td>
      <td>MH09LH1831</td>
      <td>TULSHI VRIDHAVAN</td>
      <td>16.524722</td>
      <td>74.015000</td>
      <td>1979.0</td>
      <td>To Be Confirmed</td>
      <td>Local</td>
      <td>Sambalpur</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2368</th>
      <td>1806</td>
      <td>MH09LH1841</td>
      <td>WAKHARI</td>
      <td>18.438333</td>
      <td>74.341944</td>
      <td>NaN</td>
      <td>Krishna</td>
      <td>Ghataprabha</td>
      <td>Sambalpur</td>
      <td>II</td>
      <td>Earthfill_Embankment</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>2387 rows × 19 columns</p>
</div>




```python
#basic statistics of Pandas DataFrame can be obtained with describe() method
df_Dams.describe()
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
      <th>Sr.No</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Year of Completion</th>
      <th>Height(m)</th>
      <th>Dam Length</th>
      <th>Volume Content of Dam</th>
      <th>Capacity(m3)</th>
      <th>Reservoir Area</th>
      <th>Effective Storage Capacity</th>
      <th>Designed Spillway Capacity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2387.000000</td>
      <td>2387.000000</td>
      <td>2387.000000</td>
      <td>2112.000000</td>
      <td>2367.000000</td>
      <td>2363.000000</td>
      <td>2.189000e+03</td>
      <td>2.367000e+03</td>
      <td>2.231000e+03</td>
      <td>2.340000e+03</td>
      <td>2.284000e+03</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1194.999581</td>
      <td>19.331339</td>
      <td>75.755363</td>
      <td>1983.419508</td>
      <td>19.830324</td>
      <td>2020.356019</td>
      <td>9.387402e+05</td>
      <td>2.709327e+07</td>
      <td>1.388830e+07</td>
      <td>1.955128e+07</td>
      <td>1.535373e+03</td>
    </tr>
    <tr>
      <th>std</th>
      <td>690.350301</td>
      <td>1.470480</td>
      <td>1.801071</td>
      <td>48.036552</td>
      <td>10.461409</td>
      <td>26926.674227</td>
      <td>8.652853e+06</td>
      <td>1.460839e+08</td>
      <td>1.341201e+08</td>
      <td>1.077140e+08</td>
      <td>2.165791e+04</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>10.033333</td>
      <td>70.001667</td>
      <td>15.000000</td>
      <td>10.000000</td>
      <td>10.400000</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>1.400000e+02</td>
      <td>1.070000e+02</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>597.500000</td>
      <td>18.362222</td>
      <td>74.211250</td>
      <td>1975.000000</td>
      <td>13.595000</td>
      <td>457.000000</td>
      <td>1.066300e+05</td>
      <td>1.570000e+06</td>
      <td>2.907500e+05</td>
      <td>1.402000e+06</td>
      <td>1.783600e+02</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1194.000000</td>
      <td>19.581667</td>
      <td>75.566667</td>
      <td>1984.000000</td>
      <td>17.000000</td>
      <td>760.000000</td>
      <td>1.744000e+05</td>
      <td>2.372000e+06</td>
      <td>5.600000e+05</td>
      <td>2.120000e+06</td>
      <td>3.285000e+02</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1791.500000</td>
      <td>20.423889</td>
      <td>76.983472</td>
      <td>1998.000000</td>
      <td>22.200000</td>
      <td>1229.500000</td>
      <td>4.130000e+05</td>
      <td>5.977500e+06</td>
      <td>1.240000e+06</td>
      <td>5.094500e+06</td>
      <td>7.550000e+02</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2394.000000</td>
      <td>27.294444</td>
      <td>82.133333</td>
      <td>2016.000000</td>
      <td>125.520000</td>
      <td>970000.000000</td>
      <td>2.950000e+08</td>
      <td>3.320010e+09</td>
      <td>3.500000e+09</td>
      <td>2.835540e+09</td>
      <td>1.019000e+06</td>
    </tr>
  </tbody>
</table>
</div>




```python
#maximum value in a column of a DataFrame can be obtained with max() method
df_Dams["Capacity(m3)"].max()
```




    3320010000.0




```python
df_GD
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
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
#calculation of mean monthly discharge for Jan 2005 with selection of rows by .loc operator
df_GD.loc[0:31,"Discharge (cumecs)"].mean()
```




    41.675875




```python
df_GD
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
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
#set_index() method can be used to set any column as index instead of default integer index values
df_GD1= df_GD.set_index("Day",drop= True)
df_GD1
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
    <tr>
      <th>Day</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>01-01-2005</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.473</td>
      <td>O</td>
    </tr>
    <tr>
      <th>02-01-2005</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.270</td>
      <td>C</td>
    </tr>
    <tr>
      <th>03-01-2005</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.033</td>
      <td>O</td>
    </tr>
    <tr>
      <th>04-01-2005</th>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.476</td>
      <td>O</td>
    </tr>
    <tr>
      <th>05-01-2005</th>
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
    </tr>
    <tr>
      <th>27-12-2015</th>
      <td>HHS</td>
      <td>258.040</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28-12-2015</th>
      <td>HZS</td>
      <td>3.040</td>
      <td>55.259</td>
      <td>O</td>
    </tr>
    <tr>
      <th>29-12-2015</th>
      <td>HZS</td>
      <td>3.005</td>
      <td>51.204</td>
      <td>O</td>
    </tr>
    <tr>
      <th>30-12-2015</th>
      <td>HZS</td>
      <td>3.000</td>
      <td>50.639</td>
      <td>O</td>
    </tr>
    <tr>
      <th>31-12-2015</th>
      <td>HZS</td>
      <td>2.905</td>
      <td>41.459</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
<p>4017 rows × 4 columns</p>
</div>




```python
#Data visualisation through plot() method
df_GD1["Discharge (cumecs)"].plot()
```




    <AxesSubplot:xlabel='Day'>




    
![png](06_Working_with_Pandas_Part_II_files/06_Working_with_Pandas_Part_II_59_1.png)
    



```python
#while reading the data from csv file index caolumn can be set and parsing of Dates can be enabled
#parsing of dates creates Pandas datetime objects
df_GD2=pd.read_csv(fp_GD_data,index_col=0,parse_dates=True)
df_GD2
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
      <th>Data Type</th>
      <th>Mean Gauge (m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
    <tr>
      <th>Day</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2005-01-01</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.473</td>
      <td>O</td>
    </tr>
    <tr>
      <th>2005-02-01</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.270</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2005-03-01</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.033</td>
      <td>O</td>
    </tr>
    <tr>
      <th>2005-04-01</th>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.476</td>
      <td>O</td>
    </tr>
    <tr>
      <th>2005-05-01</th>
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
    </tr>
    <tr>
      <th>2015-12-27</th>
      <td>HHS</td>
      <td>258.040</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2015-12-28</th>
      <td>HZS</td>
      <td>3.040</td>
      <td>55.259</td>
      <td>O</td>
    </tr>
    <tr>
      <th>2015-12-29</th>
      <td>HZS</td>
      <td>3.005</td>
      <td>51.204</td>
      <td>O</td>
    </tr>
    <tr>
      <th>2015-12-30</th>
      <td>HZS</td>
      <td>3.000</td>
      <td>50.639</td>
      <td>O</td>
    </tr>
    <tr>
      <th>2015-12-31</th>
      <td>HZS</td>
      <td>2.905</td>
      <td>41.459</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
<p>4017 rows × 4 columns</p>
</div>




```python
#Data visualisation through plot() method after parsing of dates
df_GD2["Discharge (cumecs)"].plot()
```




    <AxesSubplot:xlabel='Day'>




    
![png](06_Working_with_Pandas_Part_II_files/06_Working_with_Pandas_Part_II_61_1.png)
    



```python
#use of plot.scatter() method for printing scatterplot
df_GD.plot.scatter(x='Gauge(m)',y='Discharge (cumecs)')
```




    <AxesSubplot:xlabel='Gauge(m)', ylabel='Discharge (cumecs)'>




    
![png](06_Working_with_Pandas_Part_II_files/06_Working_with_Pandas_Part_II_62_1.png)
    



```python
#while reading the data from excel file index column can be set and parsing of Dates can be enabled
#parsing of dates creates Pandas datetime objects
df_Reservoir = pd.read_excel(fp_Reservoir_data,index_col=3,parse_dates=True)
df_Reservoir
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
      <th>STRUCODE</th>
      <th>BOSHORT</th>
      <th>STATE</th>
      <th>LEVEL</th>
      <th>CAPACITY</th>
    </tr>
    <tr>
      <th>DDATE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2007-06-01</th>
      <td>D03170</td>
      <td>Mulshi Dam</td>
      <td>MAHARASHTRA</td>
      <td>591.940002</td>
      <td>0.045192</td>
    </tr>
    <tr>
      <th>2007-06-02</th>
      <td>D03170</td>
      <td>Mulshi Dam</td>
      <td>MAHARASHTRA</td>
      <td>591.840027</td>
      <td>0.042631</td>
    </tr>
    <tr>
      <th>2007-06-03</th>
      <td>D03170</td>
      <td>Mulshi Dam</td>
      <td>MAHARASHTRA</td>
      <td>591.750000</td>
      <td>0.040327</td>
    </tr>
    <tr>
      <th>2007-06-04</th>
      <td>D03170</td>
      <td>Mulshi Dam</td>
      <td>MAHARASHTRA</td>
      <td>591.729980</td>
      <td>0.039821</td>
    </tr>
    <tr>
      <th>2007-06-05</th>
      <td>D03170</td>
      <td>Mulshi Dam</td>
      <td>MAHARASHTRA</td>
      <td>591.599976</td>
      <td>0.036532</td>
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
      <th>2017-05-27</th>
      <td>D03170</td>
      <td>Mulshi Dam</td>
      <td>MAHARASHTRA</td>
      <td>591.969971</td>
      <td>0.045961</td>
    </tr>
    <tr>
      <th>2017-05-28</th>
      <td>D03170</td>
      <td>Mulshi Dam</td>
      <td>MAHARASHTRA</td>
      <td>591.909973</td>
      <td>0.044425</td>
    </tr>
    <tr>
      <th>2017-05-29</th>
      <td>D03170</td>
      <td>Mulshi Dam</td>
      <td>MAHARASHTRA</td>
      <td>591.880005</td>
      <td>0.043656</td>
    </tr>
    <tr>
      <th>2017-05-30</th>
      <td>D03170</td>
      <td>Mulshi Dam</td>
      <td>MAHARASHTRA</td>
      <td>591.739990</td>
      <td>0.040074</td>
    </tr>
    <tr>
      <th>2017-05-31</th>
      <td>D03170</td>
      <td>Mulshi Dam</td>
      <td>MAHARASHTRA</td>
      <td>591.599976</td>
      <td>0.036532</td>
    </tr>
  </tbody>
</table>
<p>3653 rows × 5 columns</p>
</div>




```python
#Data visualisation through plot() method after parsing of dates
df_Reservoir["LEVEL"].plot()
```




    <AxesSubplot:xlabel='DDATE'>




    
![png](06_Working_with_Pandas_Part_II_files/06_Working_with_Pandas_Part_II_64_1.png)
    



```python
#reading of data from excel(.xls) file into a Pandas DataFrame with passing of sheet_name parameter
#for handling .xls files you may need to install xlrd python package in your environment
#for handling .xlsx files you may need to install openpyxl python package in your environment
df_Rain=pd.read_excel(fp_rainfall_data, sheet_name='Karnataka')
```


```python
df_Rain
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
      <th>State</th>
      <th>District</th>
      <th>Year</th>
      <th>January</th>
      <th>February</th>
      <th>March</th>
      <th>April</th>
      <th>May</th>
      <th>June</th>
      <th>July</th>
      <th>August</th>
      <th>September</th>
      <th>October</th>
      <th>November</th>
      <th>December</th>
      <th>Annual Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Karnataka</td>
      <td>Bagalkote</td>
      <td>2004</td>
      <td>1.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>11.6</td>
      <td>103.9</td>
      <td>123.9</td>
      <td>75.2</td>
      <td>32.8</td>
      <td>142.9</td>
      <td>57.4</td>
      <td>0.6</td>
      <td>0.0</td>
      <td>550.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Karnataka</td>
      <td>Bagalkote</td>
      <td>2005</td>
      <td>0.8</td>
      <td>0.2</td>
      <td>2.5</td>
      <td>44.7</td>
      <td>49.7</td>
      <td>68.1</td>
      <td>117.6</td>
      <td>71.1</td>
      <td>76.9</td>
      <td>124.3</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>556.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Karnataka</td>
      <td>Bagalkote</td>
      <td>2006</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.1</td>
      <td>9.5</td>
      <td>85.9</td>
      <td>98.1</td>
      <td>29.7</td>
      <td>22.4</td>
      <td>122.3</td>
      <td>37.5</td>
      <td>13.9</td>
      <td>0.0</td>
      <td>428.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Karnataka</td>
      <td>Bagalkote</td>
      <td>2007</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.2</td>
      <td>3.0</td>
      <td>52.9</td>
      <td>195.4</td>
      <td>43.5</td>
      <td>108.7</td>
      <td>267.3</td>
      <td>38.6</td>
      <td>4.2</td>
      <td>0.1</td>
      <td>713.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Karnataka</td>
      <td>Bagalkote</td>
      <td>2008</td>
      <td>0.0</td>
      <td>16.7</td>
      <td>94.2</td>
      <td>10.3</td>
      <td>37.5</td>
      <td>46.5</td>
      <td>28.3</td>
      <td>60.2</td>
      <td>135.4</td>
      <td>60.3</td>
      <td>27.2</td>
      <td>0.3</td>
      <td>516.9</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>184</th>
      <td>Karnataka</td>
      <td>Uttar Kannada</td>
      <td>2006</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.3</td>
      <td>0.6</td>
      <td>319.7</td>
      <td>708.9</td>
      <td>967.5</td>
      <td>784.4</td>
      <td>407.6</td>
      <td>217.7</td>
      <td>50.8</td>
      <td>0.0</td>
      <td>3465.5</td>
    </tr>
    <tr>
      <th>185</th>
      <td>Karnataka</td>
      <td>Uttar Kannada</td>
      <td>2007</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>1.9</td>
      <td>27.8</td>
      <td>62.9</td>
      <td>949.7</td>
      <td>810.5</td>
      <td>935.8</td>
      <td>549.6</td>
      <td>124.4</td>
      <td>28.4</td>
      <td>0.4</td>
      <td>3491.5</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Karnataka</td>
      <td>Uttar Kannada</td>
      <td>2008</td>
      <td>0.0</td>
      <td>5.3</td>
      <td>95.3</td>
      <td>11.9</td>
      <td>40.0</td>
      <td>697.5</td>
      <td>545.6</td>
      <td>831.9</td>
      <td>311.7</td>
      <td>51.9</td>
      <td>8.4</td>
      <td>1.5</td>
      <td>2601.0</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Karnataka</td>
      <td>Uttar Kannada</td>
      <td>2009</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>27.6</td>
      <td>16.4</td>
      <td>83.1</td>
      <td>428.0</td>
      <td>1412.6</td>
      <td>365.7</td>
      <td>503.2</td>
      <td>267.1</td>
      <td>113.0</td>
      <td>12.6</td>
      <td>3229.3</td>
    </tr>
    <tr>
      <th>188</th>
      <td>Karnataka</td>
      <td>Uttar Kannada</td>
      <td>2010</td>
      <td>8.9</td>
      <td>0.0</td>
      <td>1.7</td>
      <td>48.9</td>
      <td>74.4</td>
      <td>625.0</td>
      <td>1206.2</td>
      <td>555.2</td>
      <td>497.0</td>
      <td>261.8</td>
      <td>195.0</td>
      <td>6.3</td>
      <td>3480.4</td>
    </tr>
  </tbody>
</table>
<p>189 rows × 16 columns</p>
</div>




```python
#deriving a new column of Pandas Dataframe from existing columns
df_Rain["Monsoon"]=df_Rain["June"]+df_Rain["July"]+df_Rain["August"]+df_Rain["September"]
```


```python
df_Rain
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
      <th>State</th>
      <th>District</th>
      <th>Year</th>
      <th>January</th>
      <th>February</th>
      <th>March</th>
      <th>April</th>
      <th>May</th>
      <th>June</th>
      <th>July</th>
      <th>August</th>
      <th>September</th>
      <th>October</th>
      <th>November</th>
      <th>December</th>
      <th>Annual Total</th>
      <th>Monsoon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Karnataka</td>
      <td>Bagalkote</td>
      <td>2004</td>
      <td>1.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>11.6</td>
      <td>103.9</td>
      <td>123.9</td>
      <td>75.2</td>
      <td>32.8</td>
      <td>142.9</td>
      <td>57.4</td>
      <td>0.6</td>
      <td>0.0</td>
      <td>550.1</td>
      <td>374.8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Karnataka</td>
      <td>Bagalkote</td>
      <td>2005</td>
      <td>0.8</td>
      <td>0.2</td>
      <td>2.5</td>
      <td>44.7</td>
      <td>49.7</td>
      <td>68.1</td>
      <td>117.6</td>
      <td>71.1</td>
      <td>76.9</td>
      <td>124.3</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>556.0</td>
      <td>333.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Karnataka</td>
      <td>Bagalkote</td>
      <td>2006</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.1</td>
      <td>9.5</td>
      <td>85.9</td>
      <td>98.1</td>
      <td>29.7</td>
      <td>22.4</td>
      <td>122.3</td>
      <td>37.5</td>
      <td>13.9</td>
      <td>0.0</td>
      <td>428.4</td>
      <td>272.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Karnataka</td>
      <td>Bagalkote</td>
      <td>2007</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.2</td>
      <td>3.0</td>
      <td>52.9</td>
      <td>195.4</td>
      <td>43.5</td>
      <td>108.7</td>
      <td>267.3</td>
      <td>38.6</td>
      <td>4.2</td>
      <td>0.1</td>
      <td>713.9</td>
      <td>614.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Karnataka</td>
      <td>Bagalkote</td>
      <td>2008</td>
      <td>0.0</td>
      <td>16.7</td>
      <td>94.2</td>
      <td>10.3</td>
      <td>37.5</td>
      <td>46.5</td>
      <td>28.3</td>
      <td>60.2</td>
      <td>135.4</td>
      <td>60.3</td>
      <td>27.2</td>
      <td>0.3</td>
      <td>516.9</td>
      <td>270.4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>184</th>
      <td>Karnataka</td>
      <td>Uttar Kannada</td>
      <td>2006</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.3</td>
      <td>0.6</td>
      <td>319.7</td>
      <td>708.9</td>
      <td>967.5</td>
      <td>784.4</td>
      <td>407.6</td>
      <td>217.7</td>
      <td>50.8</td>
      <td>0.0</td>
      <td>3465.5</td>
      <td>2868.4</td>
    </tr>
    <tr>
      <th>185</th>
      <td>Karnataka</td>
      <td>Uttar Kannada</td>
      <td>2007</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>1.9</td>
      <td>27.8</td>
      <td>62.9</td>
      <td>949.7</td>
      <td>810.5</td>
      <td>935.8</td>
      <td>549.6</td>
      <td>124.4</td>
      <td>28.4</td>
      <td>0.4</td>
      <td>3491.5</td>
      <td>3245.6</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Karnataka</td>
      <td>Uttar Kannada</td>
      <td>2008</td>
      <td>0.0</td>
      <td>5.3</td>
      <td>95.3</td>
      <td>11.9</td>
      <td>40.0</td>
      <td>697.5</td>
      <td>545.6</td>
      <td>831.9</td>
      <td>311.7</td>
      <td>51.9</td>
      <td>8.4</td>
      <td>1.5</td>
      <td>2601.0</td>
      <td>2386.7</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Karnataka</td>
      <td>Uttar Kannada</td>
      <td>2009</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>27.6</td>
      <td>16.4</td>
      <td>83.1</td>
      <td>428.0</td>
      <td>1412.6</td>
      <td>365.7</td>
      <td>503.2</td>
      <td>267.1</td>
      <td>113.0</td>
      <td>12.6</td>
      <td>3229.3</td>
      <td>2709.5</td>
    </tr>
    <tr>
      <th>188</th>
      <td>Karnataka</td>
      <td>Uttar Kannada</td>
      <td>2010</td>
      <td>8.9</td>
      <td>0.0</td>
      <td>1.7</td>
      <td>48.9</td>
      <td>74.4</td>
      <td>625.0</td>
      <td>1206.2</td>
      <td>555.2</td>
      <td>497.0</td>
      <td>261.8</td>
      <td>195.0</td>
      <td>6.3</td>
      <td>3480.4</td>
      <td>2883.4</td>
    </tr>
  </tbody>
</table>
<p>189 rows × 17 columns</p>
</div>




```python
#district wise grouping of mean monthly rainfall values using groupby() method
df_Rain.groupby('District').mean()
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
      <th>January</th>
      <th>February</th>
      <th>March</th>
      <th>April</th>
      <th>May</th>
      <th>June</th>
      <th>July</th>
      <th>August</th>
      <th>September</th>
      <th>October</th>
      <th>November</th>
      <th>December</th>
      <th>Annual Total</th>
      <th>Monsoon</th>
    </tr>
    <tr>
      <th>District</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bagalkote</th>
      <td>2007.0</td>
      <td>2.285714</td>
      <td>2.428571</td>
      <td>15.557143</td>
      <td>14.928571</td>
      <td>64.800000</td>
      <td>108.671429</td>
      <td>60.800000</td>
      <td>78.828571</td>
      <td>143.514286</td>
      <td>85.214286</td>
      <td>22.571429</td>
      <td>4.571429</td>
      <td>604.171429</td>
      <td>391.814286</td>
    </tr>
    <tr>
      <th>Bangalore Rural</th>
      <td>2007.0</td>
      <td>0.828571</td>
      <td>2.771429</td>
      <td>32.214286</td>
      <td>40.600000</td>
      <td>116.200000</td>
      <td>96.400000</td>
      <td>113.885714</td>
      <td>123.314286</td>
      <td>149.542857</td>
      <td>150.600000</td>
      <td>59.828571</td>
      <td>9.200000</td>
      <td>895.385714</td>
      <td>483.142857</td>
    </tr>
    <tr>
      <th>Bangalore Urban</th>
      <td>2007.0</td>
      <td>1.842857</td>
      <td>2.242857</td>
      <td>32.800000</td>
      <td>63.500000</td>
      <td>124.171429</td>
      <td>100.457143</td>
      <td>125.628571</td>
      <td>140.085714</td>
      <td>172.342857</td>
      <td>171.014286</td>
      <td>61.785714</td>
      <td>8.800000</td>
      <td>1004.671429</td>
      <td>538.514286</td>
    </tr>
    <tr>
      <th>Belgam</th>
      <td>2007.0</td>
      <td>1.357143</td>
      <td>0.528571</td>
      <td>17.157143</td>
      <td>25.485714</td>
      <td>53.885714</td>
      <td>187.442857</td>
      <td>232.785714</td>
      <td>188.900000</td>
      <td>172.900000</td>
      <td>89.171429</td>
      <td>38.200000</td>
      <td>0.385714</td>
      <td>1008.200000</td>
      <td>782.028571</td>
    </tr>
    <tr>
      <th>Bellary</th>
      <td>2007.0</td>
      <td>3.885714</td>
      <td>2.400000</td>
      <td>21.542857</td>
      <td>20.914286</td>
      <td>66.328571</td>
      <td>78.142857</td>
      <td>73.114286</td>
      <td>108.400000</td>
      <td>154.457143</td>
      <td>103.242857</td>
      <td>43.171429</td>
      <td>1.842857</td>
      <td>677.442857</td>
      <td>414.114286</td>
    </tr>
    <tr>
      <th>Bidar</th>
      <td>2007.0</td>
      <td>5.714286</td>
      <td>7.471429</td>
      <td>27.371429</td>
      <td>25.500000</td>
      <td>32.071429</td>
      <td>113.385714</td>
      <td>192.142857</td>
      <td>189.871429</td>
      <td>201.928571</td>
      <td>74.742857</td>
      <td>13.857143</td>
      <td>1.771429</td>
      <td>885.828571</td>
      <td>697.328571</td>
    </tr>
    <tr>
      <th>Bijapur</th>
      <td>2007.0</td>
      <td>1.900000</td>
      <td>1.542857</td>
      <td>16.585714</td>
      <td>17.557143</td>
      <td>54.885714</td>
      <td>94.300000</td>
      <td>67.857143</td>
      <td>99.528571</td>
      <td>173.171429</td>
      <td>95.014286</td>
      <td>19.028571</td>
      <td>2.614286</td>
      <td>643.985714</td>
      <td>434.857143</td>
    </tr>
    <tr>
      <th>Chamarajanagar</th>
      <td>2007.0</td>
      <td>1.500000</td>
      <td>3.957143</td>
      <td>22.900000</td>
      <td>78.671429</td>
      <td>114.657143</td>
      <td>62.271429</td>
      <td>79.885714</td>
      <td>98.957143</td>
      <td>99.742857</td>
      <td>164.600000</td>
      <td>108.100000</td>
      <td>25.471429</td>
      <td>860.714286</td>
      <td>340.857143</td>
    </tr>
    <tr>
      <th>Chikmagalur</th>
      <td>2007.0</td>
      <td>3.142857</td>
      <td>6.600000</td>
      <td>50.128571</td>
      <td>62.100000</td>
      <td>122.571429</td>
      <td>362.314286</td>
      <td>655.900000</td>
      <td>496.671429</td>
      <td>264.314286</td>
      <td>152.085714</td>
      <td>77.871429</td>
      <td>10.600000</td>
      <td>2264.300000</td>
      <td>1779.200000</td>
    </tr>
    <tr>
      <th>Chitradurga</th>
      <td>2007.0</td>
      <td>2.371429</td>
      <td>3.685714</td>
      <td>19.285714</td>
      <td>39.914286</td>
      <td>102.185714</td>
      <td>63.714286</td>
      <td>92.814286</td>
      <td>108.842857</td>
      <td>123.885714</td>
      <td>105.114286</td>
      <td>61.485714</td>
      <td>4.200000</td>
      <td>727.500000</td>
      <td>389.257143</td>
    </tr>
    <tr>
      <th>Dakshin Kannada</th>
      <td>2007.0</td>
      <td>2.357143</td>
      <td>2.071429</td>
      <td>53.000000</td>
      <td>49.600000</td>
      <td>237.957143</td>
      <td>866.314286</td>
      <td>1094.042857</td>
      <td>739.914286</td>
      <td>465.914286</td>
      <td>241.014286</td>
      <td>136.171429</td>
      <td>17.628571</td>
      <td>3905.985714</td>
      <td>3166.185714</td>
    </tr>
    <tr>
      <th>Davangere</th>
      <td>2007.0</td>
      <td>3.200000</td>
      <td>0.142857</td>
      <td>20.814286</td>
      <td>36.942857</td>
      <td>85.685714</td>
      <td>82.528571</td>
      <td>129.528571</td>
      <td>122.628571</td>
      <td>128.771429</td>
      <td>103.742857</td>
      <td>60.542857</td>
      <td>8.514286</td>
      <td>783.042857</td>
      <td>463.457143</td>
    </tr>
    <tr>
      <th>Dharwad</th>
      <td>2007.0</td>
      <td>2.585714</td>
      <td>0.200000</td>
      <td>17.228571</td>
      <td>46.357143</td>
      <td>71.585714</td>
      <td>118.442857</td>
      <td>147.057143</td>
      <td>129.100000</td>
      <td>154.000000</td>
      <td>71.928571</td>
      <td>52.671429</td>
      <td>6.485714</td>
      <td>817.642857</td>
      <td>548.600000</td>
    </tr>
    <tr>
      <th>Gadag</th>
      <td>2007.0</td>
      <td>1.042857</td>
      <td>1.385714</td>
      <td>30.714286</td>
      <td>30.814286</td>
      <td>78.685714</td>
      <td>102.328571</td>
      <td>81.685714</td>
      <td>101.700000</td>
      <td>131.085714</td>
      <td>89.657143</td>
      <td>49.985714</td>
      <td>9.128571</td>
      <td>708.214286</td>
      <td>416.800000</td>
    </tr>
    <tr>
      <th>Gulbarga</th>
      <td>2007.0</td>
      <td>5.985714</td>
      <td>1.885714</td>
      <td>26.400000</td>
      <td>24.357143</td>
      <td>42.585714</td>
      <td>103.800000</td>
      <td>129.971429</td>
      <td>139.185714</td>
      <td>194.714286</td>
      <td>84.985714</td>
      <td>21.428571</td>
      <td>2.557143</td>
      <td>777.857143</td>
      <td>567.671429</td>
    </tr>
    <tr>
      <th>Hassan</th>
      <td>2007.0</td>
      <td>4.914286</td>
      <td>5.971429</td>
      <td>35.042857</td>
      <td>73.957143</td>
      <td>122.057143</td>
      <td>150.142857</td>
      <td>223.885714</td>
      <td>185.114286</td>
      <td>139.471429</td>
      <td>166.771429</td>
      <td>69.600000</td>
      <td>7.442857</td>
      <td>1184.371429</td>
      <td>698.614286</td>
    </tr>
    <tr>
      <th>Haveri</th>
      <td>2007.0</td>
      <td>1.614286</td>
      <td>0.171429</td>
      <td>21.242857</td>
      <td>40.628571</td>
      <td>83.600000</td>
      <td>115.242857</td>
      <td>180.185714</td>
      <td>150.528571</td>
      <td>113.271429</td>
      <td>81.842857</td>
      <td>49.000000</td>
      <td>6.128571</td>
      <td>843.457143</td>
      <td>559.228571</td>
    </tr>
    <tr>
      <th>Kodagu</th>
      <td>2007.0</td>
      <td>2.885714</td>
      <td>2.957143</td>
      <td>53.271429</td>
      <td>76.000000</td>
      <td>172.328571</td>
      <td>502.214286</td>
      <td>861.442857</td>
      <td>552.757143</td>
      <td>294.628571</td>
      <td>183.614286</td>
      <td>100.257143</td>
      <td>15.485714</td>
      <td>2817.842857</td>
      <td>2211.042857</td>
    </tr>
    <tr>
      <th>Kolar</th>
      <td>2007.0</td>
      <td>0.314286</td>
      <td>5.342857</td>
      <td>23.228571</td>
      <td>33.614286</td>
      <td>110.157143</td>
      <td>89.285714</td>
      <td>103.285714</td>
      <td>102.600000</td>
      <td>165.300000</td>
      <td>114.200000</td>
      <td>77.900000</td>
      <td>14.442857</td>
      <td>839.671429</td>
      <td>460.471429</td>
    </tr>
    <tr>
      <th>Koppal</th>
      <td>2007.0</td>
      <td>1.857143</td>
      <td>0.557143</td>
      <td>26.885714</td>
      <td>21.271429</td>
      <td>66.100000</td>
      <td>90.885714</td>
      <td>75.057143</td>
      <td>105.428571</td>
      <td>158.785714</td>
      <td>94.028571</td>
      <td>32.900000</td>
      <td>3.300000</td>
      <td>677.057143</td>
      <td>430.157143</td>
    </tr>
    <tr>
      <th>Mandya</th>
      <td>2007.0</td>
      <td>4.857143</td>
      <td>3.871429</td>
      <td>33.428571</td>
      <td>52.085714</td>
      <td>112.300000</td>
      <td>76.171429</td>
      <td>71.057143</td>
      <td>99.971429</td>
      <td>108.814286</td>
      <td>156.785714</td>
      <td>67.200000</td>
      <td>5.914286</td>
      <td>792.457143</td>
      <td>356.014286</td>
    </tr>
    <tr>
      <th>Mysore</th>
      <td>2007.0</td>
      <td>1.671429</td>
      <td>2.014286</td>
      <td>35.100000</td>
      <td>67.400000</td>
      <td>104.800000</td>
      <td>80.785714</td>
      <td>113.742857</td>
      <td>105.285714</td>
      <td>91.314286</td>
      <td>141.814286</td>
      <td>81.257143</td>
      <td>6.671429</td>
      <td>831.857143</td>
      <td>391.128571</td>
    </tr>
    <tr>
      <th>Raichur</th>
      <td>2007.0</td>
      <td>4.028571</td>
      <td>1.542857</td>
      <td>27.900000</td>
      <td>17.542857</td>
      <td>46.185714</td>
      <td>89.571429</td>
      <td>77.385714</td>
      <td>98.057143</td>
      <td>156.257143</td>
      <td>165.042857</td>
      <td>23.985714</td>
      <td>1.271429</td>
      <td>708.771429</td>
      <td>421.271429</td>
    </tr>
    <tr>
      <th>Shimoga</th>
      <td>2007.0</td>
      <td>2.614286</td>
      <td>1.828571</td>
      <td>26.714286</td>
      <td>35.714286</td>
      <td>82.171429</td>
      <td>398.242857</td>
      <td>699.600000</td>
      <td>487.457143</td>
      <td>236.671429</td>
      <td>116.214286</td>
      <td>55.185714</td>
      <td>4.285714</td>
      <td>2146.700000</td>
      <td>1821.971429</td>
    </tr>
    <tr>
      <th>Tumkur</th>
      <td>2007.0</td>
      <td>3.100000</td>
      <td>6.828571</td>
      <td>31.742857</td>
      <td>42.457143</td>
      <td>115.800000</td>
      <td>78.214286</td>
      <td>107.400000</td>
      <td>127.957143</td>
      <td>130.214286</td>
      <td>134.657143</td>
      <td>64.500000</td>
      <td>2.342857</td>
      <td>845.214286</td>
      <td>443.785714</td>
    </tr>
    <tr>
      <th>Udupi</th>
      <td>2007.0</td>
      <td>2.542857</td>
      <td>1.928571</td>
      <td>42.514286</td>
      <td>30.985714</td>
      <td>199.485714</td>
      <td>1043.671429</td>
      <td>1312.057143</td>
      <td>899.114286</td>
      <td>578.800000</td>
      <td>251.500000</td>
      <td>110.571429</td>
      <td>8.700000</td>
      <td>4481.871429</td>
      <td>3833.642857</td>
    </tr>
    <tr>
      <th>Uttar Kannada</th>
      <td>2007.0</td>
      <td>1.514286</td>
      <td>0.814286</td>
      <td>19.257143</td>
      <td>27.985714</td>
      <td>126.271429</td>
      <td>677.728571</td>
      <td>930.371429</td>
      <td>670.014286</td>
      <td>397.485714</td>
      <td>164.142857</td>
      <td>61.985714</td>
      <td>2.985714</td>
      <td>3080.557143</td>
      <td>2675.600000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#district wise grouping of mean annual and monsoon rainfall values using groupby() method
df_Rain[["Annual Total","Monsoon","District"]].groupby('District').mean()
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
      <th>Annual Total</th>
      <th>Monsoon</th>
    </tr>
    <tr>
      <th>District</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bagalkote</th>
      <td>604.171429</td>
      <td>391.814286</td>
    </tr>
    <tr>
      <th>Bangalore Rural</th>
      <td>895.385714</td>
      <td>483.142857</td>
    </tr>
    <tr>
      <th>Bangalore Urban</th>
      <td>1004.671429</td>
      <td>538.514286</td>
    </tr>
    <tr>
      <th>Belgam</th>
      <td>1008.200000</td>
      <td>782.028571</td>
    </tr>
    <tr>
      <th>Bellary</th>
      <td>677.442857</td>
      <td>414.114286</td>
    </tr>
    <tr>
      <th>Bidar</th>
      <td>885.828571</td>
      <td>697.328571</td>
    </tr>
    <tr>
      <th>Bijapur</th>
      <td>643.985714</td>
      <td>434.857143</td>
    </tr>
    <tr>
      <th>Chamarajanagar</th>
      <td>860.714286</td>
      <td>340.857143</td>
    </tr>
    <tr>
      <th>Chikmagalur</th>
      <td>2264.300000</td>
      <td>1779.200000</td>
    </tr>
    <tr>
      <th>Chitradurga</th>
      <td>727.500000</td>
      <td>389.257143</td>
    </tr>
    <tr>
      <th>Dakshin Kannada</th>
      <td>3905.985714</td>
      <td>3166.185714</td>
    </tr>
    <tr>
      <th>Davangere</th>
      <td>783.042857</td>
      <td>463.457143</td>
    </tr>
    <tr>
      <th>Dharwad</th>
      <td>817.642857</td>
      <td>548.600000</td>
    </tr>
    <tr>
      <th>Gadag</th>
      <td>708.214286</td>
      <td>416.800000</td>
    </tr>
    <tr>
      <th>Gulbarga</th>
      <td>777.857143</td>
      <td>567.671429</td>
    </tr>
    <tr>
      <th>Hassan</th>
      <td>1184.371429</td>
      <td>698.614286</td>
    </tr>
    <tr>
      <th>Haveri</th>
      <td>843.457143</td>
      <td>559.228571</td>
    </tr>
    <tr>
      <th>Kodagu</th>
      <td>2817.842857</td>
      <td>2211.042857</td>
    </tr>
    <tr>
      <th>Kolar</th>
      <td>839.671429</td>
      <td>460.471429</td>
    </tr>
    <tr>
      <th>Koppal</th>
      <td>677.057143</td>
      <td>430.157143</td>
    </tr>
    <tr>
      <th>Mandya</th>
      <td>792.457143</td>
      <td>356.014286</td>
    </tr>
    <tr>
      <th>Mysore</th>
      <td>831.857143</td>
      <td>391.128571</td>
    </tr>
    <tr>
      <th>Raichur</th>
      <td>708.771429</td>
      <td>421.271429</td>
    </tr>
    <tr>
      <th>Shimoga</th>
      <td>2146.700000</td>
      <td>1821.971429</td>
    </tr>
    <tr>
      <th>Tumkur</th>
      <td>845.214286</td>
      <td>443.785714</td>
    </tr>
    <tr>
      <th>Udupi</th>
      <td>4481.871429</td>
      <td>3833.642857</td>
    </tr>
    <tr>
      <th>Uttar Kannada</th>
      <td>3080.557143</td>
      <td>2675.600000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_GD1
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
    </tr>
    <tr>
      <th>Day</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>01-01-2005</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.473</td>
      <td>O</td>
    </tr>
    <tr>
      <th>02-01-2005</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.270</td>
      <td>C</td>
    </tr>
    <tr>
      <th>03-01-2005</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.033</td>
      <td>O</td>
    </tr>
    <tr>
      <th>04-01-2005</th>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.476</td>
      <td>O</td>
    </tr>
    <tr>
      <th>05-01-2005</th>
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
    </tr>
    <tr>
      <th>27-12-2015</th>
      <td>HHS</td>
      <td>258.040</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28-12-2015</th>
      <td>HZS</td>
      <td>3.040</td>
      <td>55.259</td>
      <td>O</td>
    </tr>
    <tr>
      <th>29-12-2015</th>
      <td>HZS</td>
      <td>3.005</td>
      <td>51.204</td>
      <td>O</td>
    </tr>
    <tr>
      <th>30-12-2015</th>
      <td>HZS</td>
      <td>3.000</td>
      <td>50.639</td>
      <td>O</td>
    </tr>
    <tr>
      <th>31-12-2015</th>
      <td>HZS</td>
      <td>2.905</td>
      <td>41.459</td>
      <td>O</td>
    </tr>
  </tbody>
</table>
<p>4017 rows × 4 columns</p>
</div>




```python
#defining a user defined function for converting cumecs to cusecs
def cumecs_to_cusecs(cumecs):
    cusecs=cumecs*35.315
    return cusecs
```


```python
#applying a user defined function to a column of Pandas DataFrame with apply()method
df_GD1['Discharge (cusecs)']=df_GD1['Discharge (cumecs)'].apply(cumecs_to_cusecs)
```


```python
df_GD1
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
      <th>Datatype</th>
      <th>Gauge(m)</th>
      <th>Discharge (cumecs)</th>
      <th>Observed/Computed</th>
      <th>Discharge (cusecs)</th>
    </tr>
    <tr>
      <th>Day</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>01-01-2005</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.473</td>
      <td>O</td>
      <td>1923.713995</td>
    </tr>
    <tr>
      <th>02-01-2005</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.270</td>
      <td>C</td>
      <td>1916.545050</td>
    </tr>
    <tr>
      <th>03-01-2005</th>
      <td>HZS</td>
      <td>2.990</td>
      <td>54.033</td>
      <td>O</td>
      <td>1908.175395</td>
    </tr>
    <tr>
      <th>04-01-2005</th>
      <td>HZS</td>
      <td>3.000</td>
      <td>55.476</td>
      <td>O</td>
      <td>1959.134940</td>
    </tr>
    <tr>
      <th>05-01-2005</th>
      <td>HZS</td>
      <td>3.020</td>
      <td>58.202</td>
      <td>O</td>
      <td>2055.403630</td>
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
      <th>27-12-2015</th>
      <td>HHS</td>
      <td>258.040</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28-12-2015</th>
      <td>HZS</td>
      <td>3.040</td>
      <td>55.259</td>
      <td>O</td>
      <td>1951.471585</td>
    </tr>
    <tr>
      <th>29-12-2015</th>
      <td>HZS</td>
      <td>3.005</td>
      <td>51.204</td>
      <td>O</td>
      <td>1808.269260</td>
    </tr>
    <tr>
      <th>30-12-2015</th>
      <td>HZS</td>
      <td>3.000</td>
      <td>50.639</td>
      <td>O</td>
      <td>1788.316285</td>
    </tr>
    <tr>
      <th>31-12-2015</th>
      <td>HZS</td>
      <td>2.905</td>
      <td>41.459</td>
      <td>O</td>
      <td>1464.124585</td>
    </tr>
  </tbody>
</table>
<p>4017 rows × 5 columns</p>
</div>




```python
#missing values in the form of NaN are not considered for calculation of group statistics
df_GD1['Discharge (cusecs)'].mean()
```




    7556.724519507041




```python

```


<iframe width="560" height="315" src="https://www.youtube.com/embed/l3Hc7lS51zY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Lecture Slides

[Download Session7_Working_with_Pandas_1.pdf](pdfs/Session7_Working_with_Pandas_1.pdf)
