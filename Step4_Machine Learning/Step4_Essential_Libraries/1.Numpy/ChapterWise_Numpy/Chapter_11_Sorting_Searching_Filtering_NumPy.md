# Chapter 11: Sorting, Searching, and Filtering Arrays

> **Goal:** Learn how to organize, search, and filter NumPy arrays
> efficiently.

------------------------------------------------------------------------

# Learning Objectives

After this chapter, you will be able to:

-   Sort 1D and multidimensional arrays
-   Use `sort()`, `argsort()`, and `lexsort()`
-   Search with `searchsorted()`
-   Locate values using `where()`, `nonzero()`, and `argwhere()`
-   Filter arrays using boolean masks
-   Work with unique and set operations

------------------------------------------------------------------------

# 1. Sorting Arrays

## `np.sort()`

Returns a **sorted copy** of the array.

``` python
import numpy as np

arr = np.array([5, 2, 8, 1, 3])

print(np.sort(arr))
```

Output:

``` text
[1 2 3 5 8]
```

The original array is unchanged.

------------------------------------------------------------------------

# 2. In-place Sorting

``` python
arr = np.array([5,2,8,1])
arr.sort()

print(arr)
```

Output:

``` text
[1 2 5 8]
```

------------------------------------------------------------------------

# 3. Sorting 2D Arrays

``` python
arr = np.array([
    [3,1,2],
    [6,4,5]
])

print(np.sort(arr))
```

Default: sorts **row-wise** (`axis=-1`).

Sort column-wise:

``` python
print(np.sort(arr, axis=0))
```

------------------------------------------------------------------------

# 4. `argsort()`

Returns the indices that would sort an array.

``` python
arr = np.array([50,20,40,10])

print(np.argsort(arr))
```

Output:

``` text
[3 1 2 0]
```

Meaning:

``` text
arr[3] = 10
arr[1] = 20
arr[2] = 40
arr[0] = 50
```

------------------------------------------------------------------------

# 5. `lexsort()`

Sort using multiple keys.

``` python
names = np.array(["Tom","Anna","Tom","Bob"])
ages = np.array([20,18,19,25])

idx = np.lexsort((names, ages))
print(idx)
```

------------------------------------------------------------------------

# 6. `searchsorted()`

Find the insertion position while maintaining sorted order.

``` python
arr = np.array([10,20,30,40])

print(np.searchsorted(arr, 25))
```

Output:

``` text
2
```

------------------------------------------------------------------------

# 7. `where()`

Return elements or indices matching a condition.

``` python
arr = np.array([10,20,30,40])

print(np.where(arr > 20))
```

Output:

``` text
(array([2, 3]),)
```

Replace values:

``` python
print(np.where(arr > 20, 100, arr))
```

Output:

``` text
[ 10  20 100 100]
```

------------------------------------------------------------------------

# 8. Boolean Filtering

``` python
arr = np.array([5,10,15,20])

print(arr[arr >= 10])
```

Output:

``` text
[10 15 20]
```

------------------------------------------------------------------------

# 9. `nonzero()`

Return indices of non-zero elements.

``` python
arr = np.array([0,5,0,8])

print(np.nonzero(arr))
```

Output:

``` text
(array([1, 3]),)
```

------------------------------------------------------------------------

# 10. `argwhere()`

Returns coordinates of matching elements.

``` python
arr = np.array([
    [1,0],
    [0,2]
])

print(np.argwhere(arr > 0))
```

Output:

``` text
[[0 0]
 [1 1]]
```

------------------------------------------------------------------------

# 11. `extract()`

Extract values using a condition.

``` python
arr = np.array([5,10,15,20])

print(np.extract(arr > 10, arr))
```

Output:

``` text
[15 20]
```

------------------------------------------------------------------------

# 12. `unique()`

Find unique values.

``` python
arr = np.array([1,2,2,3,3,3])

print(np.unique(arr))
```

Output:

``` text
[1 2 3]
```

With counts:

``` python
values, counts = np.unique(arr, return_counts=True)
print(values)
print(counts)
```

------------------------------------------------------------------------

# 13. Membership Testing

``` python
a = np.array([1,2,3,4])

print(np.isin(a, [2,4,6]))
```

Output:

``` text
[False  True False  True]
```

------------------------------------------------------------------------

# 14. Set Operations

``` python
a = np.array([1,2,3])
b = np.array([3,4,5])

print(np.intersect1d(a,b))
print(np.union1d(a,b))
print(np.setdiff1d(a,b))
print(np.setxor1d(a,b))
```

------------------------------------------------------------------------

# Common Mistakes

❌ Assuming `np.sort()` changes the original array.

It returns a sorted copy.

Use:

``` python
arr.sort()
```

for in-place sorting.

------------------------------------------------------------------------

# Interview Questions

### Q1

Difference between `sort()` and `argsort()`?

-   `sort()` returns sorted values.
-   `argsort()` returns the indices that produce the sorted order.

### Q2

Difference between `where()` and boolean indexing?

-   Boolean indexing returns matching values.
-   `where()` can return indices or perform conditional replacement.

### Q3

How do you remove duplicates?

``` python
np.unique(arr)
```

------------------------------------------------------------------------

# Practice Questions

1.  Sort a 1D array.
2.  Sort each column of a matrix.
3.  Find sorting indices using `argsort()`.
4.  Find the insertion position of 35.
5.  Replace values greater than 50 with 0.
6.  Extract all even numbers.
7.  Find unique values and their counts.
8.  Find the intersection of two arrays.
9.  Test membership using `isin()`.

------------------------------------------------------------------------

# Cheat Sheet

``` python
np.sort(arr)
arr.sort()

np.argsort(arr)
np.lexsort(keys)

np.searchsorted(arr, value)

np.where(condition)
np.where(condition, x, y)

arr[mask]

np.nonzero(arr)
np.argwhere(condition)
np.extract(mask, arr)

np.unique(arr)

np.isin(a, b)

np.intersect1d(a,b)
np.union1d(a,b)
np.setdiff1d(a,b)
np.setxor1d(a,b)
```

  Function           Purpose
  ------------------ -----------------------------------
  `sort()`           Sort values
  `argsort()`        Sort indices
  `searchsorted()`   Find insertion index
  `where()`          Conditional selection/replacement
  `unique()`         Remove duplicates
  `isin()`           Membership test
  `intersect1d()`    Common values
  `union1d()`        Combined unique values

**Next Chapter:** Joining, Splitting, and Stacking Arrays
