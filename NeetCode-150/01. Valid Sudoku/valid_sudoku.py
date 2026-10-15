class Solution:
    """
    Problem:
        - Determine whether a 9 x 9 Sudoku board is valid.
        - Each row must contain digits 1-9 without repetition.
        - Each column must contain digits 1-9 without repetition.
        - Each 3 x 3 sub-box must contain digits 1-9 without repetition.
        - Empty cells ('.') are ignored.
        - A valid board does not necessarily have to be solvable.

    Approach:
        1. Brute Force:
            - Validate each row independently using a set.
            - Validate each column independently using a set.
            - Validate each 3 x 3 sub-box independently using a set.
            - Return False if any duplicate is found; otherwise, return True.

        2. Hash Set:
            - Maintain separate sets for each of the 9 rows, columns,
              and 3 x 3 sub-boxes.
            - Traverse the board once, skipping empty cells.
            - For each filled cell, check whether its digit already
              exists in its corresponding row, column, or sub-box.
            - Return False if a duplicate is found; otherwise, add the
              digit to all three sets and return True after traversal.

        3. Bit Masking:
            - Represent the digits present in each row, column, and
              sub-box using an integer bit mask.
            - Map each digit to a bit using (1 << digit).
            - Use bitwise AND (&) to check whether the digit already
              exists in any of the three corresponding masks.
            - Return False if a duplicate is found; otherwise, update
              all three masks using bitwise OR (|).
            - Return True if the entire board is validated successfully.

    Constraints:
        - board.length == 9
        - board[i].length == 9
        - board[i][j] is a digit from '1' to '9' or '.'.
        - Only filled cells need to be validated.
        - The board may be valid even if it is not solvable.

    Notes:
        - A 3 x 3 sub-box index can be calculated as:
              box_idx = (row // 3) * 3 + (col // 3)
        - The brute-force approach validates rows, columns, and boxes
          separately, requiring multiple traversals.
        - The hash-set and bit-masking approaches validate all three
          constraints simultaneously in a single traversal.
        - Bit masking uses integer bits instead of storing digits in sets.
        - All three approaches return False immediately upon detecting
          a duplicate and True if no violations are found.
    """

    def valid_sudoku_brute(self, board: list[list[str]]) -> bool:
        """
        Intuition:
            - A Sudoku board is valid if no digit is repeated in any row,
              column, or 3 x 3 sub-box.
            - Validate each group independently using a set to track
              the digits encountered.

        Algorithm:
            1. Iterate through each row and check for duplicate digits.
            2. Iterate through each column and check for duplicate digits.
            3. Iterate through each of the nine 3 x 3 sub-boxes and check
               for duplicate digits.
            4. Ignore empty cells represented by '.'.
            5. Return False if a duplicate is found; otherwise, return True.

        Time:
            O(1) - The board has a fixed size of 9 x 9.
            More generally, O(N^2) for an N x N board, assuming
            constant-time set operations.

        Space:
            O(1) - Each set stores at most 9 digits.
            More generally, O(N) auxiliary space for a board of size N x N.
        """

        for row in range(9):
            seen = set()

            for i in range(9):
                if board[row][i] == '.':
                    continue

                if board[row][i] in seen:
                    return False

                seen.add(board[row][i])

        for col in range(9):
            seen = set()

            for i in range(9):
                if board[i][col] == '.':
                    continue

                if board[i][col] in seen:
                    return False

                seen.add(board[i][col])

        for square in range(9):
            seen = set()

            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] == '.':
                        continue

                    if board[row][col] in seen:
                        return False

                    seen.add(board[row][col])

        return True

    def valid_sudoku_hash_set(self, board: list[list[str]]) -> bool:
        """
        Intuition:
            - Each filled cell must be unique within its row, column,
              and 3 x 3 sub-box.
            - Maintain a set for every row, column, and sub-box so all
              three constraints can be checked simultaneously.

        Algorithm:
            1. Initialize 9 sets for rows, 9 for columns, and 9 for boxes.
            2. Traverse every cell, skipping empty cells.
            3. Calculate the corresponding sub-box index using:
                   box_idx = (row // 3) * 3 + (col // 3)
            4. Check whether the digit exists in the corresponding row,
               column, or sub-box set.
            5. Return False if the digit already exists in any set.
            6. Otherwise, add the digit to all three sets.
            7. Return True after processing the entire board.

        Time:
            O(1) - The board has a fixed size of 9 x 9.
            More generally, O(N^2) for an N x N board, assuming
            average O(1) set operations.

        Space:
            O(1) - The sets store at most 9 digits each.
            More generally, O(N^2) auxiliary space for an N x N board.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                ch = board[row][col]
                box_idx = (row // 3) * 3 + (col // 3)

                if ch in rows[row] or ch in cols[col] or ch in boxes[box_idx]:
                    return False

                rows[row].add(ch)
                cols[col].add(ch)
                boxes[box_idx].add(ch)

        return True

    def valid_sudoku_bit_masking(self, board: list[list[str]]) -> bool:
        """
        Intuition:
            - Represent the digits present in each row, column, and
              sub-box using an integer bit mask.
            - Each digit corresponds to a distinct bit.
            - A set bit indicates that the corresponding digit has
              already appeared in that group.
            - Bitwise AND checks for duplicates, while bitwise OR
              marks a digit as present.

        Algorithm:
            1. Initialize arrays of 9 integers each for rows, columns,
               and sub-boxes, with all masks set to zero.
            2. Traverse every cell, skipping empty cells.
            3. Convert the digit to an integer and create its bit mask:
                   mask = 1 << val
            4. Calculate the sub-box index using:
                   box_idx = (row // 3) * 3 + (col // 3)
            5. Use bitwise AND (&) to check whether the digit is already
               present in the corresponding row, column, or sub-box.
            6. Return False if any corresponding mask contains the bit.
            7. Otherwise, update all three masks using bitwise OR (|).
            8. Return True after processing the entire board.

        Time:
            O(1) - The board has a fixed size of 9 x 9.
            More generally, O(N^2) for an N x N board, assuming
            constant-time integer bitwise operations.

        Space:
            O(1) - Three arrays of 9 integer masks each.
            More generally, O(N) auxiliary space for an N x N board.
        """

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                val = int(board[row][col])
                mask = 1 << val

                box_idx = (row // 3) * 3 + (col // 3)

                if (
                    mask & rows[row] or
                    mask & cols[col] or
                    mask & boxes[box_idx]
                ):
                    return False

                rows[row] |= mask
                cols[col] |= mask
                boxes[box_idx] |= mask

        return True


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (board: list[list[str]], expected: bool)
        (
            [
                ["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]
            ],
            True
        ),
        (
            [
                ["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]
            ],
            False
        ),
    ]

    for board, expected in test_cases:
        result = solution.valid_sudoku_bit_masking(board)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"board = {board}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"board = {board}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")