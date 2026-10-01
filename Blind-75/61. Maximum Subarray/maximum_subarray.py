class Solution:
    """
    Problem:
        Given an integer array nums, find the contiguous subarray
        with the largest sum and return its sum. The subarray must
        contain at least one element.

    Approach:
        1. Brute Force: Generate all possible subarrays, calculate
           their sums, and keep track of the maximum sum.
        2. Recursion: Use a DFS with two states to decide whether
           to start a subarray or continue an existing one.
        3. Memoization: Cache recursive results for each index and
           state to avoid repeated computations.
        4. Tabulation: Convert the recursive states into a bottom-up
           DP table to calculate the maximum subarray sum.
        5. Space Optimization: Reduce the DP table to a 1D array
           by using only the previous state's result.
        6. Kadane's Algorithm: Maintain a running sum, discarding
           negative prefixes that cannot improve a future subarray.
        7. Prefix Sum: Track the minimum prefix sum encountered so
           far and maximize the difference with the current prefix.

    Constraints:
        - 1 <= nums.length <= 10^5
        - -10^4 <= nums[i] <= 10^4
        - nums contains at least one element.
        - The subarray must be contiguous and non-empty.

    Notes:
        - A subarray is a contiguous, non-empty sequence of elements.
        - The answer may be negative if all elements are negative.
        - The recursive approaches use two states:
            - started = False: A subarray has not yet been started.
            - started = True: A subarray is currently being formed.
        - Kadane's Algorithm can be implemented in O(n) time
          and O(1) auxiliary space.
        - The prefix sum approach finds the maximum difference
          between the current prefix sum and the smallest
          preceding prefix sum.
        - The divide and conquer approach is another possible
          O(n log n) solution.
    """

    def maximum_subarray_brute(self, nums: list[int]) -> int:
        """
        Intuition:
            Every contiguous subarray can be represented by a
            starting index i and an ending index j. Enumerate
            all possible subarrays and calculate their sums
            incrementally to find the maximum.

        Algorithm:
            1. Initialize the result with nums[0].
            2. Iterate over every possible starting index i.
            3. Initialize curr_sum to 0 for each starting index.
            4. Extend the subarray from i to every ending index j,
               updating curr_sum incrementally.
            5. Update the result whenever a larger sum is found.
            6. Return the maximum subarray sum.

        Time:
            O(n^2) - There are O(n^2) possible subarrays, and
            each sum is calculated incrementally in O(1).

        Space:
            O(1) - Only a few variables are used.
        """

        n = len(nums)
        res = nums[0]

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                res = max(res, curr_sum)

        return res

    def maximum_subarray_recursive(self, nums: list[int]) -> int:
        """
        Intuition:
            At every index, decide whether to start a new subarray,
            continue an existing subarray, or skip the current
            element if a subarray has not yet started.

            Use two states:
                - started = False: No subarray has been started.
                - started = True: A subarray is currently active.

            Once a subarray has started, a negative running sum
            can be discarded by stopping the current subarray.
            This allows a future subarray to begin independently.

        Algorithm:
            1. Define dfs(i, started) as the maximum subarray sum
               obtainable from index i onward, given the current
               state.
            2. If started is True:
               - Either stop the current subarray and return 0,
                 or include nums[i] and continue.
            3. If started is False:
               - Either skip nums[i] and search for a starting
                 position later, or start a subarray at nums[i].
            4. At the last index, return the appropriate result
               while ensuring a non-empty subarray.
            5. Return dfs(0, False).

        Time:
            O(2^n) - Each recursive call may branch into two
            further calls, resulting in exponential time.

        Space:
            O(n) - The recursion stack can grow up to n levels.
        """

        def dfs(i: int, started: bool) -> int:
            if i == len(nums) - 1:
                return max(0, nums[i]) if started else nums[i]

            if started:
                return max(0, nums[i] + dfs(i + 1, True))

            return max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))

        return dfs(0, False)

    def maximum_subarray_memoization(self, nums: list[int]) -> int:
        """
        Intuition:
            The recursive solution repeatedly evaluates the same
            index and state combinations. Memoization stores the
            result of each state so that it only needs to be
            computed once.

        Algorithm:
            1. Create a 2D memoization table of size n x 2,
               initialized with None.
            2. Define dfs(i, started) to represent the maximum
               subarray sum obtainable from index i onward.
            3. Handle the base case at the last index.
            4. If the state has already been computed, return
               the cached result.
            5. Otherwise, calculate the result based on whether
               the subarray has already started:
               - If started is True, either stop or continue.
               - If started is False, either skip or start.
            6. Store the result in memo[i][started].
            7. Return dfs(0, False).

        Time:
            O(n) - There are 2 states for each of n indices,
            and each state is computed only once.

        Space:
            O(n) - The memoization table requires O(n) space,
            and the recursion stack also requires O(n) space.
        """

        def dfs(i: int, started: bool) -> int:
            if i == len(nums) - 1:
                return max(0, nums[i]) if started else nums[i]

            if memo[i][started] is not None:
                return memo[i][started]

            if started:
                memo[i][started] = max(0, nums[i] + dfs(i + 1, True))
            else:
                memo[i][started] = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))

            return memo[i][started]

        memo = [[None] * 2 for _ in range(len(nums))]

        return dfs(0, False)

    def maximum_subarray_tabulation(self, nums: list[int]) -> int:
        """
        Intuition:
            Convert the recursive states into a bottom-up dynamic
            programming solution. Each state at index i depends
            only on the corresponding states at index i + 1.

        Algorithm:
            1. Create a 2D DP table of size n x 2.
            2. Initialize both states at the last index with
               nums[n - 1], ensuring the subarray is non-empty.
            3. Iterate backward from index n - 2 to 0.
            4. For started = True:
               - Either start a new subarray at nums[i], or
                 extend the subarray from the next index.
            5. For started = False:
               - Either skip the current element or use the
                 result of starting a subarray at index i.
            6. Return dp[0][0], representing the maximum sum
               when no subarray has been started yet.

        Time:
            O(n) - Each index is processed once with a constant
            number of operations.

        Space:
            O(n) - The 2D DP table stores two states per index.
        """

        n = len(nums)

        dp = [[0] * 2 for _ in range(n)]
        dp[n - 1][1] = dp[n - 1][0] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            dp[i][1] = max(nums[i], nums[i] + dp[i + 1][1])
            dp[i][0] = max(dp[i + 1][0], dp[i][1])

        return dp[0][0]

    def maximum_subarray_kadanes(self, nums: list[int]) -> int:
        """
        Intuition:
            A subarray with a negative running sum cannot help
            maximize the sum of a future subarray. Discard such
            a prefix and start a new subarray at the next element.

            Maintain a running sum for the current subarray
            and a maximum sum encountered so far. This allows
            the answer to be computed in one pass without
            storing a DP array.

        Algorithm:
            1. Initialize maxSum with nums[0] to handle
               non-empty subarrays and all-negative arrays.
            2. Initialize currSum to 0.
            3. Iterate over each number in nums:
               - If currSum is negative, reset it to 0.
               - Add the current number to currSum.
               - Update maxSum with the larger of maxSum
                 and currSum.
            4. Return maxSum.

        Time:
            O(n) - The array is traversed once.

        Space:
            O(1) - Only the running sum and maximum sum
            variables are maintained.
        """

        maxSum = nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = 0

            currSum += num
            maxSum = max(maxSum, currSum)

        return maxSum

    def maximum_subarray_alternative(self, nums: list[int]) -> int:
        """
        Intuition:
            Express each subarray sum as the difference between
            two prefix sums.

            For a current prefix sum, the maximum subarray sum
            ending at the current position is obtained by
            subtracting the smallest prefix sum seen before
            the current position.

            Maintain the running prefix sum and the minimum
            prefix sum encountered so far to calculate the
            maximum subarray sum in a single pass.

        Algorithm:
            1. Initialize runningSum and minSoFar to 0.
            2. Initialize res with nums[0] to support
               non-empty subarrays and all-negative arrays.
            3. Iterate over each number in nums:
               - Add the number to runningSum.
               - Calculate the candidate subarray sum as
                 runningSum - minSoFar.
               - Update res if the candidate is larger.
               - Update minSoFar with the smaller of
                 minSoFar and runningSum.
            4. Return res.

        Time:
            O(n) - Each element is processed exactly once.

        Space:
            O(1) - Only three variables are maintained.
        """

        runningSum = 0
        minSoFar = 0
        res = nums[0]

        for num in nums:
            runningSum += num
            res = max(res, runningSum - minSoFar)
            minSoFar = min(minSoFar, runningSum)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], expected: int)
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ]

    for nums, expected in test_cases:
        result = solution.maximum_subarray_kadanes(nums)

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