
# Vector Analysis with R (sf)

The `sf` (Simple Features) package is the modern standard for handling vector data in R. It treats spatial data as a data frame with a list-column for geometry.

## Loading Data

```r
library(sf)

# Load a built-in shapefile (North Carolina counties)
nc <- st_read(system.file("shape/nc.shp", package="sf"))

# Print first few rows
head(nc)
```

## Basic Plotting

```r
# Plot specific attribute
plot(nc["BIR74"], main = "Births in 1974")

# Plot only geometry
plot(st_geometry(nc))
```

## Spatial Operations

### Coordinate Reference Systems (CRS)

```r
# Check CRS
st_crs(nc)

# Transform to a different projection (e.g., Web Mercator)
nc_3857 <- st_transform(nc, 3857)
```

### Buffering and Intersections

```r
# Create a 10km buffer around the first county
nc_buf <- st_buffer(nc[1, ], dist = 10000)

# Intersection test
overlap <- st_intersects(nc_buf, nc)
```
