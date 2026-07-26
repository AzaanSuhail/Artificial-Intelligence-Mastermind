# Chapter 13: Broadcasting in NumPy

> **Goal:** Master NumPy broadcasting so you can perform operations on
> arrays of different shapes without writing loops.

------------------------------------------------------------------------

# Learning Objectives

After this chapter, you will be able to:

-   Understand what broadcasting is
-   Learn the broadcasting rules
-   Broadcast across 1D, 2D, 3D, 4D, and 5D arrays
-   Use `np.newaxis`, `expand_dims()`, and `squeeze()`
-   Fix common broadcasting errors
-   Solve interview questions confidently

------------------------------------------------------------------------

# 1. What is Broadcasting?

Broadcasting is NumPy's mechanism for performing element-wise operations
on arrays with **different shapes**.

Instead of copying data, NumPy **virtually stretches** the smaller array
to match the larger one.

Example:

``` python
import numpy as np

a = np.array([1, 2, 3])

print(a + 10)
```

Output:

``` text
[11 12 13]
```

The scalar `10` is broadcast to `[10, 10, 10]`.

------------------------------------------------------------------------

# 2. Why Broadcasting?

Without broadcasting:

``` python
[1,2,3] + [10,10,10]
```

With broadcasting:

``` python
[1,2,3] + 10
```

Cleaner, faster, and memory-efficient.

------------------------------------------------------------------------

# 3. Broadcasting Rules

Compare shapes **from right to left**.

Two dimensions are compatible if:

1.  They are equal.
2.  One of them is `1`.

Otherwise, broadcasting fails.

------------------------------------------------------------------------

# 4. 1D Broadcasting

``` python
a = np.array([1,2,3])
b = np.array([10])

print(a + b)
```

Shape comparison:

``` text
(3)
(1)
```

Result:

``` text
(3)
```

------------------------------------------------------------------------

# 5. 2D + 1D Broadcasting

``` python
a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([10,20,30])

print(a + b)
```

Shapes:

``` text
(2,3)
(3,)
```

Result:

``` text
(2,3)
```

The row vector is added to every row.

------------------------------------------------------------------------

# 6. Column Broadcasting

``` python
a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([[10],
              [20]])

print(a + b)
```

Shapes:

``` text
(2,3)
(2,1)
```

The column vector is broadcast across columns.

------------------------------------------------------------------------

# 7. 3D Broadcasting

``` python
a = np.ones((2,3,4))
b = np.arange(4)

print((a + b).shape)
```

Shapes:

``` text
(2,3,4)
(4,)
```

Result:

``` text
(2,3,4)
```

------------------------------------------------------------------------

# 8. 4D Broadcasting

``` python
a = np.ones((2,3,4,5))
b = np.arange(5)

print((a + b).shape)
```

The last dimension matches.

------------------------------------------------------------------------

# 9. 5D Broadcasting

``` python
a = np.ones((2,3,4,5,6))
b = np.arange(6)

print((a + b).shape)
```

Again, the final dimension is broadcast.

------------------------------------------------------------------------

# 10. `np.newaxis`

Adds a new dimension.

``` python
a = np.array([1,2,3])

print(a.shape)

b = a[:, np.newaxis]

print(b.shape)
```

Output:

``` text
(3,)
(3,1)
```

------------------------------------------------------------------------

# 11. `np.expand_dims()`

``` python
a = np.array([1,2,3])

print(np.expand_dims(a, axis=0).shape)
print(np.expand_dims(a, axis=1).shape)
```

Output:

``` text
(1,3)
(3,1)
```

------------------------------------------------------------------------

# 12. `np.squeeze()`

Removes dimensions of size `1`.

``` python
a = np.array([[[1,2,3]]])

print(a.shape)

print(np.squeeze(a).shape)
```

Output:

``` text
(1,1,3)
(3,)
```

------------------------------------------------------------------------

# 13. Broadcasting Error

``` python
a = np.ones((2,3))
b = np.ones((4,))

# ValueError
# a + b
```

Shapes:

``` text
(2,3)
(4,)
```

The last dimensions (`3` and `4`) are incompatible.

------------------------------------------------------------------------

# How to Fix Broadcasting Errors

-   Reshape one array.
-   Add a new axis.
-   Check shapes before performing operations.

Example:

``` python
b = np.array([10,20]).reshape(2,1)

print(a + b)
```

------------------------------------------------------------------------

# Common Mistakes

-   Comparing shapes from left to right instead of right to left.
-   Forgetting that `1` can expand.
-   Assuming arrays must have identical shapes.

------------------------------------------------------------------------

# Interview Questions

### Q1

What are the broadcasting rules?

Dimensions must either: - be equal, or - one of them must be `1`.

### Q2

Why is broadcasting faster?

Because NumPy avoids creating unnecessary copies and performs vectorized
operations.

### Q3

Difference between `reshape()` and `newaxis`?

-   `reshape()` changes the overall shape.
-   `newaxis` inserts a dimension of size `1`.

### Q4

What does `squeeze()` do?

Removes dimensions whose size is `1`.

------------------------------------------------------------------------

# Practice Questions

1.  Add a scalar to a vector.
2.  Add a row vector to a matrix.
3.  Add a column vector to a matrix.
4.  Broadcast a 1D array over a 3D array.
5.  Convert `(3,)` to `(3,1)` using `newaxis`.
6.  Use `expand_dims()` to create `(1,3)`.
7.  Remove singleton dimensions using `squeeze()`.
8.  Fix a broadcasting error by reshaping an array.

------------------------------------------------------------------------

# Cheat Sheet

``` python
a + 10

a + b

a[:, np.newaxis]

np.expand_dims(a, axis=0)
np.expand_dims(a, axis=1)

np.squeeze(a)
```

  Function          Purpose
  ----------------- ---------------------------
  Broadcasting      Automatic shape expansion
  `np.newaxis`      Add dimension
  `expand_dims()`   Insert axis
  `squeeze()`       Remove size-1 axes

**Next Chapter:** Random Number Generation in NumPy
