
# Tidyverse for Spatial Data

The Tidyverse approach makes data cleaning and preparation intuitive, even for spatial attributes.

## Using dplyr with sf

```r
library(sf)
library(dplyr)

nc <- st_read(system.file("shape/nc.shp", package="sf"))

# Filter counties with more than 10,000 births
large_counties <- nc %>%
  filter(BIR74 > 10000) %>%
  select(NAME, BIR74, geometry)

plot(large_counties["BIR74"])
```

## Data Summarization

```r
# Calculate total births by geometry (if grouped)
nc %>%
  summarize(Total_Births = sum(BIR74))
```

## Visualization with ggplot2

```r
library(ggplot2)

ggplot(data = nc) +
  geom_sf(aes(fill = BIR74)) +
  scale_fill_viridis_c() +
  theme_minimal() +
  labs(title = "Birth Statistics", subtitle = "North Carolina 1974")
```
