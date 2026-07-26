# Chapter 1: Introduction to NumPy

> **Goal:** Understand what NumPy is, why it exists, and how to create
> your first NumPy arrays.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Explain what NumPy is.
- Understand why NumPy is faster than Python lists.
- Install and import NumPy.
- Create 1D, 2D, and 3D arrays.
- Understand the difference between lists and NumPy arrays.
- Write your first NumPy programs.

---

# 1. What is NumPy?

**NumPy** stands for **Numerical Python**.

It is the most popular Python library for numerical computing and forms
the foundation of the Python data science ecosystem.

NumPy provides:

- Fast multidimensional arrays
- Mathematical operations
- Linear algebra
- Statistics
- Random number generation
- Support for machine learning and scientific computing

---

# 2. Why Do We Need NumPy?

Python lists are flexible but slow for large numerical computations.

NumPy stores data in contiguous memory and performs operations using
optimized C code.

### Example

```python
numbers = [1, 2, 3, 4]
```

NumPy version:

```python
import numpy as np

numbers = np.array([1, 2, 3, 4])
```

---

# 3. Advantages of NumPy

- High performance
- Less memory usage
- Easy mathematical operations
- Supports multidimensional arrays
- Foundation for Pandas, SciPy, Matplotlib, Scikit-learn, TensorFlow,
  and PyTorch

---

# 4. Installing NumPy

Using pip:

```bash
pip install numpy
```

Check the version:

```python
import numpy as np

print(np.__version__)
```

---

# 5. Importing NumPy

Standard convention:

```python
import numpy as np
```

Why `np`?

It is a widely accepted alias that makes code shorter and more readable.

---

# 6. Creating Your First Array

## 1D Array

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
```

Output:

```text
[10 20 30 40]
```

## 2D Array

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)
```

## 3D Array

```python
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(arr)
```

---

# 7. Python List vs NumPy Array

  Feature            Python List   NumPy Array

---

  Speed              Slower        Faster
  Memory             Higher        Lower
  Math Operations    Limited       Excellent
  Multidimensional   Manual        Built-in

---

# 8. Basic Mathematical Operations

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Output:

```text
[5 7 9]
[-3 -3 -3]
[ 4 10 18]
[0.25 0.4 0.5]
```

---

# 9. Common Beginner Mistakes

❌ Forgetting to import NumPy

```python
array([1,2,3])
```

✅ Correct

```python
import numpy as np

np.array([1,2,3])
```

---

# 10. Summary

You learned:

- What NumPy is
- Why NumPy is important
- Installing and importing NumPy
- Creating 1D, 2D, and 3D arrays
- Python lists vs NumPy arrays
- Basic arithmetic operations

---

# Practice Questions

1. What does NumPy stand for?
2. Why is NumPy faster than Python lists?
3. Write code to create a 1D array of five numbers.
4. Create a 2×3 array.
5. Create a 3D array with two matrices.
6. Import NumPy using the standard alias.
7. Add two NumPy arrays element-wise.
8. Name three advantages of NumPy.
9. What is the output of `np.array([1,2,3])`?
10. Why is `import numpy as np` the standard convention?

---

# Chapter 1 Cheat Sheet

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr)
print(type(arr))

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

**Next Chapter:** NumPy Array Attributes (`ndim`, `shape`, `size`,
`dtype`, `itemsize`, `nbytes`)
