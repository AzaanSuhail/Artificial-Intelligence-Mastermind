# NumPy `shape` and `reshape()` --- Complete Guide (1D to 5D)

## The Big Idea

Think of a NumPy array like a building.

-   **1D** → A straight road
-   **2D** → A building floor (rows × columns)
-   **3D** → A stack of floors
-   **4D** → Multiple buildings
-   **5D** → Multiple cities containing buildings

`shape` tells you the dimensions of the array.

`reshape()` changes how the data is arranged **without changing the data
itself.**

------------------------------------------------------------------------

# What does `shape` return?

``` python
array.shape
```

It returns a **tuple**.

Example:

``` python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a.shape)
```

Output:

``` text
(4,)
```

Notice the comma. `(4,)` is a one-element tuple.

------------------------------------------------------------------------

# 1D Array

``` python
a = np.array([1,2,3,4,5])

print(a)
print(a.shape)
```

Output:

``` text
[1 2 3 4 5]
(5,)
```

Meaning: **5 elements**

Visualization:

``` text
[1 2 3 4 5]
```

Only one axis exists:

``` text
Axis 0 → 1 2 3 4 5
```

------------------------------------------------------------------------

# 2D Array

``` python
a = np.array([
    [1,2,3],
    [4,5,6]
])
```

Shape:

``` python
print(a.shape)
```

Output:

``` text
(2,3)
```

Meaning:

-   2 rows
-   3 columns

Visualization:

``` text
1 2 3
4 5 6
```

Axes:

-   Axis 0 → Rows
-   Axis 1 → Columns

------------------------------------------------------------------------

# 3D Array

``` python
a = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
```

Shape:

``` python
print(a.shape)
```

Output:

``` text
(2,2,2)
```

Meaning:

-   2 matrices
-   Each matrix has 2 rows
-   Each row has 2 columns

Axes:

-   Axis 0 → Matrices
-   Axis 1 → Rows
-   Axis 2 → Columns

------------------------------------------------------------------------

# 4D Array

``` python
a = np.zeros((2,3,4,5))
print(a.shape)
```

Output:

``` text
(2,3,4,5)
```

Meaning:

-   2 groups
-   Each group has 3 matrices
-   Each matrix has 4 rows
-   Each row has 5 columns

------------------------------------------------------------------------

# 5D Array

``` python
a = np.zeros((2,3,4,5,6))
print(a.shape)
```

Output:

``` text
(2,3,4,5,6)
```

Meaning:

-   2 groups
-   Each group has 3 subgroups
-   Each subgroup has 4 matrices
-   Each matrix has 5 rows
-   Each row has 6 columns

------------------------------------------------------------------------

# General Rule

For:

``` text
(a, b, c, d, e)
```

Read from left to right:

-   `a` groups
-   Each group has `b`
-   Each `b` has `c`
-   Each `c` has `d`
-   Each `d` has `e`

------------------------------------------------------------------------

# Total Number of Elements

Multiply all dimensions.

Example:

``` text
Shape = (2,3,4)
```

Total elements:

``` text
2 × 3 × 4 = 24
```

Verify:

``` python
a = np.zeros((2,3,4))
print(a.size)
```

Output:

``` text
24
```

------------------------------------------------------------------------

# `reshape()`

Definition:

Changes dimensions **without changing data**.

Original:

``` python
a = np.array([1,2,3,4,5,6])
```

Shape:

``` text
(6,)
```

## Convert to 2 × 3

``` python
b = a.reshape(2,3)
```

Output:

``` text
[[1 2 3]
 [4 5 6]]
```

Shape:

``` text
(2,3)
```

## Convert to 3 × 2

``` python
b = a.reshape(3,2)
```

Output:

``` text
[[1 2]
 [3 4]
 [5 6]]
```

## Convert to 1 × 6

``` python
b = a.reshape(1,6)
```

Shape:

``` text
(1,6)
```

## Convert to 6 × 1

``` python
b = a.reshape(6,1)
```

Shape:

``` text
(6,1)
```

------------------------------------------------------------------------

# Reshape into 3D

``` python
a = np.arange(1,13)
b = a.reshape(2,2,3)
print(b.shape)
```

Output:

``` text
(2,2,3)
```

------------------------------------------------------------------------

# When does `reshape()` fail?

``` python
a = np.arange(10)
a.reshape(3,4)
```

Needs 12 elements but only 10 exist.

Result:

``` text
ValueError
```

------------------------------------------------------------------------

# Golden Rule

The product of the new shape **must equal** the number of elements.

``` text
Old size = New size
```

Examples for 24 elements:

-   2 × 12
-   3 × 8
-   4 × 6
-   2 × 2 × 6
-   2 × 3 × 4
-   1 × 24
-   24 × 1

Impossible:

``` text
5 × 5 = 25 elements
```

------------------------------------------------------------------------

# Automatic Dimension (`-1`)

NumPy calculates one missing dimension.

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

Correct:

``` python
reshape(2,-1)
reshape(-1,3)
```

Wrong:

``` python
reshape(-1,-1)
```

------------------------------------------------------------------------

# Interview Questions

## Q1

``` python
np.arange(24).reshape(2,3,4).shape
```

Answer:

``` text
(2,3,4)
```

## Q2

``` python
np.arange(20).reshape(4,5).shape
```

Answer:

``` text
(4,5)
```

## Q3

``` python
np.arange(8).reshape(2,2,2)
```

Possible?

Yes, because:

``` text
2 × 2 × 2 = 8
```

## Q4

``` python
np.arange(15).reshape(2,5)
```

Possible?

No.

Need 10 elements but have 15.

## Q5

``` python
np.arange(18).reshape(2,-1,3)
```

Calculation:

``` text
2 × x × 3 = 18
x = 3
```

Answer:

``` text
(2,3,3)
```

------------------------------------------------------------------------

# Memory Trick

``` text
1D → Line
2D → Table
3D → Stack of tables
4D → Collection of stacks
5D → Collection of collections
```

Each new dimension wraps the previous one.

------------------------------------------------------------------------

# Cheat Sheet

  ------------------------------------------------------------------------
  Dimension              Shape           Interpretation
  ---------------------- --------------- ---------------------------------
  1D                     `(5,)`          5 elements

  2D                     `(3,4)`         3 rows × 4 columns

  3D                     `(2,3,4)`       2 matrices × 3 rows × 4 columns

  4D                     `(2,3,4,5)`     2 groups × 3 matrices × 4 rows ×
                                         5 columns

  5D                     `(2,3,4,5,6)`   2 groups × 3 groups × 4 matrices
                                         × 5 rows × 6 columns
  ------------------------------------------------------------------------

## Reshape Rules

-   Number of elements must remain the same.
-   `array.size == product(new_shape)`
-   Only one `-1` is allowed.
-   `reshape()` changes the shape, not the values.
