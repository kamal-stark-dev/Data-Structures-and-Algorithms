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

    def coin_change_recursion(self, coins: list[int], amount: int) -> int:
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

        def dfs(amount: int) -> int:
            if amount == 0:
                return 0

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins

    def coin_change_(self, coins: list[int], amount: int) -> int:
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


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (coins: list[int], amount: int, expected: int)
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ]

    for coins, amount, expected in test_cases:
        result = solution.coin_change_recursion(coins, amount)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"coins = {coins}\n"
            f"amount = {amount}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"coins = {coins}\n"
            f"amount = {amount}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")