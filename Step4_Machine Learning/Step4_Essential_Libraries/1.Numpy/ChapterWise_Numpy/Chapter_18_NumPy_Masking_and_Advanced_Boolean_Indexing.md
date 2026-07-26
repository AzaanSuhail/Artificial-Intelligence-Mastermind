# Chapter 18: NumPy Masking and Advanced Boolean Indexing

> **Goal:** Learn how to filter, clean, and transform data efficiently
> using Boolean masks.

------------------------------------------------------------------------

# 1. What is Boolean Masking?

A Boolean mask is an array of `True` and `False` values used to select
elements.

``` python
import numpy as np

arr = np.array([10, 25, 30, 45, 50])
mask = arr > 30
print(mask)
```

Visualization

``` text
Values : 10   25   30   45   50
Mask   :  F    F    F    T    T
                │         │
                └─────────┴── Selected
```

------------------------------------------------------------------------

# 2. Filtering Data

``` python
print(arr[arr > 30])
```

``` text
Original
[10 25 30 45 50]

Mask
[F F F T T]

Result
[45 50]
```

------------------------------------------------------------------------

# 3. Multiple Conditions

``` python
mask = (arr > 20) & (arr < 50)
print(arr[mask])
```

Visualization

``` text
Condition 1 : >20
Condition 2 : <50

      AND (&)

      ▼

Selected Values
```

Use: - `&` → AND - `|` → OR - `~` → NOT

------------------------------------------------------------------------

# 4. np.where()

``` python
result = np.where(arr > 30, "High", "Low")
print(result)
```

``` text
Condition
    │
 ┌──┴──┐
True False
 │      │
High   Low
```

------------------------------------------------------------------------

# 5. np.select()

``` python
conditions=[arr<20, arr<40]
choices=["Low","Medium"]

print(np.select(conditions,choices,default="High"))
```

Useful for multiple conditions.

------------------------------------------------------------------------

# 6. np.putmask()

``` python
a=np.array([1,2,3,4,5])

np.putmask(a,a>3,99)

print(a)
```

``` text
Before
[1 2 3 4 5]

Mask (>3)

After
[1 2 3 99 99]
```

------------------------------------------------------------------------

# 7. Masked Arrays

``` python
masked=np.ma.masked_greater(arr,30)
print(masked)
```

Visualization

``` text
10 25 30 -- --
```

Masked values are ignored in many computations.

------------------------------------------------------------------------

# 8. Missing Values

``` python
data=np.array([1,np.nan,5,np.nan])

print(np.isnan(data))
```

``` text
Data
1 NaN 5 NaN

Mask
F  T  F  T
```

------------------------------------------------------------------------

# 9. Replace Missing Values

``` python
clean=np.where(np.isnan(data),0,data)
print(clean)
```

------------------------------------------------------------------------

# Real-World Example

``` text
CSV Dataset
     │
     ▼
Load into NumPy
     │
     ▼
Create Boolean Mask
     │
     ▼
Filter Invalid Rows
     │
     ▼
Clean Dataset
```

------------------------------------------------------------------------

# Common Mistakes

-   Using `and` instead of `&`
-   Forgetting parentheses around conditions
-   Confusing `=` with `==`
-   Ignoring `NaN` values

------------------------------------------------------------------------

# Interview Questions

1.  What is Boolean masking?
2.  Difference between `where()` and Boolean indexing?
3.  Why are parentheses required?
4.  When should masked arrays be used?
5.  Difference between `putmask()` and `where()`?

------------------------------------------------------------------------

# Practice

1.  Select values greater than 50.
2.  Filter even numbers.
3.  Replace negatives with zero.
4.  Detect NaN values.
5.  Categorize marks using `where()`.
6.  Use `np.select()` with three conditions.

------------------------------------------------------------------------

# Mind Map

``` text
Boolean Indexing
│
├── Masks
├── Filtering
├── AND / OR / NOT
├── where
├── select
├── putmask
├── Masked Arrays
└── Missing Values
```

------------------------------------------------------------------------

# Cheat Sheet

``` python
arr>5
arr[arr>5]
(arr>5)&(arr<20)
(arr<5)|(arr>50)
~(arr>5)

np.where(...)
np.select(...)
np.putmask(...)
np.isnan(...)
np.ma.masked_greater(...)
```

**Next Chapter:** NumPy Structured Arrays and Record Arrays
