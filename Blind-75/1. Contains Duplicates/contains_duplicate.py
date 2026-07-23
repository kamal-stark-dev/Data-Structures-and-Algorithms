class Solution:
    """Different approaches for detecting duplicate elements in a list."""

    def contains_duplicate_brute_force(self, nums: list[int]) -> bool:
        """
        Return True if the list contains duplicate values.

        Time: O(n^2)
        Space: O(1)
        """

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


    def contains_duplicate_sorting(self, nums: list[int]) -> bool:
        """
        Return True if the list contains duplicate values.

        Time: O(n logn)
        Space: O(n) -> due to sorted_nums
        """

        sorted_nums = sorted(nums)

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                return True
        return False


    def contains_duplicate_hash_set(self, nums: list[int]) -> bool:
        """
        Return True if the list contains duplicate values.

        Time: O(n)
        Space: O(n) -> seen set size
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


    def contains_duplicate(self, nums: list[int]) -> bool:
        """
        Return True if the list contains duplicate values. (Concise implementation)

        Time: O(n)
        Space: O(n)
        """

        return len(nums) != len(set(nums))


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([1], False)
    ]

    for nums, expected_output in test_cases:
        result = solution.contains_duplicate(nums)

        assert result == expected_output

        print(
            f"Input: {nums}\n"
            "Expected: {expected_output}, Got: {result}\n"
        )

    print("#######################\nAll test cases passed!!\n#######################")
