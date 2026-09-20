class Solution:

    """
    Problem:
        - You are climbing a staircase with n steps.
        - At each move, you can climb either 1 step or 2 steps.
        - Return the number of distinct ways to reach the top.

    Approach:
        1. Brute Force / Recursion:
           - For every step, try both possibilities: taking 1 step or 2 steps.
           - This creates overlapping subproblems and leads to exponential time.

        2. Memoization:
           - Store the result for every n that has already been calculated.
           - Avoid solving the same subproblem multiple times.

        3. Tabulation:
           - Build the solution bottom-up using a DP array.
           - dp[i] represents the number of ways to reach step i.

        4. Space Optimization:
           - Only the previous two DP values are required to calculate the
             current value.
           - Therefore, the complete DP array can be eliminated.

    Constraints:
        - 1 <= n <= 45

    Notes:
        - This problem follows the Fibonacci pattern.
        - The number of ways to reach step n is:
              dp[n] = dp[n - 1] + dp[n - 2]
        - Base cases:
              dp[1] = 1
              dp[2] = 2
    """

    def climbing_stairs_brute_TLE(self, n: int):
        """
        Intuition:
            - To reach step n, the last move must be either:
                1. A 1-step move from n - 1.
                2. A 2-step move from n - 2.
            - Therefore, the total number of ways is:
                  ways(n) = ways(n - 1) + ways(n - 2)
            - Recursively explore both possibilities.

        Algorithm:
            - If n <= 2, return n because:
                  n = 1 -> 1 way
                  n = 2 -> 2 ways
            - Otherwise, recursively calculate:
                  ways(n - 1) + ways(n - 2)
            - This repeatedly solves the same subproblems.

        Time:
            O(2^n)

        Space:
            O(n)
            - Due to the maximum recursion depth.
        """

        if n <= 2:
            return n

        return self.climbing_stairs(n - 1) + self.climbing_stairs(n - 2)

    def climbing_stairs_memoization(self, n: int):
        """
        Intuition:
            - The recursive solution calculates the same values repeatedly.
            - For example, calculating dp(5) requires dp(4) and dp(3),
              while dp(4) also requires dp(3).
            - Store already-computed results in a dictionary so that each
              subproblem is solved only once.

        Algorithm:
            - Create an empty memoization dictionary.
            - Define a recursive DP function.
            - If n is already present in memo, return the stored result.
            - For n <= 2, return n as the base case.
            - Otherwise:
                  dp(n) = dp(n - 1) + dp(n - 2)
            - Store the result in memo before returning it.

        Time:
            O(n)
            - Each value from 1 to n is calculated at most once.

        Space:
            O(n)
            - O(n) for the memoization dictionary.
            - O(n) recursion stack in the worst case.
        """

        memo = {}

        def dp(n: int) -> int:
            if n in memo:
                return memo[n]

            if n <= 2:
                return n

            res = dp(n - 1) + dp(n - 2)

            memo[n] = res
            return res

        return dp(n)

    def climbing_stairs_tabulation(self, n: int):
        """
        Intuition:
            - Instead of solving the problem recursively, solve smaller
              subproblems first and build the answer from the bottom up.
            - dp[i] represents the number of distinct ways to reach step i.
            - To reach step i, the previous move must come from either
              step i - 1 or step i - 2.

        Algorithm:
            - If n <= 2, return n.
            - Create a DP array of size n + 1.
            - Initialize:
                  dp[1] = 1
                  dp[2] = 2
            - For every step i from 3 to n:
                  dp[i] = dp[i - 1] + dp[i - 2]
            - Return dp[n].

        Time:
            O(n)
            - Iterate through the steps from 3 to n.

        Space:
            O(n)
            - The DP array stores the answer for every step.
        """

        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbing_stairs_optimal(self, n: int):
        """
        Intuition:
            - The tabulation solution only needs the previous two values
              to calculate the current value.
            - There is no need to store the entire DP array.
            - Keep only:
                  prev1 = number of ways to reach i - 2
                  prev2 = number of ways to reach i - 1
            - Update these two variables as we move forward.

        Algorithm:
            - If n <= 2, return n.
            - Initialize:
                  prev1 = 1  -> ways to reach step 1
                  prev2 = 2  -> ways to reach step 2
            - For each step from 3 to n:
                  current = prev1 + prev2
                  Move prev1 and prev2 forward.
            - Return prev2, which contains the number of ways to reach step n.

        Time:
            O(n)
            - We iterate from step 3 to step n.

        Space:
            O(1)
            - Only two variables are used regardless of n.
        """

        if n <= 2:
            return n

        prev1, prev2 = 1, 2

        for i in range(3, n + 1):
            temp = prev2
            prev2 += prev1
            prev1 = temp

            # prev1, prev2 = prev2, prev1 + prev2

        return prev2


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (n: int, expected: int)
        (2, 2),
        (3, 3),
        (4, 5),
        (7, 21),
        (44, 1134903170),
    ]

    for n, expected in test_cases:
        result = solution.climbing_stairs_optimal(n)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"n = {n}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"n = {n}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")