from collections import deque

class Solution:
    """
    Problem:
        Given a list of coin denominations and a target amount, return the
        minimum number of coins required to make that amount.

        Each coin can be used an unlimited number of times. If the amount
        cannot be formed using the given coins, return -1.

    Approach:
        1. Recursion: Try every coin and recursively solve the remaining amount.
        2. Memoization: Cache the result for every amount to avoid solving
           the same subproblem repeatedly.
        3. Tabulation: Build the minimum number of coins for every amount
           from 0 up to the target amount.
        4. BFS: Treat every reachable amount as a graph state and find the
           shortest path from 0 to the target amount.

    Constraints:
        - 1 <= coins.length <= 12
        - 1 <= coins[i] <= 2^31 - 1
        - 0 <= amount <= 10^4

    Notes:
        - An unlimited number of each coin can be used.
        - The answer can be at most `amount` when a solution exists because
          the smallest possible coin value is 1.
        - An impossible state can therefore be represented using `amount + 1`
          in tabulation, or `float("inf")` in recursion/memoization.
    """

    def coin_change_recursion(self, coins: list[int], amount: int) -> int:
        """
        Intuition:
            For every amount, try taking each coin that does not exceed the
            current amount. After taking a coin, recursively find the minimum
            number of coins required for the remaining amount.

            The recurrence is:

                dfs(amount) = min(1 + dfs(amount - coin))

            The `1` represents the coin chosen in the current step.

        Algorithm:
            1. If the amount is 0, return 0 because no coins are required.
            2. Initialize the result to a very large value.
            3. Try every coin that can be used.
            4. Recursively solve the remaining amount.
            5. Take the minimum number of coins among all choices.
            6. Return -1 if no valid combination was found.

        Time:
            O(n^amount), where n is the number of coin denominations.
            In the worst case, every recursive call branches into up to
            `n` further calls.

        Space:
            O(amount), due to the maximum recursion depth. Each recursive
            call reduces the amount by at least 1.
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

    def coin_change_memoization(self, coins: list[int], amount: int) -> int:
        """
        Intuition:
            The recursive solution repeatedly solves the same amounts.

            For example, when calculating dfs(11), multiple different paths
            may eventually require dfs(6). Instead of calculating dfs(6)
            repeatedly, store its result the first time it is computed.

            This turns the exponential recursive solution into a solution
            with one computation per possible amount.

        Algorithm:
            1. Store the base case `memo[0] = 0`.
            2. If an amount has already been computed, return its cached result.
            3. Try every coin that does not exceed the current amount.
            4. Recursively calculate the result for the remaining amount.
            5. Add 1 for the current coin and keep the minimum.
            6. Store the result in `memo`.
            7. Return -1 if the target amount remains impossible.

        Time:
            O(amount * n), where n is the number of coin denominations.
            There are at most `amount` different states, and each state
            tries every coin.

        Space:
            O(amount), for the memoization dictionary and recursion stack.
        """

        memo = {0: 0}

        def dfs(amount: int) -> int:
            if amount in memo:
                return memo[amount]

            res = float("inf")

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins == float("inf") else minCoins

    def coin_change_tabulation(self, coins: list[int], amount: int) -> int:
        """
        Intuition:
            Instead of solving the problem recursively, build the answer
            for every amount from 0 to the target amount.

            `dp[amt]` represents the minimum number of coins required to
            make exactly `amt`.

            For every coin, if we can use it, then:

                dp[amt] = min(dp[amt], 1 + dp[amt - coin])

            This is the bottom-up version of the same recurrence used in
            the memoized solution.

        Algorithm:
            1. Create a DP array of size `amount + 1`.
            2. Initialize every state with `amount + 1`, representing an
               impossible value.
            3. Set `dp[0] = 0` because zero coins are needed to make amount 0.
            4. Iterate through every amount from 1 to `amount`.
            5. For each amount, try every coin that can be used.
            6. Update the state using `1 + dp[amt - coin]`.
            7. Return the computed answer, or -1 if the target remains
               impossible.

        Time:
            O(amount * n), where n is the number of coin denominations.

        Space:
            O(amount), for the DP array.
        """

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1

    def coin_change_bfs(self, coins: list[int], amount: int) -> int:
        """
        Intuition:
            View every reachable amount as a node in a graph.

            Starting from amount 0, using a coin creates an edge to:

                current_amount + coin

            Every edge represents using exactly one coin, so finding the
            shortest path from 0 to `amount` gives the minimum number of coins.

            BFS explores states level by level:
                Level 0 -> 0 coins
                Level 1 -> 1 coin
                Level 2 -> 2 coins
                ...

            Therefore, the first time we reach the target amount, we have
            found the minimum number of coins.

        Algorithm:
            1. If the target amount is 0, return 0.
            2. Start BFS from amount 0.
            3. Maintain a `seen` array so that each amount is processed
               at most once.
            4. For every current amount, try adding every coin.
            5. If the new amount equals the target, return the current
               number of coins.
            6. Ignore amounts greater than the target or amounts already seen.
            7. Add every new valid amount to the queue.
            8. If the queue becomes empty, the target cannot be formed,
               so return -1.

        Time:
            O(amount * n), because there are at most `amount + 1` reachable
            states and each state tries every coin.

        Space:
            O(amount), for the queue and the `seen` array.
        """

        if amount == 0:
            return 0

        queue = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True

        res = 0

        while queue:
            res += 1

            for _ in range(len(queue)):
                curr = queue.popleft()

                for coin in coins:
                    nxt = curr + coin

                    if nxt == amount:
                        return res

                    if nxt > amount or seen[nxt]:
                        continue

                    seen[nxt] = True
                    queue.append(nxt)

        return -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (coins: list[int], amount: int, expected: int)
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ]

    for coins, amount, expected in test_cases:
        result = solution.coin_change_bfs(coins, amount)

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