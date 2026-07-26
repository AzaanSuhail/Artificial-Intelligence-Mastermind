# Chapter 19: NumPy Structured Arrays and Record Arrays

> **Goal:** Learn how to store heterogeneous (mixed-type) data
> efficiently using Structured Arrays and Record Arrays.

------------------------------------------------------------------------

# Why Structured Arrays?

A normal NumPy array stores only one data type.

``` python
import numpy as np

arr = np.array([1, 2, 3])
```

But real-world datasets contain multiple data types.

Example:

``` text
Student Database

+----+---------+------+-------+
| ID | Name    | Age  | Marks |
+----+---------+------+-------+
|101 | Alice   |  20  |  89.5 |
|102 | Bob     |  21  |  92.0 |
+----+---------+------+-------+
```

Structured arrays allow storing all these fields in one NumPy array.

------------------------------------------------------------------------

# 1. Creating a Structured Array

``` python
dtype = [
    ("id", "i4"),
    ("name", "U10"),
    ("age", "i4"),
    ("marks", "f4")
]

students = np.array([
    (101, "Alice", 20, 89.5),
    (102, "Bob", 21, 92.0)
], dtype=dtype)

print(students)
```

Visualization

``` text
students

┌────┬────────┬─────┬────────┐
│ id │ name   │ age │ marks  │
├────┼────────┼─────┼────────┤
│101 │ Alice  │ 20  │ 89.5   │
│102 │ Bob    │ 21  │ 92.0   │
└────┴────────┴─────┴────────┘
```

------------------------------------------------------------------------

# 2. Accessing Fields

``` python
print(students["name"])
print(students["marks"])
```

Visualization

``` text
students["name"]

Alice
Bob
```

------------------------------------------------------------------------

# 3. Accessing One Record

``` python
print(students[0])
```

``` text
(101, 'Alice', 20, 89.5)
```

------------------------------------------------------------------------

# 4. Updating Values

``` python
students["marks"][0] = 95
print(students)
```

``` text
Before

Alice → 89.5

↓

After

Alice → 95.0
```

------------------------------------------------------------------------

# 5. Filtering Structured Arrays

``` python
high = students[students["marks"] > 90]
print(high)
```

Visualization

``` text
Students
   │
Marks > 90 ?
   │
   ▼
Selected Records
```

------------------------------------------------------------------------

# 6. Sorting

``` python
sorted_students = np.sort(students, order="marks")
print(sorted_students)
```

``` text
Before

89.5
92.0

↓

Ascending Order
```

------------------------------------------------------------------------

# 7. Multiple Field Selection

``` python
print(students[["name", "marks"]])
```

------------------------------------------------------------------------

# 8. Record Arrays (`recarray`)

``` python
records = students.view(np.recarray)

print(records.name)
print(records.age)
```

Visualization

``` text
Structured Array

students["age"]

↓

Record Array

records.age
```

------------------------------------------------------------------------

# 9. Real-World Example

Employee Database

``` text
Employees
      │
      ▼
Structured Array
      │
      ├── id
      ├── name
      ├── salary
      └── department
```

------------------------------------------------------------------------

# Common Mistakes

-   Forgetting to define the dtype.
-   Using inconsistent field names.
-   Confusing normal arrays with structured arrays.
-   Accessing fields that do not exist.

------------------------------------------------------------------------

# Interview Questions

1.  What is a structured array?
2.  Difference between structured arrays and normal arrays?
3.  What is a record array?
4.  When should structured arrays be used?
5.  How do you sort by a specific field?

------------------------------------------------------------------------

# Practice

1.  Create an employee database.
2.  Filter employees with salary \> 50000.
3.  Sort by age.
4.  Update a student's marks.
5.  Access only names.
6.  Convert to a record array.

------------------------------------------------------------------------

# Mind Map

``` text
Structured Arrays
│
├── dtype
├── Fields
├── Records
├── Filtering
├── Sorting
├── recarray
└── Real-world Data
```

------------------------------------------------------------------------

# Cheat Sheet

``` python
dtype=[("id","i4"),
       ("name","U20"),
       ("age","i4"),
       ("marks","f4")]

np.array(..., dtype=dtype)

students["name"]
students["marks"]

np.sort(students, order="marks")

students.view(np.recarray)
```

**Next Chapter:** NumPy Memory Layout, Strides, and Advanced Internals
