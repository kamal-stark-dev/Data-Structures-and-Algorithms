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

    def missing_number_sorting(self, nums: list[int]) -> int:
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

        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)

    def missing_number_hash_set(self, nums: list[int]) -> int:
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

        num_set = set(nums)

        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

    def missing_number_xor(self, nums: list[int]) -> int:
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

        xorr = len(nums)

        for i in range(len(nums)):
            xorr ^= i ^ nums[i]

        return xorr

    def missing_number_math(self, nums: list[int]) -> int:
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

        actual_sum = 0

        n = len(nums)

        intended_sum = (n * (n + 1)) // 2

        for num in nums:
            actual_sum += num

        return intended_sum - actual_sum


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], expected: int)
        (
            [3, 0, 1],
            2
        ),
        (
            [0, 1],
            2
        ),
        (
            [0],
            1
        ),
        (
            [4, 5, 0, 1, 2],
            3
        ),
    ]

    for nums, expected in test_cases:
        result = solution.missing_number_xor(nums)

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