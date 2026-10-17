class Solution:
    """
    Problem:
        Given a sorted array of unique integers nums and an integer target,
        return the index of target if it exists in nums. Otherwise, return -1.

        The algorithm must run in O(log n) time.

    Approach:
        1. Use binary search to repeatedly divide the search space in half.
        2. Compare the middle element with the target to determine which
           half may contain the target.
        3. Return the target's index if found; otherwise, return -1 when
           the search space becomes empty.

    Constraints:
        - 1 <= nums.length <= 10^4
        - -10^4 < nums[i], target < 10^4
        - All integers in nums are unique.
        - nums is sorted in ascending order.
        - Runtime complexity must be O(log n).

    Notes:
        - Binary search requires the input array to be sorted.
        - Each iteration or recursive call eliminates approximately half
          of the remaining search space.
        - The recursive implementation uses O(log n) auxiliary space
          because of the call stack.
        - The iterative implementation uses O(1) auxiliary space.
        - Lower-bound and upper-bound approaches can also locate the first
          or last occurrence of a target in arrays containing duplicates.
    """

    def binary_search_recursive(self, nums: list[int], target: int) -> int:
        """
        Intuition:
            Recursively divide the sorted array into smaller search spaces.
            Compare the target with the middle element and continue searching
            only the half where the target could exist.

        Algorithm:
            1. Initialize the search boundaries to the entire array.
            2. If left > right, the search space is empty; return -1.
            3. Calculate the middle index and compare nums[mid] with target.
            4. If they are equal, return mid.
            5. If nums[mid] > target, recursively search the left half.
            6. Otherwise, recursively search the right half.
            7. Return -1 if the target is not found.

        Time:
            O(log n) - The search space is halved at each recursive call.

        Space:
            O(log n) - The recursion call stack grows logarithmically.
        """

        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                return binary_search(left, mid - 1)

            return binary_search(mid + 1, right)

        return binary_search(0, len(nums) - 1)

    def binary_search_iterative(self, nums: list[int], target: int) -> int:
        """
        Intuition:
            Maintain a search interval using two pointers, left and right.
            Repeatedly inspect the middle element and discard the half
            that cannot contain the target.

        Algorithm:
            1. Initialize left to 0 and right to len(nums) - 1.
            2. While left <= right:
                a. Calculate the middle index.
                b. If nums[mid] == target, return mid.
                c. If nums[mid] > target, move right to mid - 1.
                d. Otherwise, move left to mid + 1.
            3. If the search interval becomes empty, return -1.

        Time:
            O(log n) - Each iteration halves the remaining search space.

        Space:
            O(1) - Only a constant number of variables are used.
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def binary_search_upper_bound(self, nums: list[int], target: int) -> int:
        """
        Intuition:
            Find the upper bound of target, defined as the first index
            containing an element strictly greater than target.

            If target exists, the element immediately before the upper bound
            is its last occurrence. Since the array contains unique integers,
            this is also the target's only occurrence.

        Algorithm:
            1. Initialize the search interval to [0, len(nums)).
            2. While left < right:
                a. Calculate the middle index.
                b. If nums[mid] > target, move right to mid.
                c. Otherwise, move left to mid + 1.
            3. The converged left index is the upper bound.
            4. If the previous element equals target, return left - 1.
            5. Otherwise, return -1.

        Time:
            O(log n) - The search interval is halved at each iteration.

        Space:
            O(1) - The search is iterative and uses constant extra space.
        """

        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return left - 1 if (left and nums[left - 1] == target) else -1

    def binary_search_lower_bound(self, nums: list[int], target: int) -> int:
        """
        Intuition:
            Find the lower bound of target, defined as the first index
            containing an element greater than or equal to target.

            If the element at that index equals target, return its index.
            Otherwise, target does not exist in the array.

        Algorithm:
            1. Initialize the search interval to [0, len(nums)).
            2. While left < right:
                a. Calculate the middle index.
                b. If nums[mid] >= target, move right to mid.
                c. Otherwise, move left to mid + 1.
            3. When the pointers converge, left is the lower bound.
            4. If left is within the array and nums[left] == target,
               return left.
            5. Otherwise, return -1.

        Time:
            O(log n) - The search interval is halved at each iteration.

        Space:
            O(1) - The search is iterative and uses constant extra space.
        """

        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left if (left < len(nums) and nums[left] == target) else -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], target: int, expected: int)
        (
            [-1, 0, 3, 5, 9, 12],
            9,
            4
        ),
        (
            [-1, 0, 3, 5, 9, 12],
            2,
            -1
        ),
    ]

    for nums, target, expected in test_cases:
        result = solution.binary_search_lower_bound(nums, target)

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