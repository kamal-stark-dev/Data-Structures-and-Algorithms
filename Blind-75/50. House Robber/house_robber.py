class Solution:
    """
    Problem:
    Given an array nums where nums[i] represents the amount of money
    available in the i-th house, find the maximum amount of money that
    can be robbed without robbing two adjacent houses.

        Approach:
        1. At every house, we have two choices:
        - Skip the current house.
        - Rob the current house and skip the adjacent previous house.
        2. Define the DP state as the maximum money that can be robbed
        considering houses up to index `i`.
        3. The recurrence is:
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        This can be implemented using recursion, memoization,
        tabulation, or constant-space DP.

    Constraints:
        - 1 <= nums.length <= 100
        - 0 <= nums[i] <= 400

    Notes:
        - Adjacent houses cannot both be robbed.
        - The problem is a classic 1D Dynamic Programming problem.
        - The optimal solution only needs the results from the previous
        two states, allowing O(1) extra space.
    """

    def house_robber_recursion(self, nums: list[int]) -> int:
        """
        Intuition:
            - For every house `i`, there are two choices:
                1. Do not rob house `i`, so the answer remains the best
                answer from houses `0 ... i-1`.
                2. Rob house `i`, so house `i-1` cannot be robbed. Therefore,
                we add nums[i] to the best answer from houses `0 ... i-2`.
            - We take the maximum of these two choices.
            - This gives the recurrence:
                f(i) = max(f(i - 1), nums[i] + f(i - 2))

        Algorithm:
            - Define a recursive function `recursion(i)` that returns the
            maximum amount of money that can be robbed from houses
            `0 ... i`.
            - Base case for one house:
                f(0) = nums[0]
            - Base case for two houses:
                f(1) = max(nums[0], nums[1])
            - For every other index, choose the better of:
                - skipping the current house
                - robbing the current house
            - Return the result for the last house.

        Time:
            O(2^n)

        Space:
            O(n)

            The recursion tree can have exponential time complexity, while
            the maximum recursion depth is O(n).
        """

        n = len(nums)

        def recursion(i: int) -> int:
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            return max(recursion(i - 1), nums[i] + recursion(i - 2))

        return recursion(n - 1)

    def house_robber_memoization(self, nums: list[int]) -> int:
        """
        Intuition:
            - The recursive solution repeatedly calculates the same states.
            - For example, while calculating f(i), both f(i-1) and f(i-2)
            are needed, and their recursive calls overlap heavily.
            - We store the result of every already-computed state in a
            dictionary so that each state is calculated only once.

        Algorithm:
            - Define `dfs(i)` as the maximum money that can be robbed from
            houses `0 ... i`.
            - Before calculating a state, check whether its result already
            exists in `memo`.
            - If it exists, return the stored result.
            - Otherwise:
                f(i) = max(f(i - 1), nums[i] + f(i - 2))
            - Store the computed result in `memo`.
            - Return the result for the last house.

        Time:
            O(n)

            There are only `n` unique states, and each state is calculated
            once.

        Space:
            O(n)

            O(n) space is used by the memoization dictionary, and the
            recursion stack can also grow to O(n).
        """

        memo = {}
        n = len(nums)

        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]

            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            memo[i] = max(dfs(i - 1), nums[i] + dfs(i - 2))

            return memo[i]

        return dfs(n - 1)

    def house_robber_tabulation(self, nums: list[int]) -> int:
        """
        Intuition:
            - Instead of solving the problem recursively from the end,
            we can build the solution from left to right.
            - `dp[i]` represents the maximum amount of money that can be
            robbed from houses `0 ... i`.
            - For house `i`, we either:
                1. Skip it -> dp[i - 1]
                2. Rob it -> nums[i] + dp[i - 2]
            - Therefore:
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        Algorithm:
            - Handle the single-house case separately.
            - Initialize:
                dp[0] = nums[0]
                dp[1] = max(nums[0], nums[1])
            - Iterate from index `2` to `n - 1`.
            - For every house, calculate the best answer using:
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            - The final answer is `dp[n - 1]`.

        Time:
            O(n)

            Every house is processed exactly once.

        Space:
            O(n)

            The `dp` array stores the optimal answer for every index.
        """

        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]

    def house_robber_optimal(self, nums: list[int]) -> int:
        """
        Intuition:
            - In the tabulation approach, to calculate `dp[i]`, we only
            need the previous two states:
                dp[i - 1] and dp[i - 2]
            - Therefore, storing the entire `dp` array is unnecessary.
            - We maintain only two variables:
                prev = dp[i - 2]
                curr = dp[i - 1]
            - After calculating the next state, shift the variables forward.

        Algorithm:
            - Handle the single-house case separately.
            - Initialize:
                prev = nums[0]
                curr = max(nums[0], nums[1])
            - For every house from index `2` onward:
                1. Calculate the new maximum:
                    max(curr, prev + nums[i])
                2. Move `curr` into `prev`.
                3. Store the newly calculated value in `curr`.
            - Return `curr`, which contains the maximum amount that can
            be robbed from all houses.

        Time:
            O(n)

            Each house is processed exactly once.

        Space:
            O(1)

            Only two variables are maintained regardless of the size of
            the input array.
        """

        n = len(nums)

        if n == 1:
            return nums[0]

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, n):
            prev, curr = curr, max(curr, prev + nums[i])

        return curr


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], expected: int)
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([1, 2, 3, 4, 2, 1], 7),
        ([1], 1),
    ]

    for nums, expected in test_cases:
        result = solution.house_robber_optimal(nums)

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