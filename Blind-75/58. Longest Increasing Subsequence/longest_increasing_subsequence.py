from bisect import bisect_left

class Solution:
    """
    Problem:
        Given an integer array nums, return the length of the longest
        strictly increasing subsequence.

        A subsequence is formed by deleting zero or more elements without
        changing the relative order of the remaining elements.

    Approach:
        1. Brute force: Generate all possible subsequences using DFS and
           find the longest strictly increasing one.
        2. Memoization / Top-Down DP: For every index, calculate the length
           of the LIS starting from that index and reuse previously computed
           results.
        3. Tabulation / Bottom-Up DP: For every index, calculate the length
           of the LIS ending at that index using previously computed states.
        4. DP + Binary Search: Maintain a tails array where each position
           stores the smallest possible ending value for an increasing
           subsequence of that length.

    Constraints:
        1 <= nums.length <= 2500
        -10^4 <= nums[i] <= 10^4

    Notes:
        The subsequence does not need to be contiguous.
        The sequence must be strictly increasing, so equal values cannot
        extend an increasing subsequence.

        The four approaches take O(2^n), O(n^2), O(n^2), and O(n log n)
        time respectively.
    """

    def longest_increasing_subsequence_brute(self, nums: list[int]) -> int:
        """
        Intuition:
            At every index, we have two choices:
            1. Include nums[i] if it keeps the current subsequence
               strictly increasing.
            2. Skip nums[i].

            Exploring both choices generates every possible subsequence.
            We keep track of the maximum length found.

        Algorithm:
            1. Start DFS from index 0 with an empty current subsequence.
            2. If nums[i] can be appended while maintaining increasing order,
               include it and recursively process the next element.
            3. Backtrack and explore the option of skipping nums[i].
            4. When all elements have been processed, update maxLen.
            5. Return the maximum length found.

        Time:
            O(2^n)

        Space:
            O(n)
            The recursion depth and current subsequence can both reach n.
        """

        maxLen = 0

        def dfs(i: int, curr: list[int]) -> None:
            nonlocal maxLen

            if i == len(nums):
                maxLen = max(maxLen, len(curr))
                return

            if not curr or curr[-1] < nums[i]:
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()

            dfs(i + 1, curr)

        dfs(0, [])
        return maxLen

    def longest_increasing_subsequence_memoization(self, nums: list[int]) -> int:
        """
        Intuition:
            Define dfs(i) as the length of the longest increasing
            subsequence that starts at index i.

            From index i, we can extend the subsequence to any later index j
            where nums[j] > nums[i].

            Since the result for each index can be reused, memoization
            prevents the same subproblem from being solved repeatedly.

        Algorithm:
            1. Define dfs(i) to find the LIS starting from index i.
            2. If dfs(i) has already been calculated, return its memoized value.
            3. Initially, the LIS starting at i has length 1.
            4. Check every later index j.
            5. If nums[j] > nums[i], try extending the subsequence using
               dfs(j).
            6. Store the best result for index i in memo.
            7. Calculate dfs(i) for every index and return the maximum.

        Time:
            O(n^2)

        Space:
            O(n)
            For the memoization array and recursion stack.
        """

        def dfs(i: int) -> int:
            if memo[i] != -1:
                return memo[i]

            LIS = 1

            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            memo[i] = LIS
            return LIS

        n = len(nums)
        memo = [-1] * n

        return max(dfs(i) for i in range(n))

    def longest_increasing_subsequence_tabulation(self, nums: list[int]) -> int:
        """
        Intuition:
            Define dp[i] as the length of the longest increasing
            subsequence that ends at index i.

            To calculate dp[i], check every previous index j.
            If nums[j] < nums[i], then nums[i] can be appended to the
            increasing subsequence ending at j.

        Algorithm:
            1. Initialize dp[i] = 1 because every element forms an LIS
               of length 1 by itself.
            2. For every index i, check all previous indices j.
            3. If nums[j] < nums[i], update dp[i] using:
                   dp[i] = max(dp[i], dp[j] + 1)
            4. Keep track of the maximum dp value.
            5. Return the maximum value.

        Time:
            O(n^2)

        Space:
            O(n)
            The dp array stores the LIS length ending at each index.
        """

        n = len(nums)
        dp = [1] * n

        res = 0

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

            res = max(res, dp[i])

        return res

    def longest_increasing_subsequence_dp_and_binary_search(self, nums: list[int]) -> int:
        """
        Intuition:
            Maintain a tails array where tails[i] represents the smallest
            possible ending value of an increasing subsequence of length
            i + 1.

            For each number, use binary search to find the first position
            whose value is greater than or equal to that number.

            Replacing that value gives us a smaller or equal tail, which
            makes it easier to build a longer increasing subsequence later.

            The tails array does not necessarily contain the actual LIS.
            It only stores the best possible tail values for subsequences
            of different lengths.

        Algorithm:
            1. Initialize an empty tails array.
            2. For every number in nums:
               - Use bisect_left to find the first index whose value is
                 greater than or equal to the current number.
               - If the index equals len(tails), append the number because
                 it extends the longest subsequence found so far.
               - Otherwise, replace tails[idx] with the current number
                 because it provides a smaller or equal tail.
            3. Return len(tails), which represents the length of the LIS.

            bisect_left is used because the subsequence must be strictly
            increasing. Equal values should replace an existing value
            instead of increasing the length.

        Time:
            O(n log n)
            Each of the n elements performs a binary search.

        Space:
            O(n)
            In the worst case, tails can contain n elements.
        """

        tails = []

        for num in nums:
            idx = bisect_left(tails, num)

            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num

        return len(tails)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], expected: int)
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7], 1),
    ]

    for nums, expected in test_cases:
        result = solution.longest_increasing_subsequence_dp_and_binary_search(
            nums
        )

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