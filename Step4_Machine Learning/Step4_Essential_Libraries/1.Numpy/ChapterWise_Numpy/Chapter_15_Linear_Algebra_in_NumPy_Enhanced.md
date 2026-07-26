# Chapter 15: Linear Algebra in NumPy (Enhanced with Visualizations)

> **Goal:** Learn Linear Algebra using diagrams, visuals, and practical
> NumPy examples.

------------------------------------------------------------------------

# 1. What is a Matrix?

A matrix is a table of numbers arranged in rows and columns.

``` text
Rows ↓

      Col0 Col1 Col2
      ┌─────────────┐
Row0  │  1    2    3│
Row1  │  4    5    6│
      └─────────────┘

Shape = (2,3)
```

``` python
import numpy as np
A = np.array([[1,2,3],
              [4,5,6]])
print(A.shape)
```

------------------------------------------------------------------------

# 2. Matrix Multiplication

## Rule

``` text
(m×n) × (n×p) = (m×p)

(2×3) × (3×2) ✓
(2×3) × (2×3) ✗
```

``` python
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(A @ B)
```

### Visualization

``` text
      A                    B

┌───────┐           ┌───────┐
│1   2  │           │5   6  │
│3   4  │    ×      │7   8  │
└───────┘           └───────┘

Result

(1×5+2×7)=19
(1×6+2×8)=22
(3×5+4×7)=43
(3×6+4×8)=50

┌────────┐
│19   22 │
│43   50 │
└────────┘
```

------------------------------------------------------------------------

# 3. Dot Product

``` python
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.dot(a,b))
```

``` text
[1 2 3]
 ·
[4 5 6]

=1×4 +2×5 +3×6

=32
```

------------------------------------------------------------------------

# 4. Outer Product

``` python
print(np.outer(a,b))
```

``` text
        4   5   6
      ┌────────────┐
1  →  │ 4   5   6  │
2  →  │ 8  10  12  │
3  →  │12  15  18  │
      └────────────┘
```

------------------------------------------------------------------------

# 5. Transpose

``` python
print(A.T)
```

``` text
Before

1 2 3
4 5 6

      ↓

1 4
2 5
3 6
```

------------------------------------------------------------------------

# 6. Determinant

``` python
M=np.array([[2,1],[3,4]])
print(np.linalg.det(M))
```

Visualization

``` text
If det(A)=0
      │
      ▼
No Inverse Exists

If det(A)≠0
      │
      ▼
Inverse Exists
```

------------------------------------------------------------------------

# 7. Matrix Inverse

``` python
print(np.linalg.inv(M))
```

``` text
A
│
├─────► A⁻¹
│
└─────► A × A⁻¹ = I
```

------------------------------------------------------------------------

# 8. Solving Linear Equations

``` text
2x+y=5
x-y=1
```

``` python
A=np.array([[2,1],[1,-1]])
b=np.array([5,1])
print(np.linalg.solve(A,b))
```

Flow

``` text
Equations
   │
   ▼
Coefficient Matrix
   │
   ▼
np.linalg.solve()
   │
   ▼
Solution (x,y)
```

------------------------------------------------------------------------

# 9. Eigenvalues & Eigenvectors

``` python
vals, vecs = np.linalg.eig(M)
```

Applications

``` text
Data
 │
 ▼
Covariance Matrix
 │
 ▼
Eigenvalues
 │
 ▼
Principal Components (PCA)
```

------------------------------------------------------------------------

# 10. SVD

``` python
U,S,Vt=np.linalg.svd(M)
```

``` text
           A
           │
           ▼
     ┌──────────┐
     │   SVD    │
     └──────────┘
      /    |    \
     ▼     ▼     ▼
     U     Σ     Vᵀ
```

Uses: - Image compression - Recommendation systems - NLP

------------------------------------------------------------------------

# 11. QR Decomposition

``` python
Q,R=np.linalg.qr(M)
```

``` text
A
│
▼
QR
│
├── Q (Orthogonal)
└── R (Upper Triangular)
```

------------------------------------------------------------------------

# 12. Neural Network Visualization

``` text
Input Vector
      │
      ▼
Weight Matrix
      │
(Matrix Multiplication)
      │
      ▼
Activation
      │
      ▼
Prediction
```

------------------------------------------------------------------------

# Common Mistakes

-   Using `*` instead of `@`
-   Taking inverse of a non-square matrix
-   Ignoring `det(A)=0`

------------------------------------------------------------------------

# Practice

1.  Multiply two matrices.
2.  Find determinant.
3.  Compute inverse.
4.  Solve linear equations.
5.  Compute eigenvalues.
6.  Perform SVD.

------------------------------------------------------------------------

# Mind Map

``` text
Linear Algebra
│
├── Matrix
├── Dot Product
├── MatMul
├── Transpose
├── Determinant
├── Inverse
├── Solve
├── Eigen
├── SVD
└── QR
```

------------------------------------------------------------------------

# Cheat Sheet

``` python
A @ B
np.dot(a,b)
np.outer(a,b)
A.T
np.linalg.det(A)
np.linalg.inv(A)
np.linalg.solve(A,b)
np.linalg.eig(A)
np.linalg.svd(A)
np.linalg.qr(A)
```
