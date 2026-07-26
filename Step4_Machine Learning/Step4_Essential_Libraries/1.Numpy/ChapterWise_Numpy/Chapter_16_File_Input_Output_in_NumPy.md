# Chapter 16: File Input/Output in NumPy

> **Goal:** Learn how to save, load, and exchange NumPy arrays
> efficiently.

------------------------------------------------------------------------

# Why Save Arrays?

Real-world projects often need to:

-   Save model data
-   Store datasets
-   Reload arrays later
-   Share data with other programs

``` text
Create Array
     │
     ▼
 Save to Disk
     │
     ▼
 Reload Later
```

------------------------------------------------------------------------

# 1. Saving a Single Array (`save`)

``` python
import numpy as np

arr = np.array([10,20,30])

np.save("numbers.npy", arr)
```

Visualization

``` text
Memory
[10 20 30]
     │
     ▼
numbers.npy
```

------------------------------------------------------------------------

# 2. Loading Arrays (`load`)

``` python
data = np.load("numbers.npy")
print(data)
```

``` text
numbers.npy
     │
     ▼
[10 20 30]
```

------------------------------------------------------------------------

# 3. Saving Multiple Arrays (`savez`)

``` python
a = np.arange(5)
b = np.ones((2,2))

np.savez("dataset.npz", a=a, b=b)
```

Visualization

``` text
dataset.npz
├── a
└── b
```

------------------------------------------------------------------------

# 4. Compressed Files (`savez_compressed`)

``` python
np.savez_compressed("small.npz", a=a, b=b)
```

Best for large datasets.

------------------------------------------------------------------------

# 5. Reading Text Files (`loadtxt`)

Suppose `data.txt` contains:

``` text
1 2 3
4 5 6
7 8 9
```

``` python
arr = np.loadtxt("data.txt")
```

------------------------------------------------------------------------

# 6. Reading CSV (`genfromtxt`)

``` python
arr = np.genfromtxt(
    "students.csv",
    delimiter=",",
    skip_header=1
)
```

Useful for missing values.

------------------------------------------------------------------------

# 7. Writing CSV (`savetxt`)

``` python
np.savetxt(
    "output.csv",
    arr,
    delimiter=",",
    fmt="%d"
)
```

Flow

``` text
NumPy Array
      │
      ▼
 output.csv
```

------------------------------------------------------------------------

# 8. Binary vs Text

  Binary (.npy)   Text (.csv/.txt)
  --------------- ------------------
  Faster          Human readable
  Smaller         Larger
  NumPy native    Universal

------------------------------------------------------------------------

# Real-World Workflow

``` text
Sensor Data
      │
      ▼
 NumPy Array
      │
      ├── save(.npy)
      ├── savez(.npz)
      └── savetxt(.csv)
```

------------------------------------------------------------------------

# Common Mistakes

-   Loading CSV with `load()` instead of `loadtxt()` or `genfromtxt()`
-   Forgetting the delimiter
-   Using `loadtxt()` when missing values exist

------------------------------------------------------------------------

# Interview Questions

1.  Difference between `.npy` and `.npz`?
2.  When should `genfromtxt()` be used?
3.  Why is `.npy` faster than CSV?
4.  Difference between `savez()` and `savez_compressed()`?

------------------------------------------------------------------------

# Practice

1.  Save a 1D array.
2.  Save a 2D matrix.
3.  Load a saved array.
4.  Save two arrays into one file.
5.  Export a matrix to CSV.
6.  Read a CSV with headers.

------------------------------------------------------------------------

# Mind Map

``` text
NumPy File I/O
│
├── save
├── load
├── savez
├── savez_compressed
├── loadtxt
├── genfromtxt
└── savetxt
```

------------------------------------------------------------------------

# Cheat Sheet

``` python
np.save()
np.load()
np.savez()
np.savez_compressed()
np.loadtxt()
np.genfromtxt()
np.savetxt()
```

**Next Chapter:** Performance Optimization and Vectorization
