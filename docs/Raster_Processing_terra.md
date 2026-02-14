
# Raster Processing with R (terra)

The `terra` package is the successor to the older `raster` package, providing faster performance for gridded spatial data.

## Loading and Visualizing Rasters

```r
library(terra)

# Create a sample raster
r <- rast(nrows=10, ncols=10, xmin=0, xmax=10, ymin=0, ymax=10)
values(r) <- 1:100

# Plotting
plot(r, main="Simple Raster")
```

## Raster Algebra

```r
# Multi-band operations
r2 <- r * 2
r_sum <- r + r2

# Thresholding
mask <- r > 50
plot(mask)
```

## Crop and Mask

```r
# Define an extent
e <- ext(2, 5, 2, 5)

# Crop raster
r_cropped <- crop(r, e)
plot(r_cropped)
```
