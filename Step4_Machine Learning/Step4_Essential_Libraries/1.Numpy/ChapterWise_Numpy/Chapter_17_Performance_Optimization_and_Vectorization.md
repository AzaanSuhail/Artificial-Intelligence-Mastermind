# Chapter 17: Performance Optimization and Vectorization in NumPy

> **Goal:** Learn why NumPy is fast and how to write high-performance
> numerical code.

------------------------------------------------------------------------

# Why Performance Matters

``` text
Large Dataset
      │
      ▼
Efficient NumPy Code
      │
      ▼
Faster Execution
      │
      ▼
Less CPU Time
```

Machine Learning, AI, and Data Science often process millions of values.
Small optimizations can save minutes or even hours.

------------------------------------------------------------------------

# 1. Python Loop vs NumPy Vectorization

Python loop:

``` python
result=[]
for i in range(5):
    result.append(i*2)
```

Vectorized:

``` python
import numpy as np

arr=np.arange(5)
print(arr*2)
```

Visualization

``` text
Python

1 → multiply
2 → multiply
3 → multiply
4 → multiply
5 → multiply

NumPy

Entire Array
     │
     ▼
Single Vectorized Operation
```

------------------------------------------------------------------------

# 2. Why NumPy is Faster

``` text
Python
│
├── One element at a time
├── Interpreter overhead
└── Slower

NumPy
│
├── C implementation
├── Continuous memory
├── SIMD optimizations
└── Faster
```

------------------------------------------------------------------------

# 3. Broadcasting Improves Speed

``` python
a=np.arange(5)
print(a+10)
```

``` text
Scalar
 10
 │
 ▼
Broadcast
 │
 ▼
Entire Array
```

------------------------------------------------------------------------

# 4. Avoid Python Loops

❌

``` python
for i in range(len(arr)):
    arr[i]+=1
```

✅

``` python
arr += 1
```

------------------------------------------------------------------------

# 5. Views vs Copies

``` python
a=np.arange(6)
view=a[:3]
copy=a[:3].copy()
```

Visualization

``` text
Original Array
      │
 ┌────┴────┐
 ▼         ▼
View      Copy

View shares memory.
Copy owns new memory.
```

------------------------------------------------------------------------

# 6. Timing Code

``` python
import timeit

time=timeit.timeit(
    "arr*2",
    setup="import numpy as np; arr=np.arange(1000000)",
    number=100
)

print(time)
```

------------------------------------------------------------------------

# 7. Memory-Efficient Operations

Instead of:

``` python
c=a+b
```

Use:

``` python
np.add(a,b,out=a)
```

Visualization

``` text
Without out=
A + B
 │
 ▼
New Memory

With out=
A + B
 │
 ▼
Reuse Existing Memory
```

------------------------------------------------------------------------

# 8. Performance Checklist

-   Use vectorization
-   Avoid Python loops
-   Use broadcasting
-   Prefer views when safe
-   Use in-place operations
-   Profile before optimizing

------------------------------------------------------------------------

# Real-World Example

``` text
CSV
 │
 ▼
NumPy Array
 │
 ▼
Vectorized Processing
 │
 ▼
Machine Learning Model
```

------------------------------------------------------------------------

# Common Mistakes

-   Iterating through every element manually
-   Creating unnecessary copies
-   Ignoring broadcasting
-   Premature optimization

------------------------------------------------------------------------

# Interview Questions

1.  Why is NumPy faster than Python lists?
2.  What is vectorization?
3.  Difference between a view and a copy?
4.  How does broadcasting improve performance?
5.  When should you use `out=`?

------------------------------------------------------------------------

# Practice

1.  Replace a loop with vectorization.
2.  Time two different approaches using `timeit`.
3.  Compare view vs copy.
4.  Use broadcasting to add a scalar.
5.  Perform an in-place addition.

------------------------------------------------------------------------

# Mind Map

``` text
Performance
│
├── Vectorization
├── Broadcasting
├── Views
├── Copies
├── In-place
├── timeit
└── Memory Optimization
```

------------------------------------------------------------------------

# Cheat Sheet

``` python
arr*2
arr+10
arr+=1
np.add(a,b,out=a)
view=a[:]
copy=a.copy()
timeit.timeit(...)
```

**Next Chapter:** NumPy Masking and Advanced Boolean Indexing
