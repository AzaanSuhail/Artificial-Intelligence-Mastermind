# Chapter 5: Indexing and Slicing in NumPy

> **Goal:** Learn how to access, extract, and modify data efficiently in
> NumPy arrays from 1D to 5D.

------------------------------------------------------------------------

# Learning Objectives

By the end of this chapter, you will be able to:

-   Access elements using indexing
-   Use positive and negative indexing
-   Slice arrays
-   Index 1D, 2D, 3D, 4D, and 5D arrays
-   Understand views vs copies
-   Use boolean indexing
-   Use fancy indexing

------------------------------------------------------------------------

# 1. What is Indexing?

**Indexing** means accessing a specific element using its position.

NumPy uses **zero-based indexing**.

``` python
import numpy as np

a = np.array([10,20,30,40])

print(a[0])
print(a[2])
```

Output:

``` text
10
30
```

------------------------------------------------------------------------

# 2. Negative Indexing

Negative indexes count from the end.

``` python
print(a[-1])
print(a[-2])
```

Output:

``` text
40
30
```

------------------------------------------------------------------------

# 3. 1D Slicing

Syntax:

``` python
array[start:stop:step]
```

Example:

``` python
a = np.array([10,20,30,40,50,60])

print(a[1:5])
print(a[:3])
print(a[::2])
print(a[::-1])
```

Output:

``` text
[20 30 40 50]
[10 20 30]
[10 30 50]
[60 50 40 30 20 10]
```

------------------------------------------------------------------------

# 4. 2D Indexing

``` python
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(a[1,2])
```

Output:

``` text
6
```

Rule:

``` text
array[row, column]
```

------------------------------------------------------------------------

# 5. 2D Slicing

First row:

``` python
a[0,:]
```

Second column:

``` python
a[:,1]
```

Submatrix:

``` python
a[0:2,1:3]
```

Output:

``` text
[[2 3]
 [5 6]]
```

------------------------------------------------------------------------

# 6. 3D Indexing

``` python
a = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print(a[0,1,1])
```

Output:

``` text
4
```

Rule:

``` text
array[matrix, row, column]
```

------------------------------------------------------------------------

# 7. 4D and 5D Indexing

A 4D array:

``` python
a = np.zeros((2,3,4,5))
```

Access one element:

``` python
a[1,2,3,4]
```

A 5D array:

``` python
b = np.zeros((2,2,3,4,5))
```

Access:

``` python
b[1,0,2,3,4]
```

General Rule:

``` text
One index for each dimension.
```

------------------------------------------------------------------------

# 8. Boolean Indexing

Select elements using a condition.

``` python
a = np.array([10,20,30,40,50])

print(a[a > 25])
```

Output:

``` text
[30 40 50]
```

Examples:

``` python
a[a % 2 == 0]
a[a != 20]
a[a < 40]
```

------------------------------------------------------------------------

# 9. Fancy Indexing

Select multiple positions at once.

``` python
a = np.array([10,20,30,40,50])

print(a[[0,2,4]])
```

Output:

``` text
[10 30 50]
```

2D Example:

``` python
a = np.array([[1,2],[3,4]])

print(a[[0,1],[1,0]])
```

Output:

``` text
[2 3]
```

------------------------------------------------------------------------

# 10. Views vs Copies

Slicing returns a **view**.

``` python
a = np.array([1,2,3,4])

b = a[1:3]
b[0] = 99

print(a)
```

Output:

``` text
[ 1 99  3  4]
```

Need an independent array?

``` python
c = a[1:3].copy()
```

------------------------------------------------------------------------

# Common Mistakes

❌

``` python
a[1,2]
```

on a 1D array.

Error:

``` text
IndexError
```

------------------------------------------------------------------------

❌

``` python
a[10]
```

when only 5 elements exist.

Error:

``` text
IndexError
```

------------------------------------------------------------------------

# Interview Questions

### Q1

Difference between indexing and slicing?

-   Indexing returns a single element.
-   Slicing returns one or more elements (usually a view).

### Q2

Does slicing create a copy?

No. It usually returns a **view**.

### Q3

How do you make a copy?

``` python
arr.copy()
```

### Q4

Difference between boolean indexing and fancy indexing?

-   Boolean indexing filters using conditions.
-   Fancy indexing selects specific positions.

------------------------------------------------------------------------

# Practice Questions

1.  Print the last element of a 1D array.
2.  Reverse an array using slicing.
3.  Print the second row of a matrix.
4.  Print the third column.
5.  Extract a 2×2 submatrix.
6.  Access an element from a 3D array.
7.  Select values greater than 100.
8.  Select indexes 0, 3, and 5 using fancy indexing.
9.  Demonstrate that slicing returns a view.
10. Create a copy and verify changes do not affect the original.

------------------------------------------------------------------------

# Cheat Sheet

``` python
arr[i]
arr[-1]

arr[start:stop:step]

arr[row, col]

arr[:,1]
arr[1,:]

arr[a > 10]

arr[[0,2,4]]

arr.copy()
```

  Technique           Purpose
  ------------------- ------------------
  `arr[i]`            Single element
  `arr[start:stop]`   Slice
  `arr[row,col]`      2D indexing
  `arr[:,1]`          Entire column
  `arr[1,:]`          Entire row
  `arr[mask]`         Boolean indexing
  `arr[[...]]`        Fancy indexing
  `copy()`            Independent copy

**Next Chapter:** Iterating Through NumPy Arrays (`nditer`,
`ndenumerate`, loops)
