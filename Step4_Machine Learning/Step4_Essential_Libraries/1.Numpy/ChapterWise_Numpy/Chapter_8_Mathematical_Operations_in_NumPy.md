# Chapter 8: Mathematical Operations in NumPy

> **Goal:** Master element-wise mathematical operations, aggregation,
> and broadcasting basics for numerical computing.

------------------------------------------------------------------------

# Learning Objectives

After this chapter, you will be able to:

-   Perform arithmetic operations on arrays
-   Understand element-wise computation
-   Use scalar operations
-   Apply mathematical functions
-   Compare arrays
-   Aggregate values
-   Understand common mathematical interview questions

------------------------------------------------------------------------

# 1. Element-wise Operations

NumPy performs operations **element by element**.

``` python
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Output:

``` text
[5 7 9]
[-3 -3 -3]
[ 4 10 18]
[0.25 0.4  0.5 ]
```

------------------------------------------------------------------------

# 2. Scalar Operations

A scalar is a single value.

``` python
a = np.array([1,2,3])

print(a + 10)
print(a * 5)
print(a / 2)
```

Output:

``` text
[11 12 13]
[ 5 10 15]
[0.5 1.  1.5]
```

------------------------------------------------------------------------

# 3. Power and Modulus

``` python
a = np.array([2,3,4])

print(a ** 2)
print(a % 2)
```

Output:

``` text
[ 4  9 16]
[0 1 0]
```

------------------------------------------------------------------------

# 4. Absolute Values

``` python
a = np.array([-5,-2,3])

print(np.abs(a))
```

Output:

``` text
[5 2 3]
```

------------------------------------------------------------------------

# 5. Square Root

``` python
a = np.array([1,4,9,16])

print(np.sqrt(a))
```

Output:

``` text
[1. 2. 3. 4.]
```

------------------------------------------------------------------------

# 6. Exponential and Logarithm

``` python
a = np.array([1,2,3])

print(np.exp(a))
print(np.log(a))
```

-   `np.exp(x)` computes (e\^x).
-   `np.log(x)` computes the natural logarithm.

------------------------------------------------------------------------

# 7. Trigonometric Functions

``` python
angles = np.array([0, np.pi/2, np.pi])

print(np.sin(angles))
print(np.cos(angles))
print(np.tan(angles))
```

Angles are measured in **radians**.

------------------------------------------------------------------------

# 8. Rounding Functions

``` python
a = np.array([1.25, 2.75, 3.49])

print(np.floor(a))
print(np.ceil(a))
print(np.round(a))
```

------------------------------------------------------------------------

# 9. Comparison Operations

``` python
a = np.array([1,2,3])
b = np.array([2,2,1])

print(a > b)
print(a == b)
print(a != b)
```

Output:

``` text
[False False  True]
[False  True False]
[ True False  True]
```

------------------------------------------------------------------------

# 10. Aggregation Functions

``` python
a = np.array([10,20,30,40])

print(np.sum(a))
print(np.mean(a))
print(np.min(a))
print(np.max(a))
```

Output:

``` text
100
25.0
10
40
```

Other useful functions:

``` python
print(np.prod(a))
print(np.std(a))
print(np.var(a))
```

------------------------------------------------------------------------

# 11. Axis-Based Operations

``` python
a = np.array([
    [1,2,3],
    [4,5,6]
])

print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
```

Output:

``` text
[5 7 9]
[ 6 15]
```

-   `axis=0` → column-wise
-   `axis=1` → row-wise

------------------------------------------------------------------------

# 12. Dot Product

``` python
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.dot(a,b))
```

Output:

``` text
32
```

Calculation:

``` text
1×4 + 2×5 + 3×6 = 32
```

------------------------------------------------------------------------

# 13. Matrix Multiplication

``` python
a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])

print(a @ b)
```

Equivalent:

``` python
print(np.matmul(a,b))
```

------------------------------------------------------------------------

# Common Mistakes

❌ Using `*` for matrix multiplication.

``` python
a * b
```

This performs **element-wise multiplication**.

✅ Use:

``` python
a @ b
```

or

``` python
np.matmul(a,b)
```

------------------------------------------------------------------------

# Interview Questions

### Q1

What is the difference between `*` and `@`?

-   `*` → element-wise multiplication
-   `@` → matrix multiplication

### Q2

Difference between `sum()` and `mean()`?

-   `sum()` adds values.
-   `mean()` computes the average.

### Q3

Why does `np.sin()` expect radians?

NumPy follows the mathematical standard where trigonometric functions
operate on radians.

------------------------------------------------------------------------

# Practice Questions

1.  Add two arrays.
2.  Multiply an array by 100.
3.  Compute square roots of an array.
4.  Find the mean of a matrix.
5.  Compute row-wise and column-wise sums.
6.  Calculate a dot product.
7.  Perform matrix multiplication.
8.  Compare two arrays using `>` and `==`.

------------------------------------------------------------------------

# Cheat Sheet

``` python
a + b
a - b
a * b
a / b
a ** 2
a % 2

np.abs(a)
np.sqrt(a)
np.exp(a)
np.log(a)

np.sum(a)
np.mean(a)
np.min(a)
np.max(a)
np.prod(a)

np.dot(a,b)
a @ b
np.matmul(a,b)
```

  Function      Purpose
  ------------- -------------------------
  `+ - * /`     Element-wise arithmetic
  `**`          Power
  `%`           Modulus
  `np.sqrt()`   Square root
  `np.exp()`    Exponential
  `np.log()`    Natural log
  `np.sum()`    Sum
  `np.mean()`   Average
  `np.dot()`    Dot product
  `@`           Matrix multiplication

**Next Chapter:** Universal Functions (ufuncs)
