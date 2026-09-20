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

    def climbing_stairs_brute_TLE(self, n: int):
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

        if n <= 2:
            return n

        return self.climbing_stairs(n - 1) + self.climbing_stairs(n - 2)

    def climbing_stairs_memoization(self, n: int):
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
            -

        Algorithm:
            -

        Time:
            O()

        Space:
            O()
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
            -

        Algorithm:
            -

        Time:
            O()

        Space:
            O()
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