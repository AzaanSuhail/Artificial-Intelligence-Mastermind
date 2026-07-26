# Chapter 10: Statistical Functions in NumPy

> **Goal:** Learn how to summarize, analyze, and interpret numerical
> data using NumPy's statistical functions.

------------------------------------------------------------------------

# Learning Objectives

After this chapter, you will be able to:

-   Calculate sums, averages, and products
-   Find minimum and maximum values
-   Compute median, variance, and standard deviation
-   Work with percentiles and quantiles
-   Find element positions using `argmin()` and `argmax()`
-   Calculate covariance and correlation
-   Handle missing values using NaN-aware functions
-   Perform row-wise and column-wise statistics

------------------------------------------------------------------------

# 1. Why Statistical Functions?

Statistics help summarize large datasets.

Example:

``` python
import numpy as np

scores = np.array([78, 85, 91, 88, 95])
```

------------------------------------------------------------------------

# 2. Sum

``` python
print(np.sum(scores))
```

Output:

``` text
437
```

------------------------------------------------------------------------

# 3. Mean (Average)

``` python
print(np.mean(scores))
```

Output:

``` text
87.4
```

Formula:

``` text
Mean = Sum of values / Number of values
```

------------------------------------------------------------------------

# 4. Median

Middle value after sorting.

``` python
print(np.median(scores))
```

Output:

``` text
88.0
```

------------------------------------------------------------------------

# 5. Minimum and Maximum

``` python
print(np.min(scores))
print(np.max(scores))
```

Output:

``` text
78
95
```

------------------------------------------------------------------------

# 6. Index of Minimum and Maximum

``` python
print(np.argmin(scores))
print(np.argmax(scores))
```

Output:

``` text
0
4
```

------------------------------------------------------------------------

# 7. Product

``` python
a = np.array([2,3,4])

print(np.prod(a))
```

Output:

``` text
24
```

------------------------------------------------------------------------

# 8. Standard Deviation

Measures how spread out the data is.

``` python
print(np.std(scores))
```

A small standard deviation means values are close to the mean.

------------------------------------------------------------------------

# 9. Variance

``` python
print(np.var(scores))
```

Variance is the square of the standard deviation.

------------------------------------------------------------------------

# 10. Percentiles

``` python
a = np.array([10,20,30,40,50])

print(np.percentile(a, 25))
print(np.percentile(a, 50))
print(np.percentile(a, 75))
```

The 50th percentile equals the median.

------------------------------------------------------------------------

# 11. Quantiles

``` python
print(np.quantile(a, 0.25))
print(np.quantile(a, 0.50))
print(np.quantile(a, 0.75))
```

Relationship:

``` text
25%  = 0.25
50%  = 0.50
75%  = 0.75
```

------------------------------------------------------------------------

# 12. Row-wise and Column-wise Statistics

``` python
arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))
```

-   `axis=0` → column-wise
-   `axis=1` → row-wise

------------------------------------------------------------------------

# 13. Covariance

Shows how two variables change together.

``` python
x = np.array([1,2,3,4])
y = np.array([2,4,6,8])

print(np.cov(x,y))
```

Returns the covariance matrix.

------------------------------------------------------------------------

# 14. Correlation Coefficient

Measures the strength of a linear relationship.

``` python
print(np.corrcoef(x,y))
```

Interpretation:

    Value Meaning
  ------- ------------------------------
        1 Perfect positive correlation
        0 No linear correlation
       -1 Perfect negative correlation

------------------------------------------------------------------------

# 15. Handling Missing Values (NaN)

``` python
a = np.array([10,20,np.nan,40])

print(np.nanmean(a))
print(np.nansum(a))
print(np.nanmax(a))
```

Useful functions:

-   `np.nanmean()`
-   `np.nansum()`
-   `np.nanmin()`
-   `np.nanmax()`
-   `np.nanstd()`
-   `np.nanvar()`

------------------------------------------------------------------------

# Common Mistakes

❌ Confusing `mean` with `median`.

-   Mean uses all values.
-   Median is the middle value.

❌ Ignoring NaN values.

Regular functions often return `nan` if the array contains missing
values.

Use the `nan*` functions instead.

------------------------------------------------------------------------

# Interview Questions

### Q1

Difference between mean and median?

-   Mean = arithmetic average.
-   Median = middle value after sorting.

### Q2

Difference between variance and standard deviation?

-   Variance = squared spread.
-   Standard deviation = square root of variance.

### Q3

Difference between `max()` and `argmax()`?

-   `max()` returns the value.
-   `argmax()` returns its index.

### Q4

When should you use `nanmean()`?

When the dataset contains missing (`NaN`) values.

------------------------------------------------------------------------

# Practice Questions

1.  Find the mean of an array.
2.  Find the median.
3.  Compute variance and standard deviation.
4.  Find the largest value and its index.
5.  Calculate the 90th percentile.
6.  Compute row-wise averages.
7.  Compute column-wise sums.
8.  Calculate correlation between two arrays.
9.  Handle missing values using `nanmean()`.

------------------------------------------------------------------------

# Cheat Sheet

``` python
np.sum(a)
np.mean(a)
np.median(a)
np.min(a)
np.max(a)
np.argmin(a)
np.argmax(a)
np.prod(a)

np.std(a)
np.var(a)

np.percentile(a, 50)
np.quantile(a, 0.5)

np.cov(x, y)
np.corrcoef(x, y)

np.nanmean(a)
np.nansum(a)
np.nanmax(a)
```

  Function         Purpose
  ---------------- --------------------
  `sum()`          Sum
  `mean()`         Average
  `median()`       Middle value
  `std()`          Standard deviation
  `var()`          Variance
  `argmax()`       Index of maximum
  `percentile()`   Percentiles
  `corrcoef()`     Correlation
  `cov()`          Covariance
  `nanmean()`      Mean ignoring NaN

**Next Chapter:** Sorting, Searching, and Filtering Arrays
