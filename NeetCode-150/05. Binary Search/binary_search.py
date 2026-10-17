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

    def binary_search(self, nums: list[int], target: int) -> int:
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

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


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
        result = solution.binary_search(nums, target)

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