class Solution:
    """
    Problem:
        Given a sorted array of distinct integers that has been rotated at an
        unknown pivot, return the index of the target value if it exists.
        Otherwise, return -1.

    Approach:
        1. Implement a brute-force linear search for comparison.
        2. Use a modified binary search to achieve O(log n) runtime.

    Constraints:
        - 1 <= len(nums) <= 5000
        - -10^4 <= nums[i] <= 10^4
        - All values in nums are unique.
        - nums is sorted in ascending order before being rotated.
        - -10^4 <= target <= 10^4

    Notes:
        - A rotated sorted array always has at least one sorted half.
        - Exploiting the sorted half allows binary search to be applied even
        after rotation.
    """

    def search_in_rotated_sorted_array_brute_force(self, nums: list[int], target: int) -> int:
        """
        Intuition:
            Check every element one by one until the target is found.
            Since the array may be rotated, this approach ignores the ordering
            and simply performs a linear scan.

        Algorithm:
            1. Iterate through the array.
            2. If the current element equals the target, return its index.
            3. If the loop completes without finding the target, return -1.

        Time:
            O(n)

        Space:
            O(1)
        """

        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1


    def search_in_rotated_sorted_array_binary_search(self, nums: list[int], target: int) -> int:
        """
        Intuition:
            Even though the array is rotated, at least one half of the current
            search space is always sorted.

            By identifying the sorted half and checking whether the target lies
            within its range, we can safely discard the other half, preserving
            the efficiency of binary search.

        Algorithm:
            1. Initialize two pointers: left and right.
            2. Compute the middle index.
            3. If nums[mid] is the target, return mid.
            4. Determine whether the left half or the right half is sorted.
            5. If the target lies within the sorted half, continue searching
            there; otherwise, search the opposite half.
            6. Repeat until the target is found or the search space becomes empty.
            7. Return -1 if the target does not exist.

        Time:
            O(log n)

        Space:
            O(1)
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1



if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], target: int, expected: int)
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([11, 13, 15, 17], 11, 0),
    ]

    for nums, target, expected in test_cases:
        result = solution.search_in_rotated_sorted_array_binary_search(nums, target)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"nums = {nums}\n"
            f"target = {target}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"nums = {nums}\n"
            f"target = {target}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")