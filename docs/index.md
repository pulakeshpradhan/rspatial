
# Coding Muscle with R Geospatial

Welcome to **Coding Muscle with R Geospatial**. This comprehensive learning resource is designed to bridge the gap between traditional GIS workflows and modern, programmatic geospatial analysis using the R programming language.

## Foundation: Data Science Stack

Before diving into maps, we master the core tools that power modern data science in R.

* <a href="https://www.r-project.org/" target="_blank"><img src="https://www.r-project.org/logo/Rlogo.svg" style="width: 50px; height: 50px; object-fit: contain; vertical-align: middle; margin-right: 15px;" alt="R"></a> **Base R** ("The Foundation")

    R is built for statistics. Its vectors and matrices are native, making mathematical operations intuitive and fast.

    ```r
    # Create a vector and calculate mean
    data <- c(1, 2, 3, 4, 5)
    mean(data)
    ```

* <a href="https://www.tidyverse.org/" target="_blank"><img src="https://tidyverse.tidyverse.org/logo.png" style="width: 50px; height: 50px; object-fit: contain; vertical-align: middle; margin-right: 15px;" alt="Tidyverse"></a> **Tidyverse** ("The Data Engine")

    A collection of R packages designed for data science. Packages like `dplyr` and `tidyr` let you filter, sort, and analyze tabular data with a readable syntax.

    ```r
    library(dplyr)
    # Read and filter data
    df <- read.csv("data.csv") %>%
      filter(value > 10) %>%
      head()
    ```

* <a href="https://ggplot2.tidyverse.org/" target="_blank"><img src="https://ggplot2.tidyverse.org/logo.png" style="width: 50px; height: 50px; object-fit: contain; vertical-align: middle; margin-right: 15px;" alt="ggplot2"></a> **ggplot2** ("The Grammar of Graphics")

    A powerful system for creating elegant data visualizations based on the Grammar of Graphics.

    ```r
    library(ggplot2)
    ggplot(mtcars, aes(x=wt, y=mpg)) + 
      geom_point() + 
      geom_smooth()
    ```

## Applied Geospatial Modules

Once the foundation is set, we apply these skills to specialized geospatial domains using our grid of advanced modules.

<div class="grid-container">

<div class="card">
  <div class="card-icon-wrapper">
    <img src="https://r-spatial.github.io/sf/reference/figures/logo.png" alt="Vector Data">
  </div>
  <h3>Vector Analysis</h3>
  <p class="subtitle"><strong>sf (Simple Features)</strong></p>
  <p>Master the manipulation of geometric data using tidy principles.</p>

```r
library(sf)
nc <- st_read(system.file("shape/nc.shp", package="sf"))
plot(st_geometry(nc))
```

</div>

<div class="card">
  <div class="card-icon-wrapper">
    <img src="https://rspatial.github.io/terra/reference/figures/logo.png" alt="Raster Data">
  </div>
  <h3>Raster Processing</h3>
  <p class="subtitle"><strong>terra & stars</strong></p>
  <p>Unlock the power of pixel-based data (Satellite imagery, DEMs).</p>

```r
library(terra)
r <- rast("image.tif")
plot(r)
```

</div>

<div class="card">
  <div class="card-icon-wrapper">
    <img src="https://tidyverse.tidyverse.tidyverse.org/logo.png" alt="Time Series">
  </div>
  <h3>Time Series</h3>
  <p class="subtitle"><strong>tsibble & lubridate</strong></p>
  <p>Handle temporal data with precision for meteorological trends.</p>

```r
library(lubridate)
df$date <- ymd(df$date_string)
# Monthly aggregate
df %>% group_by(month = month(date)) %>% summarize(mean(val))
```

</div>

<div class="card">
  <div class="card-icon-wrapper">
    <img src="https://www.r-project.org/logo/Rlogo.svg" alt="Cloud & Web API">
  </div>
  <h3>Web APIs & Cloud</h3>
  <p class="subtitle"><strong>httr & jsonlite</strong></p>
  <p>Connect to live APIs like OpenWeatherMap.</p>

```r
library(httr)
res <- GET(api_url)
data <- content(res, "parsed")
```

</div>

</div>
