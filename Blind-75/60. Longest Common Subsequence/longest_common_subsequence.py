class Solution:
    """
    Problem:
        Given two strings text1 and text2, return the length of their
        longest common subsequence (LCS).

        A subsequence is formed by deleting zero or more characters from
        a string without changing the relative order of the remaining
        characters.

    Approach:
        1. Recursion: Explore all possible subsequences recursively.
        2. Memoization: Cache results for overlapping subproblems.
        3. Tabulation: Build a bottom-up DP table.
        4. Space Optimization: Reduce the 2D DP table to two 1D arrays.

    Constraints:
        - 1 <= text1.length, text2.length <= 1000
        - text1 and text2 consist only of lowercase English characters.

    Notes:
        For two characters at positions i and j:
        - If they are equal, they are part of the LCS, so we move both
          pointers forward.
        - If they are different, we try skipping either character and
          take the better result.
    """

    def longest_common_subsequence_recursion(self, text1: str, text2: str) -> int:
        """
        Intuition:
            At every pair of indices, we decide how the current characters
            contribute to the LCS.

            If text1[idx1] == text2[idx2], this character can be included
            in the LCS, so we move both indices forward.

            If they are different, the current characters cannot both be
            selected together. We try skipping the character from either
            string and take the maximum result.

        Algorithm:
            1. Start with the first character of both strings.
            2. If either string is exhausted, return 0.
            3. If the current characters match, add 1 and move both indices.
            4. Otherwise, recursively try:
               - Skipping the current character of text1.
               - Skipping the current character of text2.
            5. Return the maximum of the two choices.

        Time:
            O(2^(m + n))

        Space:
            O(m + n)
            - Recursion stack can grow up to m + n.

        Where:
            m = len(text1)
            n = len(text2)
        """

        def dfs(idx1: int, idx2: int) -> int:
            if idx1 == len(text1) or idx2 == len(text2):
                return 0

            if text1[idx1] == text2[idx2]:
                return 1 + dfs(idx1 + 1, idx2 + 1)

            return max(
                dfs(idx1 + 1, idx2),
                dfs(idx1, idx2 + 1)
            )

        return dfs(0, 0)

    def longest_common_subsequence_memoization(self, text1: str, text2: str) -> int:
        """
        Intuition:
            The recursive solution repeatedly solves the same subproblems.
            For example, the result for a pair of indices (i, j) can be
            reached through multiple recursive paths.

            We store the answer for every (i, j) pair in a dictionary so
            that each subproblem is solved only once.

        Algorithm:
            1. Define dfs(i, j) as the LCS length of text1[i:] and text2[j:].
            2. If either string is exhausted, return 0.
            3. If (i, j) has already been computed, return the cached result.
            4. If text1[i] == text2[j], include the character and move
               both indices forward.
            5. Otherwise, skip one character from either string and take
               the maximum result.
            6. Store each result in memo before returning it.

        Time:
            O(m * n)

        Space:
            O(m * n)
            - O(m * n) for the memoization dictionary.
            - O(m + n) recursion stack.

        Where:
            m = len(text1)
            n = len(text2)
        """

        memo = {}

        def dfs(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[(i, j)]

        return dfs(0, 0)

    def longest_common_subsequence_tabulation(self, text1: str, text2: str) -> int:
        """
        Intuition:
            Convert the recursive relationship into a bottom-up DP table.

            dp[i][j] represents the LCS length of text1[i:] and text2[j:].
            Since each state depends on positions to the right and below,
            the table is filled from bottom-right to top-left.

        Algorithm:
            1. Create a 2D DP table of size (m + 1) x (n + 1).
            2. The extra row and column represent cases where one string
               has been completely exhausted, so they remain 0.
            3. Iterate through both strings from right to left.
            4. If text1[i] == text2[j], set:
                   dp[i][j] = 1 + dp[i + 1][j + 1]
            5. Otherwise, set:
                   dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
            6. Return dp[0][0].

        Time:
            O(m * n)

        Space:
            O(m * n)

        Where:
            m = len(text1)
            n = len(text2)
        """

        rows, cols = len(text1), len(text2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

    def longest_common_subsequence_optimal(self, text1: str, text2: str) -> int:
        """
        Intuition:
            The 2D DP solution only needs the current row and the row
            immediately below it.

            Therefore, instead of storing the entire DP table, we maintain
            two 1D arrays:
                - prev: represents the row below the current row.
                - curr: represents the current row.

            We also use the shorter string for the columns to reduce memory.

        Algorithm:
            1. Make text2 the shorter string to minimize memory usage.
            2. Create two arrays of size len(text2) + 1.
            3. Iterate through text1 from right to left.
            4. For every character in text2, also iterate from right to left.
            5. If the characters match:
                   curr[j] = 1 + prev[j + 1]
            6. Otherwise:
                   curr[j] = max(curr[j + 1], prev[j])
            7. Swap prev and curr after processing each row.
            8. Return prev[0].

        Time:
            O(m * n)

        Space:
            O(min(m, n))

        Where:
            m = len(text1)
            n = len(text2)
        """

        if len(text1) < len(text2):
            text1, text2 = text2, text1

        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):

                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]

                else:
                    curr[j] = max(curr[j + 1], prev[j])

            prev, curr = curr, prev

        return prev[0]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (text1: str, text2: str, expected: int)
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
    ]

    for text1, text2, expected in test_cases:
        result = solution.longest_common_subsequence_optimal(text1, text2)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"text1 = {text1}\n"
            f"text2 = {text2}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"text1 = {text1}\n"
            f"text2 = {text2}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")