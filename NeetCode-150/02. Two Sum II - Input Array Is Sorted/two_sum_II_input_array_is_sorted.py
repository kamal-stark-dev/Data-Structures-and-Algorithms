class Solution:
    """
    Problem:
        -

    Approach:
        1.
        2.
        3.

    Constraints:
        -

    Notes:
        -
    """

    def two_sum_II_sorted_brute(self, nums: list[int], target: int) -> list[int]:
        """
        Intuition:
            -

        Algorithm:
            -

        Time:
            O()

        Space:
            O()
        """

        n = len(nums)

        for i in range(n):
            rem = target - nums[i]

            for j in range(i + 1, n):
                if nums[j] == rem:
                    return [i + 1, j + 1]

        return [-1, -1] # not found

    def two_sum_II_sorted_binary_search(self, nums: list[int], target: int) -> list[int]:
        """
        Intuition:
            -

        Algorithm:
            -

        Time:
            O()

        Space:
            O()
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


    def two_sum_II_sorted_hash_map(self, nums: list[int], target: int) -> list[int]:
        """
        Intuition:
            -

        Algorithm:
            -

        Time:
            O()

        Space:
            O()
        """

        seen = {}

        for i, num in enumerate(nums):
            rem = target - num

            if rem in seen:
                return [seen[rem] + 1, i + 1]

            seen[num] = i

        return [-1, -1]

    def two_sum_II_sorted_two_pointers(self, nums: list[int], target: int) -> list[int]:
        """
        Intuition:
            -

        Algorithm:
            -

        Time:
            O()

        Space:
            O()
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