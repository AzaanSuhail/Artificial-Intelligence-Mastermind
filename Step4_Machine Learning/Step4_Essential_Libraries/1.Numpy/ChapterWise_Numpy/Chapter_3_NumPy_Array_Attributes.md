# Chapter 3: NumPy Array Attributes

> **Goal:** Learn how to inspect and understand any NumPy array using
> its attributes.

------------------------------------------------------------------------

# Learning Objectives

After this chapter, you will be able to:

-   Understand `ndim`
-   Understand `shape`
-   Understand `size`
-   Understand `dtype`
-   Understand `itemsize`
-   Understand `nbytes`
-   Use these attributes to debug arrays
-   Answer common interview questions

------------------------------------------------------------------------

# What Are Array Attributes?

Array attributes describe an array. They tell us:

-   How many dimensions it has
-   How many elements it contains
-   What type of data it stores
-   How much memory it uses

Example:

``` python
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
```

------------------------------------------------------------------------

# 1. `ndim`

Returns the number of dimensions (axes).

## 1D

``` python
a = np.array([1,2,3])
print(a.ndim)
```

Output:

``` text
1
```

## 2D

``` python
a = np.array([[1,2],[3,4]])
print(a.ndim)
```

Output:

``` text
2
```

## 3D

``` python
a = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print(a.ndim)
```

Output:

``` text
3
```

Rule:

-   Line → 1D
-   Table → 2D
-   Stack of tables → 3D

------------------------------------------------------------------------

# 2. `shape`

Returns the size of every dimension as a tuple.

``` python
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
```

Output:

``` text
(2, 3)
```

Meaning:

-   2 rows
-   3 columns

Examples:

  Array                 Shape
  --------------------- -----------
  `[1,2,3]`             `(3,)`
  `[[1,2],[3,4]]`       `(2,2)`
  `np.zeros((2,3,4))`   `(2,3,4)`

Memory trick:

Read left to right.

For `(2,3,4)`:

-   2 matrices
-   each matrix has 3 rows
-   each row has 4 columns

------------------------------------------------------------------------

# 3. `size`

Returns the total number of elements.

``` python
a = np.array([[1,2,3],[4,5,6]])
print(a.size)
```

Output:

``` text
6
```

Formula:

``` text
size = product(shape)
```

Example:

Shape:

``` text
(2,3,4)
```

Size:

``` text
2 × 3 × 4 = 24
```

------------------------------------------------------------------------

# 4. `dtype`

Shows the data type of the array.

``` python
a = np.array([1,2,3])
print(a.dtype)
```

Output (platform dependent):

``` text
int64
```

Float example:

``` python
np.array([1.5,2.5]).dtype
```

Common data types:

  Type         Meaning
  ------------ ----------------
  int32        32-bit integer
  int64        64-bit integer
  float32      32-bit float
  float64      64-bit float
  bool         Boolean
  complex128   Complex number

Specify a type:

``` python
a = np.array([1,2,3], dtype=np.float32)
```

------------------------------------------------------------------------

# 5. `itemsize`

Returns the memory used by one element (in bytes).

``` python
a = np.array([1,2,3], dtype=np.int32)
print(a.itemsize)
```

Output:

``` text
4
```

Examples:

  Data Type     Item Size
  ----------- -----------
  int32           4 bytes
  int64           8 bytes
  float32         4 bytes
  float64         8 bytes

------------------------------------------------------------------------

# 6. `nbytes`

Returns the total memory used by the array.

Formula:

``` text
nbytes = size × itemsize
```

Example:

``` python
a = np.array([1,2,3], dtype=np.int32)

print(a.size)
print(a.itemsize)
print(a.nbytes)
```

Output:

``` text
3
4
12
```

------------------------------------------------------------------------

# Relationship Between Attributes

``` text
shape  -> dimensions
size   -> total elements
dtype  -> data type
itemsize -> bytes per element
nbytes -> total memory
ndim   -> number of axes
```

------------------------------------------------------------------------

# Complete Example

``` python
import numpy as np

a = np.array([[10,20,30],
              [40,50,60]])

print("Array:")
print(a)

print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)
print("dtype:", a.dtype)
print("itemsize:", a.itemsize)
print("nbytes:", a.nbytes)
```

------------------------------------------------------------------------

# Common Interview Questions

## Q1

Difference between `shape` and `size`?

**Answer**

-   `shape` gives dimensions.
-   `size` gives total elements.

------------------------------------------------------------------------

## Q2

Difference between `ndim` and `shape`?

**Answer**

-   `ndim` = number of dimensions.
-   `shape` = length of each dimension.

------------------------------------------------------------------------

## Q3

How is `nbytes` calculated?

**Answer**

``` text
nbytes = size × itemsize
```

------------------------------------------------------------------------

## Q4

Can two arrays have the same size but different shapes?

Yes.

Examples:

-   `(2,6)`
-   `(3,4)`
-   `(12,)`

All have 12 elements.

------------------------------------------------------------------------

# Practice Questions

1.  Create a 1D array and print every attribute.
2.  Create a 2×4 array and find its shape and size.
3.  Create a `(2,3,4)` array using `zeros()` and print `ndim`.
4.  Create a `float32` array and check `itemsize`.
5.  Verify `nbytes = size × itemsize`.
6.  Which attribute returns the number of dimensions?
7.  Which attribute returns the total elements?
8.  Which attribute returns the data type?

------------------------------------------------------------------------

# Cheat Sheet

``` python
import numpy as np

a = np.array([[1,2],[3,4]])

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)
```

  Attribute    Returns
  ------------ ----------------------
  `ndim`       Number of dimensions
  `shape`      Dimensions
  `size`       Total elements
  `dtype`      Data type
  `itemsize`   Bytes per element
  `nbytes`     Total memory

**Next Chapter:** Reshaping Arrays (`reshape()`, `resize()`,
`flatten()`, `ravel()`)
