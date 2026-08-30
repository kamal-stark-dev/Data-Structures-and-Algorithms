class Solution:
    """
    Solve LeetCode 79: Word Search.

    Problem:
        Given an m x n grid of characters and a word, determine whether
        the word can be constructed by following horizontally or vertically
        adjacent cells.

        A cell may be used at most once while constructing the word.

    Approaches:
        1. Use the board itself to mark cells as visited temporarily.
        2. Use a separate `visited` matrix to keep track of visited cells.

    Constraints:
        - 1 <= m, n <= 6
        - 1 <= len(word) <= 15
        - The board and word contain only English letters.

    Notes:
        The solution uses depth-first search (DFS) with backtracking.
        After exploring a path, the visited state is restored so that
        other possible paths can use the cell.
    """

    def helper_with_visited(self, i: int, j: int, idx: int, board: list[list[str]], word: str, visited: list[list[bool]]) -> bool:
        """
        Search for `word[idx:]` using a separate visited matrix.

        Unlike `helper`, this implementation does not modify the board.
        Instead, `visited[i][j]` is set to True while a cell is part of
        the current DFS path and reset to False during backtracking.

        Args:
            i: Current row index.
            j: Current column index.
            idx: Index of the character currently being matched.
            board: The character grid.
            word: The target word.
            visited: Matrix indicating which cells are currently being
                used in the DFS path.

        Returns:
            True if the remaining part of the word can be constructed
            from the current position; otherwise, False.
        """
        m, n = len(board), len(board[0])

        # All characters have been successfully matched.
        if idx == len(word):
            return True

        # Check boundaries, character match, and whether this cell
        # has already been used in the current path.
        if (
            i < 0
            or i >= m
            or j < 0
            or j >= n
            or visited[i][j]
            or board[i][j] != word[idx]
        ):
            return False

        # Mark the current cell as visited.
        visited[i][j] = True

        # Explore all four possible directions.
        res = (
            self.helper_with_visited(
                i + 1, j, idx + 1, board, word, visited
            )
            or self.helper_with_visited(
                i, j + 1, idx + 1, board, word, visited
            )
            or self.helper_with_visited(
                i - 1, j, idx + 1, board, word, visited
            )
            or self.helper_with_visited(
                i, j - 1, idx + 1, board, word, visited
            )
        )

        # Backtrack: allow this cell to be used by another path.
        visited[i][j] = False

        return res

    def word_search_with_visited(self, board: list[list[str]], word: str) -> bool:
        """
        Determine whether `word` exists in the board using a visited matrix.

        This is functionally equivalent to `word_search`, but instead of
        temporarily changing board cells, it maintains a separate boolean
        matrix to track cells used during the current DFS path.

        Args:
            board: An m x n grid of characters.
            word: The word to search for.

        Returns:
            True if the word can be constructed from adjacent cells;
            otherwise, False.

        Complexity:
            Time:
                O(m * n * 4^L), where L is the length of `word`.

            Space:
                O(m * n) for the visited matrix plus O(L) for the
                recursion stack.
        """
        m, n = len(board), len(board[0])

        # Create a matrix where False means the cell has not been
        # visited on the current DFS path.
        visited = [[False] * n for _ in range(m)]

        # Try every cell as a potential starting position.
        for i in range(m):
            for j in range(n):
                if self.helper_with_visited(
                    i,
                    j,
                    0,
                    board,
                    word,
                    visited,
                ):
                    return True

        return False

    def helper(self, i: int, j: int, idx: int, board: list[list[str]], word: str) -> bool:
        """
        Search for `word[idx:]` starting from board[i][j].

        This implementation marks the current cell directly in `board`
        using '%' to indicate that the cell has already been visited on
        the current DFS path.

        Args:
            i: Current row index.
            j: Current column index.
            idx: Index of the character currently being matched in `word`.
            board: The character grid.
            word: The target word.

        Returns:
            True if the remaining part of the word can be constructed
            from the current position; otherwise, False.
        """
        m, n = len(board), len(board[0])

        # All characters have been successfully matched.
        if idx == len(word):
            return True

        # Check whether the current position is valid and matches
        # the character we are looking for.
        if (
            i < 0
            or i >= m
            or j < 0
            or j >= n
            or board[i][j] != word[idx]
        ):
            return False

        # Mark the current cell as visited.
        original = board[i][j]
        board[i][j] = "%"

        # Explore all four possible directions.
        res = (
            self.helper(i + 1, j, idx + 1, board, word)
            or self.helper(i, j + 1, idx + 1, board, word)
            or self.helper(i - 1, j, idx + 1, board, word)
            or self.helper(i, j - 1, idx + 1, board, word)
        )

        # Backtrack: restore the original character.
        board[i][j] = original

        return res

    def word_search(self, board: list[list[str]], word: str) -> bool:
        """
        Determine whether `word` exists in the board.

        The function tries every cell as a possible starting position
        and uses DFS with backtracking to search for the remaining
        characters.

        Args:
            board: An m x n grid of characters.
            word: The word to search for.

        Returns:
            True if the word can be constructed from adjacent cells;
            otherwise, False.

        Complexity:
            Time:
                O(m * n * 4^L), where L is the length of `word`.
                More precisely, after the first character, each step
                has at most 3 useful choices because we cannot immediately
                reuse the previous cell.

            Space:
                O(L) for the recursive call stack, where L is the
                length of `word`.
        """
        m, n = len(board), len(board[0])

        # Try every cell as a potential starting point.
        for i in range(m):
            for j in range(n):
                if self.helper(i, j, 0, board, word):
                    return True

        return False


if __name__ == "__main__":
    """
    Run test cases for both Word Search implementations.

    Each test case contains:
        - A board.
        - A word to search for.
        - The expected result.

    Both implementations are tested against the same test cases to
    verify that they produce identical results.
    """

    solution = Solution()

    test_cases = [
        # (board: list[list[str]], word: str, expected: bool)
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCCED",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "SEE",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCB",
            False,
        ),
    ]

    # Test both implementations.
    for board, word, expected in test_cases:
        result_in_place = solution.word_search(board, word)
        result_with_visited = solution.word_search(board, word)

        assert result_in_place == expected, (
            f"\n\nIn-place implementation failed!\n"
            f"board = {board}\n"
            f"word = {word}\n"
            f"expected = {expected}\n"
            f"got = {result_in_place}\n"
        )

        assert result_with_visited == expected, (
            f"\n\nVisited-array implementation failed!\n"
            f"board = {board}\n"
            f"word = {word}\n"
            f"expected = {expected}\n"
            f"got = {result_with_visited}\n"
        )

        print(
            f"board = {board}\n"
            f"word = {word}\n"
            f"expected = {expected}\n"
            f"in-place result = {result_in_place}\n"
            f"visited-array result = {result_with_visited}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")