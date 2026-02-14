
# Data Structures in R

## Vectors

Vectors are the most basic data structure in R. They must contain elements of the same type.

```r
# Atomic vector
rain <- c(10, 20, 15, 30)
names(rain) <- c("Mon", "Tue", "Wed", "Thu")
rain
```

## Lists

Lists can contain elements of different types, including other lists.

```r
station_info <- list(
  name = "Pune",
  coords = c(18.52, 73.85),
  active = TRUE
)
station_info$name
```

## Data Frames

Data frames are the standard for tabular data in R. They are like a list of vectors of equal length.

```r
df <- data.frame(
  station = c("Pune", "Mumbai", "Delhi"),
  rainfall = c(100, 250, 80)
)
summary(df)
```

## Matrices

Matrices are two-dimensional arrays where all elements must be of the same type.

```r
m <- matrix(1:9, nrow=3)
m[1, 2] # Row 1, Col 2
```

## Factors

Factors are used to represent categorical data.

```r
land_use <- factor(c("Urban", "Forest", "Water", "Urban"))
levels(land_use)
```
