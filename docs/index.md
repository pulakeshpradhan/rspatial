
# Coding Muscle with GeoPython

Welcome to **Coding Muscle with GeoPython**. This comprehensive learning resource is vetted by the **National Water Academy (NWA)** and designed to bridge the gap between traditional GIS workflows and modern, programmatic geospatial analysis.

## Foundation: Data Science Stack

Before diving into maps, we master the core tools that power modern data science.

* <a href="https://numpy.org/" target="_blank"><img src="https://numpy.org/images/logo.svg" style="width: 50px; height: 50px; object-fit: contain; vertical-align: middle; margin-right: 15px;" alt="NumPy"></a> **NumPy** ("The Math Engine")

    Python lists are slow for millions of numbers. NumPy makes math instant. It handles the heavy lifting for all other data packages.

    ```python
    import numpy as np
    # Create an array and calculate mean
    data = np.array([1, 2, 3, 4, 5])
    print(data.mean())
    ```

* <a href="https://pandas.pydata.org/" target="_blank"><img src="https://pandas.pydata.org/static/img/pandas.svg" style="width: 50px; height: 50px; object-fit: contain; vertical-align: middle; margin-right: 15px;" alt="Pandas"></a> **Pandas** ("The Super Spreadsheet")

    Imagine Excel, but programmable and capable of handling millions of rows in seconds. Pandas lets you filter, sort, and analyze tabular data with ease.

    ```python
    import pandas as pd
    # Read a CSV file
    df = pd.read_csv("data.csv")
    print(df.head())
    ```

* <a href="https://matplotlib.org/" target="_blank"><img src="https://matplotlib.org/stable/_static/logo2.svg" style="width: 50px; height: 50px; object-fit: contain; vertical-align: middle; margin-right: 15px;" alt="Matplotlib"></a> **Matplotlib** ("The Artists")

    These libraries turn your numbers into visual stories—line charts, bar graphs, heatmaps, and more.

    ```python
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()
    ```

## Applied Geospatial Modules

Once the foundation is set, we apply these skills to specialized geospatial domains using our grid of advanced modules.

<div class="grid-container">

<div class="card">
  <div class="card-icon-wrapper">
    <img src="https://geopandas.org/en/stable/_static/geopandas_logo_web.svg" alt="Vector Data">
  </div>
  <h3>Vector Analysis</h3>
  <p class="subtitle"><strong>GeoPandas</strong></p>
  <p>Master the manipulation of geometric data (Points, Lines, Polygons).</p>

```python
import geopandas as gpd
gdf = gpd.read_file("map.shp")
gdf.plot()
```

</div>

<div class="card">
  <div class="card-icon-wrapper">
    <img src="https://avatars.githubusercontent.com/u/46967650?v=4" alt="Raster Data">
  </div>
  <h3>Raster Processing</h3>
  <p class="subtitle"><strong>Rasterio & Xarray</strong></p>
  <p>Unlock the power of pixel-based data (Satellite imagery, DEMs).</p>

```python
import rasterio
import matplotlib.pyplot as plt
src = rasterio.open("image.tif")
plt.imshow(src.read(1))
plt.show()
```

</div>

<div class="card">
  <div class="card-icon-wrapper">
    <img src="https://pandas.pydata.org/static/img/pandas.svg" alt="Time Series">
  </div>
  <h3>Time Series</h3>
  <p class="subtitle"><strong>Advanced Pandas</strong></p>
  <p>Handle temporal data with precision for meteorological trends.</p>

```python
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.resample('M').mean()
```

</div>

<div class="card">
  <div class="card-icon-wrapper">
    <img src="https://jupyter.org/assets/homepage/main-logo.svg" alt="Cloud & Web API">
  </div>
  <h3>Web APIs & Cloud</h3>
  <p class="subtitle"><strong>Jupyter & APIs</strong></p>
  <p>Connect to live APIs like OpenWeatherMap.</p>

```python
import requests
res = requests.get(api_url)
data = res.json()
```

</div>

</div>

## Acknowledgement

We define our sincere gratitude to **National Water Academy (NWA), Pune** for providing the content, expertise, and resources that made this tutorial possible.
