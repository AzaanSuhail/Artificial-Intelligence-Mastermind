# Chapter 6: Iterating Through NumPy Arrays

> **Goal:** Learn how to traverse NumPy arrays efficiently from 1D to
> 5D.

---

# Learning Objectives

After this chapter, you will be able to:

- Iterate through 1D, 2D, 3D, 4D, and 5D arrays
- Use standard `for` loops
- Use `np.nditer()`
- Use `np.ndenumerate()`
- Understand C-order and F-order iteration
- Modify arrays while iterating
- Answer common interview questions

---

# 1. What is Iteration?

Iteration means visiting every element of an array one by one.

```python
import numpy as np

arr = np.array([10, 20, 30])

for value in arr:
    print(value)
```

Output:

```text
10
20
30
```

---

# 2. Iterating Over a 2D Array

```python
arr = np.array([
    [1,2,3],
    [4,5,6]
])

for row in arr:
    print(row)
```

Output:

```text
[1 2 3]
[4 5 6]
```

To access every element:

```python
for row in arr:
    for value in row:
        print(value)
```

---

# 3. Iterating Over a 3D Array

```python
arr = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

for matrix in arr:
    for row in matrix:
        for value in row:
            print(value)
```

---

# 4. Iterating Over 4D and 5D Arrays

The idea is the same: add one loop for each dimension.

```python
arr = np.zeros((2,3,4,5))
```

```python
for group in arr:
    for matrix in group:
        for row in matrix:
            for value in row:
                print(value)
```

A 5D array requires five nested loops.

> Deep nesting becomes difficult to read. NumPy provides better tools.

---

# 5. Using `np.nditer()`

`nditer()` visits every element regardless of the number of dimensions.

```python
arr = np.array([
    [1,2,3],
    [4,5,6]
])

for value in np.nditer(arr):
    print(value)
```

Output:

```text
1
2
3
4
5
6
```

Benefits:

- Works with any number of dimensions
- Avoids deeply nested loops
- Memory efficient

---

# 6. Iterating Over a 3D Array with `nditer()`

```python
arr = np.arange(8).reshape(2,2,2)

for value in np.nditer(arr):
    print(value)
```

No extra loops are required.

---

# 7. Modifying Values During Iteration

Use `op_flags=['readwrite']`.

```python
arr = np.array([1,2,3])

for value in np.nditer(arr, op_flags=['readwrite']):
    value[...] = value * 10

print(arr)
```

Output:

```text
[10 20 30]
```

---

# 8. `np.ndenumerate()`

Returns both the index and the value.

```python
arr = np.array([[10,20],[30,40]])

for index, value in np.ndenumerate(arr):
    print(index, value)
```

Output:

```text
(0, 0) 10
(0, 1) 20
(1, 0) 30
(1, 1) 40
```

Useful when you need both the location and the element.

---

# 9. C-Order vs F-Order

## C-Order (Row Major)

Default iteration order.

```text
1 2 3
4 5 6

Visits:
1 2 3 4 5 6
```

```python
for x in np.nditer(arr, order='C'):
    print(x)
```

---

## F-Order (Column Major)

Visits column by column.

```text
1 2 3
4 5 6

Visits:
1 4 2 5 3 6
```

```python
for x in np.nditer(arr, order='F'):
    print(x)
```

---

# 10. External Loop

Process multiple values at once.

```python
arr = np.arange(6)

for chunk in np.nditer(arr, flags=['external_loop']):
    print(chunk)
```

Output:

```text
[0 1 2 3 4 5]
```

---

# Performance Tips

- Use vectorized operations instead of loops whenever possible.
- Use `nditer()` for generic multidimensional iteration.
- Avoid deeply nested loops for high-dimensional arrays.

Example:

```python
arr = np.arange(1_000_000)

# Better
arr = arr * 2

# Slower
for i in range(len(arr)):
    arr[i] *= 2
```

---

# Common Mistakes

❌ Forgetting nested loops for multidimensional arrays.

❌ Using Python loops when vectorized NumPy operations are available.

❌ Trying to modify values through `nditer()` without `readwrite`.

---

# Interview Questions

### Q1

What is the difference between a normal `for` loop and `nditer()`?

- `for` loops require nesting for higher dimensions.
- `nditer()` works for arrays of any dimension.

### Q2

When should you use `ndenumerate()`?

When you need both the index and the value.

### Q3

What is the default iteration order?

C-order (row-major).

### Q4

How do you modify values using `nditer()`?

```python
op_flags=['readwrite']
```

---

# Practice Questions

1. Iterate through a 1D array.
2. Print every element of a 2D array.
3. Iterate through a 3D array using nested loops.
4. Iterate through a 3D array using `nditer()`.
5. Print indexes and values using `ndenumerate()`.
6. Double every element using `readwrite`.
7. Compare C-order and F-order iteration.

---

# Cheat Sheet

```python
for x in arr:
    ...

for x in np.nditer(arr):
    ...

for idx, value in np.ndenumerate(arr):
    ...

for x in np.nditer(arr, op_flags=['readwrite']):
    x[...] *= 2

for x in np.nditer(arr, order='C'):
    ...

for x in np.nditer(arr, order='F'):
    ...
```

  Method                     Purpose

---

  `for`                      Simple iteration
  `nditer()`                 Iterate any dimension
  `ndenumerate()`            Index + value
  `order='C'`                Row-major
  `order='F'`                Column-major
  `op_flags=['readwrite']`   Modify elements

**Next Chapter:** Data Types and Type Conversion (`dtype`, `astype()`,
casting)
