# Chapter 2: Creating NumPy Arrays

> **Goal:** Learn every major way to create NumPy arrays.

------------------------------------------------------------------------

# Learning Objectives

By the end of this chapter you will be able to:

-   Create arrays using `array()`
-   Generate arrays with `zeros()`, `ones()`, `empty()`, and `full()`
-   Create identity matrices using `eye()` and `identity()`
-   Generate sequences using `arange()`, `linspace()`, and `logspace()`
-   Understand when to use each function

------------------------------------------------------------------------

# 1. `np.array()`

Converts Python lists or tuples into NumPy arrays.

``` python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
```

Output:

``` text
[1 2 3 4]
```

2D Example:

``` python
a = np.array([
    [1,2,3],
    [4,5,6]
])
```

------------------------------------------------------------------------

# 2. `np.zeros()`

Creates an array filled with zeros.

``` python
np.zeros(5)
```

Output:

``` text
[0. 0. 0. 0. 0.]
```

2D:

``` python
np.zeros((2,3))
```

------------------------------------------------------------------------

# 3. `np.ones()`

Creates an array filled with ones.

``` python
np.ones((3,2))
```

Output:

``` text
[[1. 1.]
 [1. 1.]
 [1. 1.]]
```

------------------------------------------------------------------------

# 4. `np.empty()`

Creates an array without initializing its values.

``` python
np.empty((2,2))
```

> The values are whatever already existed in memory, so they are
> unpredictable.

------------------------------------------------------------------------

# 5. `np.full()`

Creates an array filled with a specific value.

``` python
np.full((2,3), 7)
```

Output:

``` text
[[7 7 7]
 [7 7 7]]
```

------------------------------------------------------------------------

# 6. `np.eye()`

Creates an identity-like matrix.

``` python
np.eye(4)
```

Output:

``` text
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

Custom offset:

``` python
np.eye(4, k=1)
```

------------------------------------------------------------------------

# 7. `np.identity()`

Creates a square identity matrix.

``` python
np.identity(3)
```

Difference:

-   `identity(n)` only creates square identity matrices.
-   `eye()` is more flexible.

------------------------------------------------------------------------

# 8. `np.arange()`

Creates evenly spaced values using a step.

``` python
np.arange(0, 10, 2)
```

Output:

``` text
[0 2 4 6 8]
```

Syntax:

``` python
np.arange(start, stop, step)
```

------------------------------------------------------------------------

# 9. `np.linspace()`

Creates a fixed number of evenly spaced values.

``` python
np.linspace(0, 10, 5)
```

Output:

``` text
[ 0.   2.5  5.   7.5 10. ]
```

Syntax:

``` python
np.linspace(start, stop, num)
```

------------------------------------------------------------------------

# 10. `np.logspace()`

Creates values evenly spaced on a logarithmic scale.

``` python
np.logspace(0, 3, 4)
```

Output:

``` text
[   1.   10.  100. 1000.]
```

------------------------------------------------------------------------

# `arange()` vs `linspace()`

  Function       Controls
  -------------- ------------------
  `arange()`     Step size
  `linspace()`   Number of values

Example:

``` python
np.arange(0,10,2)
# [0 2 4 6 8]

np.linspace(0,10,6)
# [0. 2. 4. 6. 8. 10.]
```

------------------------------------------------------------------------

# Common Mistakes

❌

``` python
np.zeros(2,3)
```

✅

``` python
np.zeros((2,3))
```

❌

``` python
np.arange(5,0)
```

Returns an empty array because the default step is `+1`.

✅

``` python
np.arange(5,0,-1)
```

------------------------------------------------------------------------

# Summary

You learned:

-   `array()`
-   `zeros()`
-   `ones()`
-   `empty()`
-   `full()`
-   `eye()`
-   `identity()`
-   `arange()`
-   `linspace()`
-   `logspace()`

------------------------------------------------------------------------

# Practice Questions

1.  Create a 3×4 array of zeros.
2.  Create a 5×5 identity matrix.
3.  Create an array from 10 to 50 with a step of 5.
4.  Generate 11 equally spaced values from 0 to 100.
5.  Create a 4×2 array filled with 99.
6.  Explain the difference between `eye()` and `identity()`.
7.  Explain the difference between `arange()` and `linspace()`.
8.  Why should `empty()` be used carefully?
9.  Create a 2×2 array of ones.
10. Create logarithmic values from 10⁰ to 10⁴.

------------------------------------------------------------------------

# Cheat Sheet

``` python
import numpy as np

np.array([1,2,3])
np.zeros((2,3))
np.ones((2,3))
np.empty((2,3))
np.full((2,3),5)
np.eye(3)
np.identity(3)
np.arange(0,10,2)
np.linspace(0,10,5)
np.logspace(0,3,4)
```

**Next Chapter:** Array Attributes (`ndim`, `shape`, `size`, `dtype`,
`itemsize`, `nbytes`)
