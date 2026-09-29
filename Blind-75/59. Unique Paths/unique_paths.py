class Solution:
    """
    Problem:
        Given an m x n grid, return the number of unique paths from the
        top-left corner to the bottom-right corner.

        The robot can only move either right or down at any point.

    Approach:
        1. Recursion: Explore every possible path using DFS.
        2. Memoization: Cache the result for each grid position.
        3. Tabulation: Build the number of paths from bottom-right to top-left.
        4. Space Optimization: Reduce the 2D DP table to a 1D array.

    Constraints:
        1 <= m, n <= 100

    Notes:
        Each position can be reached either from the cell above or the cell
        to its left, so the number of paths to a cell is the sum of the
        paths to those two previous cells.
    """

    def unique_paths_recursion(self, m: int, n: int) -> int:
        """
        Intuition:
            From every cell, the robot has at most two choices:
            move right or move down.

            Recursively explore both choices. Whenever the destination is
            reached, return 1 because one valid path has been found.
            If the robot moves outside the grid, return 0.

        Algorithm:
            1. Start DFS from the top-left corner.
            2. If the destination is reached, return 1.
            3. If the current position is outside the grid, return 0.
            4. Recursively count paths by moving right and down.
            5. Return the sum of both results.

        Time:
            O(2^(m+n))

        Space:
            O(m + n)
            # Maximum recursion depth.
        """

        def dfs(i: int, j: int) -> int:
            if i == (m - 1) and j == (n - 1):
                return 1

            if i >= m or j >= n:
                return 0

            return dfs(i, j + 1) + dfs(i + 1, j)

        return dfs(0, 0)

    def unique_paths_memoization(self, m: int, n: int) -> int:
        """
        Intuition:
            The recursive solution repeatedly solves the same subproblems.
            For example, multiple paths can reach the same cell, causing
            its remaining paths to be calculated again.

            Store the answer for every cell after calculating it once.

        Algorithm:
            1. Create a memoization table initialized with -1.
            2. Start DFS from the top-left corner.
            3. Return 1 when the destination is reached.
            4. Return 0 when outside the grid.
            5. If the current cell has already been calculated, return
               its stored result.
            6. Otherwise, calculate the paths by moving right and down,
               store the result, and return it.

        Time:
            O(m * n)

        Space:
            O(m * n)
            # Memoization table + recursion stack.
        """

        memo = [[-1] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if i == (m - 1) and j == (n - 1):
                return 1

            if i >= m or j >= n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return memo[i][j]

        return dfs(0, 0)

    def unique_paths_tabulation(self, m: int, n: int) -> int:
        """
        Intuition:
            Instead of recursively exploring paths, calculate the number
            of paths for every cell using previously calculated cells.

            For any cell, the robot can arrive either from above or from
            the left:

                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

            Since we start from the destination, we fill the table
            backwards toward the top-left.

        Algorithm:
            1. Create a DP table with an extra row and column of zeros.
            2. Set the destination cell to 1 because there is exactly
               one way to stay at the destination.
            3. Iterate from bottom-right toward top-left.
            4. For every cell, add the number of paths from the cell below
               and the cell to the right.
            5. Return the value at the top-left corner.

        Time:
            O(m * n)

        Space:
            O(m * n)
            # 2D DP table.
        """

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]

    def unique_paths_optimal(self, m: int, n: int) -> int:
        """
        Intuition:
            The tabulation approach only needs the current row and the
            values from the row below. Therefore, we can compress the
            2D DP table into a single 1D array.

            dp[j] represents the number of paths from the current cell
            in column j to the destination.

            When processing from right to left:
                dp[j] = paths from below + paths from right

        Algorithm:
            1. Initialize every value in dp to 1 because the last row
               has only one possible path: keep moving right.
            2. Process the remaining rows from bottom to top.
            3. Process each row from right to left.
            4. Update dp[j] using:
                   dp[j] += dp[j + 1]
            5. Return dp[0], which represents the number of paths from
               the top-left corner.

        Time:
            O(m * n)

        Space:
            O(n)
            # 1D DP array.
        """

        dp = [1] * n

        for _ in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]

        return dp[0]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (m: int, n: int, expected: int)
        (3, 7, 28),
        (3, 2, 3),
    ]

    for m, n, expected in test_cases:
        result = solution.unique_paths_optimal(m, n)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"m = {m}\n"
            f"n = {n}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"m = {m}\n"
            f"n = {n}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")