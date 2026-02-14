
# Basic Data Types in R

## Characters (Strings)

In R, strings are called "characters".

```r
x <- '2'
```

```r
class(x)
```

[1] "character"

```r
y <- "Hello World"
```

```r
class(y)
```

[1] "character"

### String Length

Unlike Python's `len()`, R uses `nchar()` for the number of characters in a string.

```r
nchar("Hello World")
```

[1] 11

### String Indexing

R is **1-indexed**. To get a substring, use `substr()`.

```r
# Get the first character
substr(y, 1, 1)
```

[1] "H"

```r
# Get characters from 7 to 11
substr(y, 7, 11)
```

[1] "World"

### String Concatenation

R uses `paste()` or `paste0()` for concatenation.

```r
first_name <- 'Madhya'
last_name <- 'Pradesh'
full_name <- paste(first_name, last_name)
full_name
```

[1] "Madhya Pradesh"

## Numeric and Integer

R handles numbers as `numeric` (double precision) by default.

```r
a <- 2
class(a)
```

[1] "numeric"

```r
# Explicit integer
b <- 2L
class(b)
```

[1] "integer"

### Type Conversion

```r
x <- "2"
as.numeric(x)
```

[1] 2

```r
as.character(2.5)
```

[1] "2.5"

## Logical (Booleans)

R uses `TRUE` and `FALSE` (or `T` and `F`).

```r
is_water <- TRUE
class(is_water)
```

[1] "logical"

## Character Methods

R has several built-in functions for string manipulation.

```r
toupper("hello")
```

[1] "HELLO"

```r
tolower("WORLD")
```

[1] "world"

```r
# Trim whitespace
trimws("   Pune   ")
```

[1] "Pune"

```r
# Replace
gsub("Jal Shakti", "Jalshakti", "Ministry of Jal Shakti")
```

[1] "Ministry of Jalshakti"
