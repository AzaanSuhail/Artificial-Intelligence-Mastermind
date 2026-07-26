# Chapter 14: Random Number Generation in NumPy

> **Goal:** Learn how to generate random numbers, control randomness,
> and create reproducible experiments using NumPy.

------------------------------------------------------------------------

# Learning Objectives

After this chapter, you will be able to:

-   Generate random numbers
-   Create random integers and floating-point values
-   Sample random elements from arrays
-   Shuffle and permute data
-   Use random seeds for reproducibility
-   Use the modern `Generator` API
-   Generate values from common probability distributions

------------------------------------------------------------------------

# 1. Why Random Numbers?

Random numbers are used in:

-   Machine Learning
-   Data Science
-   Simulations
-   Games
-   Testing
-   Cryptography (specialized libraries are recommended for security)

``` python
import numpy as np
```

------------------------------------------------------------------------

# 2. `np.random.rand()`

Generates uniformly distributed numbers between **0 and 1**.

``` python
print(np.random.rand())
print(np.random.rand(3))
print(np.random.rand(2,3))
```

------------------------------------------------------------------------

# 3. `np.random.randn()`

Generates samples from the **standard normal distribution**.

``` python
print(np.random.randn(5))
```

-   Mean ≈ 0
-   Standard deviation ≈ 1

------------------------------------------------------------------------

# 4. `np.random.randint()`

Generate random integers.

``` python
print(np.random.randint(1, 10))
print(np.random.randint(1, 10, size=5))
print(np.random.randint(0, 100, size=(2,3)))
```

------------------------------------------------------------------------

# 5. `np.random.random()`

Another way to generate uniform random floats.

``` python
print(np.random.random((2,2)))
```

------------------------------------------------------------------------

# 6. `np.random.choice()`

Randomly select elements.

``` python
arr = np.array([10,20,30,40])

print(np.random.choice(arr))
print(np.random.choice(arr, size=3))
print(np.random.choice(arr, size=3, replace=False))
```

------------------------------------------------------------------------

# 7. `np.random.shuffle()`

Shuffles an array **in place**.

``` python
arr = np.array([1,2,3,4,5])

np.random.shuffle(arr)
print(arr)
```

------------------------------------------------------------------------

# 8. `np.random.permutation()`

Returns a shuffled copy.

``` python
arr = np.array([1,2,3,4])

print(np.random.permutation(arr))
print(arr)
```

The original array is unchanged.

------------------------------------------------------------------------

# 9. `np.random.seed()`

Makes results reproducible.

``` python
np.random.seed(42)

print(np.random.randint(1,10,5))
```

Running this again with the same seed produces identical output.

------------------------------------------------------------------------

# 10. Modern Generator API

NumPy recommends using `default_rng()`.

``` python
rng = np.random.default_rng(42)

print(rng.integers(1,10,size=5))
print(rng.random((2,2)))
```

Benefits:

-   Better random number algorithms
-   Independent generators
-   Preferred for new code

------------------------------------------------------------------------

# 11. Common Probability Distributions

Uniform:

``` python
rng.uniform(0, 1, size=5)
```

Normal:

``` python
rng.normal(0, 1, size=5)
```

Binomial:

``` python
rng.binomial(10, 0.5, size=5)
```

Poisson:

``` python
rng.poisson(3, size=5)
```

------------------------------------------------------------------------

# 12. Real-World Example

Split randomized training data.

``` python
indices = rng.permutation(100)

train = indices[:80]
test = indices[80:]
```

------------------------------------------------------------------------

# Common Mistakes

-   Forgetting to set a seed when reproducible results are required.
-   Using `shuffle()` when you need to preserve the original array.
-   Using the legacy API in new projects instead of `default_rng()`.

------------------------------------------------------------------------

# Interview Questions

### Q1

Difference between `shuffle()` and `permutation()`?

-   `shuffle()` modifies the original array.
-   `permutation()` returns a shuffled copy.

### Q2

Why use `default_rng()`?

It provides the modern, recommended random number generator with
improved design.

### Q3

What does a random seed do?

It initializes the generator so the same sequence of random numbers can
be reproduced.

### Q4

Difference between `rand()` and `randn()`?

-   `rand()` → Uniform distribution (0 to 1)
-   `randn()` → Standard normal distribution

------------------------------------------------------------------------

# Practice Questions

1.  Generate five random integers.
2.  Create a 3×3 matrix of random floats.
3.  Pick three unique values from an array.
4.  Shuffle an array in place.
5.  Create a shuffled copy using `permutation()`.
6.  Use `default_rng()` with a fixed seed.
7.  Generate samples from a normal distribution.
8.  Generate samples from a Poisson distribution.

------------------------------------------------------------------------

# Cheat Sheet

``` python
np.random.rand(3)
np.random.randn(3)
np.random.randint(1,10,size=5)
np.random.random((2,2))

np.random.choice(arr)
np.random.shuffle(arr)
np.random.permutation(arr)

np.random.seed(42)

rng = np.random.default_rng(42)
rng.random(5)
rng.integers(1,10,size=5)
rng.normal(0,1,size=5)
rng.uniform(0,1,size=5)
rng.binomial(10,0.5,size=5)
rng.poisson(3,size=5)
```

  Function          Purpose
  ----------------- -------------------------
  `rand()`          Uniform random floats
  `randn()`         Standard normal samples
  `randint()`       Random integers
  `choice()`        Random sampling
  `shuffle()`       Shuffle in place
  `permutation()`   Shuffled copy
  `seed()`          Reproducibility
  `default_rng()`   Modern random generator

**Next Chapter:** Linear Algebra in NumPy
