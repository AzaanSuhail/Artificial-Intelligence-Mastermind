# Chapter 12: Joining, Splitting, and Stacking Arrays

> **Goal:** Learn how to combine and divide NumPy arrays efficiently.

------------------------------------------------------------------------

# Learning Objectives

After this chapter, you will be able to:

-   Join arrays using `concatenate()` and `stack()`
-   Use `hstack()`, `vstack()`, `dstack()`
-   Use `column_stack()` and `row_stack()`
-   Split arrays using `split()` and `array_split()`
-   Split multidimensional arrays with `hsplit()`, `vsplit()`, and
    `dsplit()`
-   Understand shape compatibility rules

------------------------------------------------------------------------

# 1. Joining Arrays with `concatenate()`

``` python
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.concatenate((a,b)))
```

Output:

``` text
[1 2 3 4 5 6]
```

------------------------------------------------------------------------

# 2. Concatenate 2D Arrays

``` python
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.concatenate((a,b), axis=0))
print(np.concatenate((a,b), axis=1))
```

-   `axis=0` → join rows
-   `axis=1` → join columns

------------------------------------------------------------------------

# 3. `stack()`

Creates a **new axis**.

``` python
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.stack((a,b)))
```

Output shape: `(2, 3)`

------------------------------------------------------------------------

# 4. `vstack()`

Stack vertically.

``` python
print(np.vstack((a,b)))
```

------------------------------------------------------------------------

# 5. `hstack()`

Stack horizontally.

``` python
print(np.hstack((a,b)))
```

------------------------------------------------------------------------

# 6. `dstack()`

Stack along the third dimension.

``` python
print(np.dstack((a,b)))
```

------------------------------------------------------------------------

# 7. `column_stack()`

``` python
print(np.column_stack((a,b)))
```

Output:

``` text
[[1 4]
 [2 5]
 [3 6]]
```

------------------------------------------------------------------------

# 8. `row_stack()`

``` python
print(np.row_stack((a,b)))
```

Equivalent to `vstack()`.

------------------------------------------------------------------------

# 9. Splitting Arrays

``` python
arr = np.array([1,2,3,4,5,6])

print(np.split(arr, 3))
```

Output:

``` text
[array([1,2]), array([3,4]), array([5,6])]
```

------------------------------------------------------------------------

# 10. `array_split()`

Unlike `split()`, it allows unequal sections.

``` python
print(np.array_split(arr, 4))
```

------------------------------------------------------------------------

# 11. `hsplit()`

``` python
arr = np.array([[1,2,3,4],
                [5,6,7,8]])

print(np.hsplit(arr, 2))
```

------------------------------------------------------------------------

# 12. `vsplit()`

``` python
arr = np.array([[1,2],
                [3,4],
                [5,6],
                [7,8]])

print(np.vsplit(arr, 2))
```

------------------------------------------------------------------------

# 13. `dsplit()`

Split a 3D array.

``` python
arr = np.arange(24).reshape(2,3,4)

print(np.dsplit(arr, 2))
```

------------------------------------------------------------------------

# Shape Compatibility Rules

Arrays must have compatible shapes except along the joining axis.

Example:

``` python
a = np.array([[1,2]])
b = np.array([[3,4,5]])

# Raises ValueError
# np.concatenate((a,b), axis=0)
```

------------------------------------------------------------------------

# Common Mistakes

-   Using incompatible shapes when joining arrays.
-   Using `split()` when the array cannot be divided equally.
-   Forgetting that `stack()` creates a new dimension.

------------------------------------------------------------------------

# Interview Questions

### Q1

Difference between `concatenate()` and `stack()`?

-   `concatenate()` joins existing axes.
-   `stack()` creates a new axis.

### Q2

Difference between `split()` and `array_split()`?

-   `split()` requires equal-sized sections.
-   `array_split()` allows unequal sections.

### Q3

What is the difference between `vstack()` and `hstack()`?

-   `vstack()` stacks vertically.
-   `hstack()` stacks horizontally.

------------------------------------------------------------------------

# Practice Questions

1.  Join two 1D arrays.
2.  Join two matrices row-wise.
3.  Join two matrices column-wise.
4.  Create a new dimension using `stack()`.
5.  Split an array into 4 parts.
6.  Use `array_split()` on 10 elements.
7.  Split a matrix column-wise.
8.  Split a 3D array using `dsplit()`.

------------------------------------------------------------------------

# Cheat Sheet

``` python
np.concatenate((a,b), axis=0)
np.stack((a,b))
np.vstack((a,b))
np.hstack((a,b))
np.dstack((a,b))
np.column_stack((a,b))
np.row_stack((a,b))

np.split(arr, 3)
np.array_split(arr, 4)
np.hsplit(arr, 2)
np.vsplit(arr, 2)
np.dsplit(arr, 2)
```

  Function          Purpose
  ----------------- --------------------
  `concatenate()`   Join arrays
  `stack()`         Join with new axis
  `vstack()`        Vertical stack
  `hstack()`        Horizontal stack
  `dstack()`        Depth stack
  `split()`         Equal split
  `array_split()`   Unequal split
  `hsplit()`        Horizontal split
  `vsplit()`        Vertical split
  `dsplit()`        Depth split

**Next Chapter:** Broadcasting in NumPy
