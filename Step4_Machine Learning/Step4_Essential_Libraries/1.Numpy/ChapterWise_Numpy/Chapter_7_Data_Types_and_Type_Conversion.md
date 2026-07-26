# Chapter 7: NumPy Data Types and Type Conversion

> **Goal:** Understand NumPy data types (`dtype`) and learn how to
> convert arrays safely and efficiently.

------------------------------------------------------------------------

# Learning Objectives

After this chapter, you will be able to:

-   Understand what a data type is
-   Use `dtype`
-   Create arrays with a specific data type
-   Convert data using `astype()`
-   Explain implicit and explicit casting
-   Choose appropriate data types for performance and memory

------------------------------------------------------------------------

# 1. What is a Data Type?

A **data type** tells NumPy what kind of values an array stores.

Examples:

-   Integers
-   Floating-point numbers
-   Boolean values
-   Complex numbers
-   Strings

``` python
import numpy as np

arr = np.array([10, 20, 30])
print(arr.dtype)
```

Output:

``` text
int64
```

------------------------------------------------------------------------

# 2. Common NumPy Data Types

  Data Type      Description
  -------------- --------------------------------
  `int8`         8-bit signed integer
  `int16`        16-bit signed integer
  `int32`        32-bit signed integer
  `int64`        64-bit signed integer
  `uint8`        8-bit unsigned integer
  `float32`      32-bit floating point
  `float64`      64-bit floating point
  `bool_`        Boolean values
  `complex64`    Complex numbers
  `complex128`   High precision complex numbers
  `str_`         Unicode strings

------------------------------------------------------------------------

# 3. Checking the Data Type

``` python
a = np.array([1.2, 3.4])

print(a.dtype)
```

Output:

``` text
float64
```

------------------------------------------------------------------------

# 4. Creating Arrays with a Specific Type

``` python
a = np.array([1,2,3], dtype=np.float32)

print(a)
print(a.dtype)
```

Output:

``` text
[1. 2. 3.]
float32
```

------------------------------------------------------------------------

# 5. Type Conversion with `astype()`

``` python
a = np.array([1,2,3])

b = a.astype(np.float64)

print(b.dtype)
```

Output:

``` text
float64
```

------------------------------------------------------------------------

# 6. Integer to Float

``` python
a = np.array([10,20,30])

print(a.astype(float))
```

Output:

``` text
[10. 20. 30.]
```

------------------------------------------------------------------------

# 7. Float to Integer

``` python
a = np.array([1.9, 2.8, 3.1])

print(a.astype(int))
```

Output:

``` text
[1 2 3]
```

> `astype(int)` truncates the decimal part; it does **not** round.

------------------------------------------------------------------------

# 8. Boolean Conversion

``` python
a = np.array([0, 1, 2, -5])

print(a.astype(bool))
```

Output:

``` text
[False  True  True  True]
```

Rule:

-   `0` → `False`
-   Non-zero → `True`

------------------------------------------------------------------------

# 9. String Conversion

``` python
a = np.array([1,2,3])

print(a.astype(str))
```

Output:

``` text
['1' '2' '3']
```

------------------------------------------------------------------------

# 10. Implicit vs Explicit Casting

## Implicit

NumPy chooses a compatible type automatically.

``` python
a = np.array([1, 2.5])

print(a.dtype)
```

Output:

``` text
float64
```

The integer is promoted to a float.

## Explicit

You choose the type.

``` python
np.array([1,2,3], dtype=np.int16)
```

------------------------------------------------------------------------

# 11. Memory Comparison

``` python
a = np.array([1,2,3], dtype=np.int32)
b = np.array([1,2,3], dtype=np.int64)

print(a.itemsize)
print(b.itemsize)
```

Output:

``` text
4
8
```

Smaller types use less memory but have a smaller range.

------------------------------------------------------------------------

# 12. Safe vs Unsafe Casting

Safe:

``` python
np.array([1,2,3]).astype(np.float64)
```

Unsafe (possible information loss):

``` python
np.array([1.8,2.9]).astype(np.int32)
```

Decimals are discarded.

------------------------------------------------------------------------

# Best Practices

-   Use `float32` for many machine learning tasks to reduce memory
    usage.
-   Use `int32` or `int64` for integer data depending on the required
    range.
-   Convert types only when necessary.

------------------------------------------------------------------------

# Common Mistakes

❌ Assuming `astype()` changes the original array.

``` python
a = np.array([1,2,3])

a.astype(float)

print(a.dtype)
```

Output:

``` text
int64
```

Correct:

``` python
a = a.astype(float)
```

------------------------------------------------------------------------

# Interview Questions

### Q1

What does `dtype` return?

The data type of the array.

### Q2

What is the difference between `dtype` and `astype()`?

-   `dtype` inspects.
-   `astype()` converts.

### Q3

Does `astype()` modify the original array?

No. It returns a new array.

### Q4

Does converting `float` to `int` round values?

No. It truncates them.

------------------------------------------------------------------------

# Practice Questions

1.  Create an `int32` array.
2.  Convert an integer array to `float32`.
3.  Convert floats to integers.
4.  Create a boolean array from integers.
5.  Compare `itemsize` of `int32` and `int64`.
6.  Print the `dtype` of a string array.
7.  Demonstrate implicit casting.

------------------------------------------------------------------------

# Cheat Sheet

``` python
import numpy as np

a = np.array([1,2,3])

print(a.dtype)

a = a.astype(np.float32)

a.astype(int)
a.astype(bool)
a.astype(str)
```

  Function     Purpose
  ------------ -------------------
  `dtype`      Inspect data type
  `astype()`   Convert data type
  `itemsize`   Bytes per element

**Next Chapter:** Mathematical Operations in NumPy
