# Chapter 9: Universal Functions (ufuncs) in NumPy

> **Goal:** Learn how NumPy's Universal Functions (ufuncs) perform fast,
> vectorized operations on arrays.

---

# Learning Objectives

After this chapter, you will be able to:

- Understand what a ufunc is
- Use common built-in ufuncs
- Understand vectorization
- Use ufunc methods like `reduce()`, `accumulate()`, and `outer()`
- Understand why ufuncs are faster than Python loops

---

# 1. What is a Universal Function (ufunc)?

A **Universal Function (ufunc)** is a function that operates
**element-wise** on NumPy arrays.

Instead of looping through each element yourself, NumPy performs the
operation internally using optimized C code.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])

print(np.square(arr))
```

Output:

```text
[ 1  4  9 16]
```

---

# 2. Why Use ufuncs?

Python loop:

```python
result = []

for x in [1,2,3]:
    result.append(x * 2)
```

NumPy:

```python
arr = np.array([1,2,3])

result = arr * 2
```

Advantages:

- Faster
- Cleaner code
- Uses optimized native implementation
- Supports broadcasting

---

# 3. Common Unary ufuncs

Unary = one input array.

```python
arr = np.array([-1,4,9])

print(np.abs(arr))
print(np.sqrt([1,4,9]))
print(np.square([2,3,4]))
print(np.exp([1,2]))
print(np.log([1,np.e]))
```

---

# 4. Common Binary ufuncs

Binary = two input arrays.

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.power(a,2))
```

Equivalent operators:

  ufunc             Operator

---

  `np.add()`        `+`
  `np.subtract()`   `-`
  `np.multiply()`   `*`
  `np.divide()`     `/`

---

# 5. Comparison ufuncs

```python
a = np.array([1,2,3])
b = np.array([2,2,1])

print(np.greater(a,b))
print(np.less(a,b))
print(np.equal(a,b))
```

Output:

```text
[False False  True]
[ True False False]
[False  True False]
```

---

# 6. Logical ufuncs

```python
a = np.array([True, False, True])
b = np.array([False, False, True])

print(np.logical_and(a,b))
print(np.logical_or(a,b))
print(np.logical_not(a))
```

---

# 7. Aggregation with `reduce()`

`reduce()` repeatedly applies a ufunc.

```python
arr = np.array([1,2,3,4])

print(np.add.reduce(arr))
```

Output:

```text
10
```

Equivalent to:

```text
1 + 2 + 3 + 4
```

---

# 8. Running Results with `accumulate()`

```python
arr = np.array([1,2,3,4])

print(np.add.accumulate(arr))
```

Output:

```text
[ 1  3  6 10]
```

---

# 9. Outer Operations

```python
a = np.array([1,2,3])
b = np.array([10,20])

print(np.multiply.outer(a,b))
```

Output:

```text
[[10 20]
 [20 40]
 [30 60]]
```

---

# 10. Broadcasting with ufuncs

```python
a = np.array([1,2,3])

print(np.add(a,10))
```

Output:

```text
[11 12 13]
```

The scalar is automatically broadcast to every element.

---

# 11. Where Parameter

Apply an operation only where a condition is true.

```python
a = np.array([1,2,3,4])

print(np.sqrt(a, where=a>2))
```

---

# 12. Output Parameter

Store the result in an existing array.

```python
a = np.array([1,2,3])
b = np.empty_like(a)

np.square(a, out=b)

print(b)
```

---

# Why Are ufuncs Fast?

- Implemented in optimized native code
- Operate on entire arrays
- Avoid Python-level loops
- Reduce interpreter overhead

---

# Common Mistakes

❌ Using Python loops for operations that NumPy can vectorize.

❌ Assuming every function modifies the original array.

Most ufuncs return a new array unless you use `out=`.

---

# Interview Questions

### Q1

What is a ufunc?

A function that performs fast element-wise operations on NumPy arrays.

### Q2

What is vectorization?

Performing operations on entire arrays instead of looping element by
element in Python.

### Q3

Difference between `reduce()` and `accumulate()`?

- `reduce()` returns a single result.
- `accumulate()` returns intermediate results.

### Q4

Why are ufuncs faster?

Because they are implemented in optimized native code and avoid Python
loops.

---

# Practice Questions

1. Square every element of an array.
2. Add two arrays using `np.add()`.
3. Find the cumulative sum using `np.add.accumulate()`.
4. Multiply two arrays using `np.multiply()`.
5. Create an outer product using `np.multiply.outer()`.
6. Compare two arrays using `np.greater()`.
7. Store results using the `out` parameter.

---

# Cheat Sheet

```python
np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)
np.divide(a,b)

np.square(a)
np.sqrt(a)
np.exp(a)
np.log(a)

np.add.reduce(a)
np.add.accumulate(a)

np.multiply.outer(a,b)

np.greater(a,b)
np.equal(a,b)

np.square(a, out=result)
```

  Method           Purpose

---

  `np.add()`       Addition
  `np.square()`    Square values
  `reduce()`       Single aggregated result
  `accumulate()`   Running result
  `outer()`        Outer operation
  `out=`           Write into existing array

**Next Chapter:** Statistical Functions in NumPy
