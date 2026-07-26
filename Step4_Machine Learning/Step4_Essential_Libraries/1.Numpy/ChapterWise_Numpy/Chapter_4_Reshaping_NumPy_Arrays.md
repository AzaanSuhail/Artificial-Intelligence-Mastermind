# Chapter 4: Reshaping NumPy Arrays

> **Goal:** Learn how to change the shape of NumPy arrays without
> changing their data.

------------------------------------------------------------------------

# Learning Objectives

After this chapter, you will be able to:

-   Understand `reshape()`
-   Understand `resize()`
-   Understand `flatten()`
-   Understand `ravel()`
-   Understand `transpose()` and `.T`
-   Use `-1` in `reshape()`
-   Explain memory sharing vs copying
-   Solve common interview questions

------------------------------------------------------------------------

# 1. Why Reshape Arrays?

Machine learning, deep learning, image processing, and data analysis
often require data in a specific shape.

Example:

``` python
import numpy as np

a = np.arange(1, 13)
print(a)
```

Output:

``` text
[ 1  2  3  4  5  6  7  8  9 10 11 12]
```

This is a **1D** array.

------------------------------------------------------------------------

# 2. `reshape()`

Changes the shape **without changing the data**.

``` python
a = np.arange(1, 13)

b = a.reshape(3, 4)

print(b)
```

Output:

``` text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```

Shape:

``` python
print(b.shape)
# (3, 4)
```

------------------------------------------------------------------------

# Golden Rule

The number of elements **must remain the same**.

``` text
Old size = New size
```

Example:

``` text
12 elements

Possible:
(2,6)
(3,4)
(2,2,3)
(1,12)
(12,1)

Not Possible:
(5,3) -> needs 15 elements
```

------------------------------------------------------------------------

# 3. Reshape into Higher Dimensions

## 1D → 2D

``` python
a = np.arange(6)
print(a.reshape(2,3))
```

## 1D → 3D

``` python
a = np.arange(24)
print(a.reshape(2,3,4))
```

Shape:

``` text
(2,3,4)
```

Interpretation:

-   2 matrices
-   3 rows
-   4 columns

------------------------------------------------------------------------

# 4. Using `-1`

NumPy automatically calculates one missing dimension.

``` python
a = np.arange(12)

b = a.reshape(3,-1)

print(b.shape)
```

Output:

``` text
(3,4)
```

Another example:

``` python
a.reshape(-1,2)
```

Output:

``` text
(6,2)
```

Only **one** `-1` is allowed.

------------------------------------------------------------------------

# 5. `resize()`

Unlike `reshape()`, `resize()` can change the number of elements.

``` python
a = np.array([1,2,3,4])

b = np.resize(a, (3,3))

print(b)
```

Output:

``` text
[[1 2 3]
 [4 1 2]
 [3 4 1]]
```

If the new array is larger, NumPy repeats values.

------------------------------------------------------------------------

# 6. `flatten()`

Returns a **copy** of the array as a 1D array.

``` python
a = np.array([[1,2],[3,4]])

b = a.flatten()

print(b)
```

Output:

``` text
[1 2 3 4]
```

Changing `b` does **not** change `a`.

------------------------------------------------------------------------

# 7. `ravel()`

Returns a flattened **view whenever possible**.

``` python
a = np.array([[1,2],[3,4]])

b = a.ravel()
```

Changing `b` usually changes `a` because they share memory.

------------------------------------------------------------------------

# `flatten()` vs `ravel()`

  Feature         flatten()   ravel()
  --------------- ----------- --------------------
  Returns         Copy        View (if possible)
  Shares Memory   No          Usually Yes
  Faster          No          Yes

Example:

``` python
a = np.array([[1,2],[3,4]])

b = a.ravel()
b[0] = 99

print(a)
```

Output:

``` text
[[99  2]
 [ 3  4]]
```

------------------------------------------------------------------------

# 8. `transpose()`

Swaps rows and columns.

``` python
a = np.array([
    [1,2,3],
    [4,5,6]
])

print(a.transpose())
```

Output:

``` text
[[1 4]
 [2 5]
 [3 6]]
```

Shortcut:

``` python
print(a.T)
```

Both produce the same result.

------------------------------------------------------------------------

# 9. Memory Sharing

``` python
a = np.arange(6)

b = a.reshape(2,3)
```

Normally, `b` shares memory with `a`.

``` python
b[0,0] = 100

print(a)
```

Output:

``` text
[100   1   2   3   4   5]
```

------------------------------------------------------------------------

# Common Errors

## Invalid reshape

``` python
np.arange(10).reshape(3,4)
```

Error:

``` text
ValueError
```

Reason:

10 elements cannot become 12 elements.

------------------------------------------------------------------------

# Interview Questions

### Q1

Difference between `reshape()` and `resize()`?

-   `reshape()` keeps the same number of elements.
-   `resize()` can increase or decrease elements.

### Q2

Difference between `flatten()` and `ravel()`?

-   `flatten()` returns a copy.
-   `ravel()` returns a view when possible.

### Q3

Can `reshape()` fail?

Yes, when the total number of elements does not match.

### Q4

Why use `-1`?

To let NumPy calculate one dimension automatically.

------------------------------------------------------------------------

# Practice Questions

1.  Convert a `(12,)` array into `(3,4)`.
2.  Convert a `(24,)` array into `(2,3,4)`.
3.  Use `reshape(-1,4)`.
4.  Explain why `reshape(5,5)` fails for a 24-element array.
5.  Compare `flatten()` and `ravel()`.
6.  Demonstrate `transpose()`.
7.  Show that `reshape()` shares memory.

------------------------------------------------------------------------

# Cheat Sheet

``` python
import numpy as np

a = np.arange(12)

a.reshape(3,4)
a.reshape(2,2,3)
a.reshape(-1,4)

np.resize(a, (4,4))

a.flatten()
a.ravel()

a.T
a.transpose()
```

  Function        Purpose
  --------------- -----------------------
  `reshape()`     Change shape
  `resize()`      Resize array
  `flatten()`     1D copy
  `ravel()`       1D view (if possible)
  `.T`            Transpose
  `transpose()`   Swap axes

**Next Chapter:** Indexing and Slicing in NumPy
