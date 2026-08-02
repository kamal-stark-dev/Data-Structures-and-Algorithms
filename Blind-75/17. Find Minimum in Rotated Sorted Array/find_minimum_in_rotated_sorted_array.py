class Solution:
    """
    Problem:
        Given a sorted array of unique integers that has been rotated between
        1 and n times, return the minimum element in the array.

        The original array is sorted in ascending order before rotation.

    Approach:
        1. Linear Search:
           - Simply return the minimum value using Python's built-in min().
           - Simple but does not satisfy the O(log n) requirement.

        2. Binary Search:
           - Use the sorted property of each half to determine where the
             rotation point (minimum element) lies.
           - If the current search window is already sorted, the leftmost
             element is the minimum.
           - Otherwise, eliminate one half of the search space each iteration.

        3. Lower Bound Binary Search:
           - Compare the middle element with the rightmost element.
           - If nums[mid] < nums[right], the minimum lies in the left half
             (including mid).
           - Otherwise, the minimum lies in the right half (excluding mid).
           - Continue until both pointers converge.

    Constraints:
        - 1 <= len(nums) <= 5000
        - -5000 <= nums[i] <= 5000
        - All elements are unique.
        - nums is sorted in ascending order and rotated between 1 and n times.

    Notes:
        - The linear search solution is included for completeness.
        - The binary search solutions leverage the rotated sorted array property.
        - The lower-bound binary search is the cleanest and most common solution.
    """

    def minimum_in_rotated_sorted_array_linear_search(self, nums: list[int]) -> int:
        """
        Intuition:
            Since every element is inspected, the smallest value can be found
            directly using Python's built-in min() function.

        Algorithm:
            - Return min(nums).

        Time:
            O(n)

        Space:
            O(1)
        """

        return min(nums)


    def minimum_in_rotated_sorted_array_binary_search(self, nums: list[int]) -> int:
        """
        Intuition:
            A rotated sorted array always has at least one sorted half.

            If the current search window is already sorted, the leftmost element
            is the minimum. Otherwise, determine which half contains the rotation
            point by comparing the middle element with the left boundary.

        Algorithm:
            - Initialize the result as the first element.
            - While the search window is valid:
                - If the current window is already sorted, update the result with
                nums[left] and terminate.
                - Compute the middle index and update the result.
                - If the left half is sorted, search the right half.
                - Otherwise, search the left half.
            - Return the minimum found.

        Time:
            O(log n)

        Space:
            O(1)
        """

        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = left + (right - left) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res


    def minimum_in_rotated_sorted_array_lower_bound(self, nums: list[int]) -> int:
        """
        Intuition:
            The minimum element is the first value where the sorted order "wraps
            around."

            By comparing nums[mid] with nums[right], we can determine which side
            contains the minimum:
                - nums[mid] < nums[right]:
                    The right half is sorted, so the minimum is at mid or to
                    its left.
                - nums[mid] > nums[right]:
                    The minimum must lie strictly to the right of mid.

            Repeating this process narrows the search until both pointers meet at
            the minimum element.

        Algorithm:
            - Initialize left and right pointers.
            - While left < right:
                - Compute the middle index.
                - If nums[mid] < nums[right]:
                    - Move right to mid.
                - Otherwise:
                    - Move left to mid + 1.
            - Return nums[left].

        Time:
            O(log n)

        Space:
            O(1)
        """

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], expected)
        ([3,4,5,1,2], 1),
        ([4,5,6,7,0,1,2], 0),
        ([11, 13, 15, 17], 11)
    ]

    for nums, expected in test_cases:
        result = solution.minimum_in_rotated_sorted_array_lower_bound(nums)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")