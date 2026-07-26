class Solution:
    """
    Provides multiple approaches to solve the Product of Array Except Self problem.

    Each method returns a new array where the element at index i is equal to
    the product of every element in the input array except nums[i].

    The implementations demonstrate different time and space complexity
    trade-offs, ranging from a brute-force solution to the optimal
    prefix/suffix approach.

    Constraints:
        2 <= nums.length <= 10^5
        -30 <= nums[i] <= 30
        The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
    """

    def product_except_self_brute_force(self, nums: list[int]) -> list[int]:
        """
        Compute the product of every element except the current one using a
        brute-force approach.

        For each index, iterate through the entire array and multiply every
        element except the one at the current index.

        Time: O(n^2)
        Space: O(1) auxiliary space (excluding the output array)
        """

        res = []

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            res.append(prod)

        return res


    def product_except_self_division(self, nums: list[int]) -> list[int]:
        """
        Compute the product of every element except the current one using
        division.

        The method first calculates the product of all non-zero elements while
        counting the number of zeros in the array. Special handling is required
        because division by zero is undefined.

        Cases:
            - More than one zero: every result is 0.
            - Exactly one zero: only the index containing the zero receives the
            product of the non-zero elements.
            - No zeros: divide the total product by the current element.

        Time: O(n)
        Space: O(1) auxiliary space (excluding the output array)
        """

        prod, zero_count = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero_count:
                res[i] = 0 if num else prod
            else:
                res[i] = prod // num

        return res


    def product_except_self_prefix_and_suffix(self, nums: list[int]) -> list[int]:
        """
        Compute the product of every element except the current one using
        separate prefix and suffix product arrays.

        The prefix array stores the product of all elements before each index,
        while the suffix array stores the product of all elements after each
        index. The final answer for each position is obtained by multiplying
        the corresponding prefix and suffix values.

        Time: O(n)
        Space: O(n) auxiliary space for the prefix and suffix arrays
        """

        n = len(nums)
        res = [0] * n
        prefixes = [0] * n
        suffixes = [0] * n

        prefixes[0] = suffixes[n - 1] = 1
        for i in range(1, n):
            prefixes[i] = nums[i - 1] * prefixes[i - 1]
        for i in range(n - 2, -1, -1):
            suffixes[i] = nums[i + 1] * suffixes[i + 1]

        for i in range(n):
            res[i] = prefixes[i] * suffixes[i]

        return res


    def product_except_self_prefix_and_suffix_optimal(self, nums: list[int]) -> list[int]:
        """
        Compute the product of every element except the current one using the
        optimal prefix/suffix technique.

        The result array is first populated with prefix products in a left-to-
        right pass. A second right-to-left pass multiplies each entry by the
        corresponding suffix product, eliminating the need for separate prefix
        and suffix arrays.

        This approach satisfies the problem's requirement of O(1) auxiliary
        space (excluding the output array).

        Time: O(n)
        Space: O(1)
        """

        res = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res



if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
    ]

    for nums, expected in test_cases:
        result = solution.product_except_self_prefix_and_suffix_optimal(nums)

        assert result == expected

        print(
            f"nums = {nums}\n"
            f"got = {result}, expected = {expected}\n"
        )

    print("#######################\nAll test cases passed!!\n#######################")