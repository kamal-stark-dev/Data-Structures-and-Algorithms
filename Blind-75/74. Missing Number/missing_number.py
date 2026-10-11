class Solution:
    """
    Problem:
        Given an array nums containing n distinct integers in the range
        [0, n], return the only number in the range that is missing.

    Approach:
        1. Sorting:
           Sort the array and find the first index where nums[i] != i.
        2. Hash Set:
           Store all elements in a set and check which number in [0, n]
           is absent.
        3. XOR:
           XOR all indices and array elements, including n, to find
           the missing number.
        4. Mathematical Sum:
           Calculate the expected sum of numbers from 0 to n and
           subtract the actual sum of the array.

    Constraints:
        - n == len(nums)
        - 1 <= n <= 10^4
        - 0 <= nums[i] <= n
        - All elements in nums are distinct.
        - Exactly one number from [0, n] is missing.

    Notes:
        - The array contains n elements, but the range [0, n] has n + 1
          numbers.
        - Sorting modifies the original array.
        - The XOR and mathematical approaches use O(1) auxiliary space
          and O(n) time, satisfying the follow-up requirement.
    """

    def missing_number_sorting(self, nums: list[int]) -> int:
        """
        Intuition:
            If every number were present in its correct sorted position,
            nums[i] would equal i. The first mismatch identifies the
            missing number.

        Algorithm:
            1. Sort nums in ascending order.
            2. Iterate through the array using indices from 0 to n - 1.
            3. If nums[i] != i, return i as the missing number.
            4. If every element matches its index, return n because
               the missing number must be the largest number.

        Time:
            O(n log n) - Sorting takes O(n log n); the scan takes O(n).

        Space:
            O(1) auxiliary space for the scan, assuming an in-place
            sorting implementation. Python's list.sort() may use
            O(n) auxiliary space in the worst case.
        """

        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)

    def missing_number_hash_set(self, nums: list[int]) -> int:
        """
        Intuition:
            A set provides average O(1) membership checks. By checking
            every number in [0, n], we can identify the absent number.

        Algorithm:
            1. Convert nums into a set for efficient lookups.
            2. Iterate through every integer from 0 to n, inclusive.
            3. Return the first integer that is not present in the set.

        Time:
            O(n) average time to build the set and search for the
            missing number.

        Space:
            O(n) auxiliary space to store the elements in the set.
        """

        num_set = set(nums)

        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

    def missing_number_xor(self, nums: list[int]) -> int:
        """
        Intuition:
            XOR has two important properties:
                a ^ a = 0
                a ^ 0 = a

            XORing a number with itself cancels it out. If we XOR every
            number from 0 to n with every element in nums, all present
            numbers cancel out, leaving only the missing number.

        Algorithm:
            1. Initialize xorr with n, the largest possible number.
            2. For every index i, XOR xorr with both i and nums[i].
            3. Return xorr, which contains the missing number.

        Time:
            O(n) because we process every array element once.

        Space:
            O(1) auxiliary space because only a constant number of
            variables are used.
        """

        xorr = len(nums)

        for i in range(len(nums)):
            xorr ^= i ^ nums[i]

        return xorr

    def missing_number_math(self, nums: list[int]) -> int:
        """
        Intuition:
            The sum of all integers from 0 to n is n * (n + 1) // 2.
            Subtracting the sum of the array from this expected sum
            gives the missing number.

        Algorithm:
            1. Let n be the length of nums.
            2. Calculate the expected sum of integers from 0 to n.
            3. Calculate the actual sum of all elements in nums.
            4. Return the expected sum minus the actual sum.

        Time:
            O(n) because we iterate through nums once to calculate
            its sum.

        Space:
            O(1) auxiliary space because only a constant number of
            variables are used.
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
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([0], 1),
        ([4, 5, 0, 1, 2], 3),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
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