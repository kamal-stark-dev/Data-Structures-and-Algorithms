# Bucket Sort

**Bucket Sort** is a _distribution_ sorting algorithm, which works by distributing the elements of array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.

> Bucket Sort is one of the fastest sorting algorithms when used under the right conditions. Unlike comparison-based algorithms like Merge or Quick Sort because it works by dividing the data into groups and sorting each group individually.

We make an assumption that the data we need to sort is _fairly evenly distributed_.

## Basic Idea

Suppose we have:

```
[42, 32, 33, 52, 37, 47, 51]
```

Create Buckets:

```
Bucket 0

Bucket 1

Bucket 2

Bucket 3
```

Distribute Numbers:

```
Bucket 0
32
33
37

Bucket 1
42
47

Bucket 2
51
52

Bucket 3
(empty)
```

Sort Each Bucket:

```
32 33 37

42 47

51 52
```

Merge:

```
32 33 37 42 47 51 52
```

Done.

## Bucket Sort Algorithm

1. **Create** `n` empty buckets
2. For every element:
   find the **correct bucket** and put the element in it
3. **Sort** every bucket
4. **Merge** all buckets
5. **Return** sorted array

### When to use Bucket Sort

**Bucket sort works best when**:

- Numbers are uniformly distributed
- Data range is known
- Floating-point numbers between 0 and 1
- Large datasets
- External sorting

**Examples**:

- Student grades
- Ages
- Temperatures
- Percentages
- Decimal values

## Complexity Analysis

1. **Best Case**: _O(n)_, buckets contain roughly equal numbers.
2. **Average Case**: _O(n + k)_, where n = number of elements and k = number of buckets.
3. **Worst Case**: _O(n^2)_, if every element goes into one bucket (as you'll be sorting one large bucket).
4. **Space Complexity**: _O(n + k)_, extra memory needed for buckets.

<br />

> **Q.** Why can Bucket Sort be faster than _O(n logn)_?
>
> \> Bucket Sort avoids excessive comparisons by **placing elements directly into their approximate final regions**.

If buckets are balanced:

```
10,000 numbers
    ↓
100 buckets
    ↓
100 numbers per bucket
    ↓
Each bucket sorts quickly
    ↓
Overall nearly O(n)
```

## Choosing Buckets

This is the most important part.

Too few buckets:

```
Bucket 1: 1100 elements
Bucket 2: 300 elements
```

_Bad_.

Too many buckets.

```
1000 buckets

Most empty!!
```

_Waste of memory_.

A common choice is:

```
Number of buckets = √n

OR

Number of buckets = n
```

_depending on the data_.

## Pros and Cons

**Pros**:

- Really fast for uniformly distributed data.
- Can achieve near linear time O(n).
- Simple concept, easy to parallelize since buckets can be sorted independently.
- Effective for floating point values and known ranges.

**Cons**:

- Performance depends heavily on good bucket distribution.
- Extra memory is required for the buckets.
- Worst-case complexity is O(n^2), if all the elements fall into one bucket.
- Not ideal when the input range is unknown or highly skewed.
- Requires careful bucket size selection.

## Optimizations

1. Use **Insertion Sort** for small buckets because it performs well on nearly sorted data.
2. Choose bucket sizes based on the data distribution instead of a fixed number.
3. Sort the buckets in parallel on multi-core systems.
4. Reuse bucket storage when sorting repeatedly to reduce allocation.

## Bucket Sort vs Other Sorting Algorithms

| Algorithm     | Best Case       | Average Case    | Worst Case      | Space Complexity | Stable | Notes                                          |
| ------------- | --------------- | --------------- | --------------- | ---------------- | ------ | ---------------------------------------------- |
| Bucket Sort   | **O(n)**        | **O(n + k)**    | **O(n²)**       | **O(n + k)**     | Yes\*  | Best for uniformly distributed data            |
| Merge Sort    | **O(n log n)**  | **O(n log n)**  | **O(n log n)**  | **O(n)**         | Yes    | Consistent performance                         |
| Quick Sort    | **O(n log n)**  | **O(n log n)**  | **O(n²)**       | **O(log n)**     | No     | Very fast in practice                          |
| Heap Sort     | **O(n log n)**  | **O(n log n)**  | **O(n log n)**  | **O(1)**         | No     | Memory efficient                               |
| Counting Sort | **O(n + k)**    | **O(n + k)**    | **O(n + k)**    | **O(k)**         | Yes    | Best for small integer ranges                  |
| Radix Sort    | **O(d(n + k))** | **O(d(n + k))** | **O(d(n + k))** | **O(n + k)**     | Yes    | Excellent for fixed-length integers or strings |

```
Notes:

`n` = Number of elements

`k` = Number of buckets (Bucket Sort) or range of input values (Counting/Radix Sort)

`d` = Number of digits (or characters) processed in Radix Sort

(Yes*) for Bucket Sort means it is stable only if the sorting algorithm used for each bucket is stable (e.g., Insertion Sort or Merge Sort).\*
```
