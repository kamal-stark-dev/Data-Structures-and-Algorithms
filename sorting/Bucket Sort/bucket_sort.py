from typing import TypeVar

T= TypeVar("T", int, float) # this is done io use `T` in decorators as the function can sort any numberic data type

def bucket_sort(nums: list[T]) -> list[T]:
    """
    Bucket Sort is a distribution based sorting algorithm that excels when input values are spread relatively evenly across a known range.

    Check the Nodes.md file for it's working.

    Time: Best - O(n), Average - O(n + k), Worst: O(n ^ 2)
    Space: O(n + k), extra space for buckets

    n = number of elements
    k = number of buckets
    """

    if not nums:
        return nums

    min_value = min(nums)
    max_value = max(nums)

    if min_value == max_value:
        return nums # all elements are same

    bucket_count = len(nums)
    buckets: list[list[T]] = [[] for _ in range(bucket_count)]

    bucket_range = (max_value - min_value) / bucket_count

    for num in nums:
        # Calculate index and cap it to prevent out-of-bounds for max_value
        idx = int((num - min_value) / bucket_range)
        if idx >= bucket_count: # in case of max_value
            idx = bucket_count - 1
        buckets[idx].append(num)

    result: list[T] = []

    for bucket in buckets:
        bucket.sort() # Timsort handles small bucket sorting optimally
        result.extend(bucket)

    return result


def bucket_sort_visulize(nums: list[T]) -> list[T]:
    """
    Bucket sort implementation + visualization of all the steps in console.
    """

    if not nums:
        return nums

    min_value = min(nums)
    max_value = max(nums)

    if min_value == max_value:
        return nums

    bucket_count = len(nums)
    buckets: list[list[T]] = [[] for _ in range(bucket_count)]
    bucket_range = (max_value - min_value) / bucket_count

    print(f"\nInput List: {nums}")
    print(f"Range Config: Min = {min_value}, Max = {max_value}")
    print(f"Bucket Range Size = {bucket_range:.2f}\n")
    print("--- Distribution Step ---")

    for num in nums:
        idx = int((num - min_value) / bucket_range)
        if idx >= bucket_count:
            idx = bucket_count - 1

        buckets[idx].append(num)

        # Print current state of buckets after adding this number
        print(f"Added {num:5} -> Calculated Index: {idx}")
        for i, b in enumerate(buckets):
            print(f"* Bucket [{i}]: {b}")
        print("-------------------------\n")

    print("--- Sorting & Flattening Step ---")
    result: list[T] = []
    for i, bucket in enumerate(buckets):
        prev_bucket = bucket.copy()
        bucket.sort()
        print(f"> Bucket [{i}] before sort: {prev_bucket} -> sorted: {bucket}")
        result.extend(bucket)

    print(f"\n>> Final Sorted List: {result}")
    return result


if __name__ == "__main__":
    # test with integers
    ints = [42, 32, 33, 52, 37, 47, 51]
    print('Sorted nums:', bucket_sort(ints))

    # Test with floats
    floats = [42.85, 12.04, 89.31, 3.14, 67.59, 23.48, 95.12, 54.76, 8.90, 31.25]
    print('Sorted floats:', bucket_sort(floats))

    # Standard unsorted numbers
    # test_nums = [42, 10, 33, 52, 21]
    test_nums = [10, 11, 14, 20, 43]
    bucket_sort_visulize(test_nums)