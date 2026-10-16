class Solution:
    """
    Problem:
        Given a 1-indexed integer array `numbers` sorted in non-decreasing
        order and an integer `target`, find two distinct elements whose
        sum equals `target`.

        Return their 1-based indices as [index1, index2], where
        index1 < index2.

        Exactly one solution exists, and the same element cannot be
        used twice.

    Approach:
        1. Brute Force:
           Check every possible pair of elements until their sum equals
           the target.

        2. Binary Search:
           For each element, binary search the remaining portion of the
           sorted array for its complement.

        3. Hash Map:
           Store previously visited elements and their indices to find
           the complement in constant average time.

        4. Two Pointers:
           Start with pointers at both ends of the sorted array.
           Move the left pointer right if the sum is too small, or move
           the right pointer left if the sum is too large.

    Constraints:
        - 2 <= numbers.length <= 3 * 10^4
        - -1000 <= numbers[i] <= 1000
        - numbers is sorted in non-decreasing order.
        - -1000 <= target <= 1000
        - Exactly one solution exists.
        - The same element cannot be used twice.
        - The required output contains 1-based indices.

    Notes:
        - The array is already sorted, enabling binary search and the
          two-pointer technique.
        - The problem requires constant extra space, making the
          two-pointer approach the optimal solution.
        - The hash map approach uses additional space and therefore
          does not satisfy the constant-extra-space requirement.
        - The brute-force and binary-search approaches also use
          constant auxiliary space.
    """

    def two_sum_II_sorted_brute(
        self, nums: list[int], target: int
    ) -> list[int]:
        """
        Intuition:
            Try every possible pair of distinct elements. If their sum
            equals the target, return their 1-based indices.

        Algorithm:
            1. Iterate through each element using index i.
            2. Calculate the required complement: target - nums[i].
            3. Iterate through every subsequent element using index j.
            4. If nums[j] equals the complement, return [i + 1, j + 1].
            5. If no pair is found, return [-1, -1].

        Time:
            O(n^2), where n is the length of the array. Each element
            may be compared with every subsequent element.

        Space:
            O(1), because only a constant number of variables are used.
        """

        n = len(nums)

        for i in range(n):
            rem = target - nums[i]

            for j in range(i + 1, n):
                if nums[j] == rem:
                    return [i + 1, j + 1]

        return [-1, -1]  # not found

    def two_sum_II_sorted_binary_search(
        self, nums: list[int], target: int
    ) -> list[int]:
        """
        Intuition:
            Since the array is sorted, binary search can efficiently
            locate the complement of each element in the remaining
            portion of the array.

        Algorithm:
            1. Iterate through each element using index i.
            2. Calculate its complement: target - nums[i].
            3. Initialize binary search boundaries to i + 1 and n - 1,
               ensuring the same element is never used twice.
            4. Calculate the middle index of the search range.
            5. If nums[mid] equals the complement, return
               [i + 1, mid + 1].
            6. If nums[mid] is greater than the complement, search the
               left half; otherwise, search the right half.
            7. If no pair is found, return [-1, -1].

        Time:
            O(n log n), because binary search takes O(log n) for each
            of the n elements.

        Space:
            O(1), because binary search uses only a constant number
            of additional variables.
        """

        n = len(nums)

        for i in range(n):
            rem = target - nums[i]

            left, right = i + 1, n - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == rem:
                    return [i + 1, mid + 1]
                elif nums[mid] > rem:
                    right = mid - 1
                else:
                    left = mid + 1

        return [-1, -1]

    def two_sum_II_sorted_hash_map(
        self, nums: list[int], target: int
    ) -> list[int]:
        """
        Intuition:
            For each element, check whether its complement has already
            been visited. A hash map allows average O(1) lookup time.

        Algorithm:
            1. Initialize an empty hash map to store each visited
               number and its 0-based index.
            2. Iterate through the array using enumerate().
            3. Calculate the complement: target - num.
            4. If the complement exists in the hash map, return the
               stored index and the current index, converted to 1-based.
            5. Otherwise, store the current number and its index.
            6. If no pair is found, return [-1, -1].

        Time:
            O(n) average, because each hash map lookup and insertion
            takes O(1) average time.

        Space:
            O(n), because the hash map may store up to n elements.

        Note:
            Although efficient, this approach does not satisfy the
            problem's constant-extra-space requirement.
        """

        seen = {}

        for i, num in enumerate(nums):
            rem = target - num

            if rem in seen:
                return [seen[rem] + 1, i + 1]

            seen[num] = i

        return [-1, -1]

    def two_sum_II_sorted_two_pointers(
        self, nums: list[int], target: int
    ) -> list[int]:
        """
        Intuition:
            Because the array is sorted, the sum of the leftmost and
            rightmost elements provides useful information about which
            pointer to move.

            - If the sum equals the target, the solution is found.
            - If the sum is too large, move the right pointer left.
            - If the sum is too small, move the left pointer right.

        Algorithm:
            1. Initialize left = 0 and right = len(nums) - 1.
            2. While left < right, calculate the sum of the elements
               at both pointers.
            3. If the sum equals the target, return
               [left + 1, right + 1].
            4. If the sum exceeds the target, decrement right.
            5. Otherwise, increment left.
            6. If no pair is found, return [-1, -1].

        Time:
            O(n), because each iteration moves one pointer toward the
            other, and each pointer moves at most n positions.

        Space:
            O(1), because only two pointers and a constant number of
            additional variables are used.

        Note:
            This is the optimal approach for the problem because it
            achieves linear time complexity while satisfying the
            constant-extra-space requirement.
        """

        left, right = 0, len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]

            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], target: int, expected: list[int])
        (
            [2, 7, 11, 15],
            9,
            [1, 2]
        ),
        (
            [2, 3, 4],
            6,
            [1, 3]
        ),
        (
            [-1, 0],
            -1,
            [1, 2]
        ),
    ]

    for nums, target, expected in test_cases:
        result = solution.two_sum_II_sorted_binary_search(nums, target)

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