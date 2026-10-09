from copy import deepcopy

class Solution:
    """
    Problem:
        Given an m x n integer matrix, if an element is 0, set its entire
        row and column to 0. The modification must be performed in place.

    Approach:
        1. Brute Force:
        Create a copy of the matrix. For every zero in the original
        matrix, mark its entire row and column as zero in the copy.
        Copy the result back into the original matrix.

        2. Space Optimized:
        Use separate boolean arrays to track which rows and columns
        contain at least one zero. Update the original matrix using
        these markers.

        3. Space Optimal:
        Use the first row and first column of the matrix as markers
        to record which rows and columns must be zeroed. Use two
        boolean variables to track whether the first row and first
        column originally contain a zero.

    Constraints:
        - 1 <= m, n <= 200
        - -2^31 <= matrix[i][j] <= 2^31 - 1
        - The matrix must be modified in place.

    Notes:
        - Zeroes must be identified before modifying the corresponding
        rows and columns to avoid incorrectly propagating new zeroes.
        - The brute-force approach uses O(m * n) auxiliary space.
        - The space-optimized approach uses O(m + n) auxiliary space.
        - The space-optimal approach uses O(1) auxiliary space.
        - All three approaches run in O(m * n) time.
    """

    def set_matrix_zeros_brute(self, matrix: list[list[int]]) -> None:
        """
        Intuition:
            Directly setting rows and columns to zero while traversing the
            original matrix can cause newly created zeroes to be processed
            as if they were present initially. This can incorrectly zero
            additional rows and columns.

            To avoid this, maintain a separate copy of the matrix. Use the
            original matrix to identify zeroes and modify only the copy.

        Algorithm:
            1. Create a deep copy of the matrix.
            2. Traverse every element of the original matrix.
            3. If matrix[r][c] == 0:
            - Set every element in column c of the copy to zero.
            - Set every element in row r of the copy to zero.
            4. Copy the modified matrix back into the original matrix.

        Time:
            O(m * n * (m + n))
            Traversing the matrix takes O(m * n). For each zero, updating
            its row and column takes O(m + n). In the worst case, every
            element is zero.

        Space:
            O(m * n)
            The temporary matrix stores a copy of all m * n elements.
        """

        rows, cols = len(matrix), len(matrix[0])

        temp_matrix = [[matrix[r][c] for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for row in range(rows):
                        temp_matrix[row][c] = 0

                    for col in range(cols):
                        temp_matrix[r][col] = 0

        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = temp_matrix[r][c]

    def set_matrix_zeros_space_optimized(self, matrix: list[list[int]]) -> None:
        """
        Intuition:
            Instead of storing a complete copy of the matrix, maintain two
            boolean arrays:
            - rows_zeros[r] indicates whether row r must be zeroed.
            - cols_zeros[c] indicates whether column c must be zeroed.

            First identify all affected rows and columns. Then update the
            original matrix using these markers, avoiding interference
            between identifying zeroes and modifying the matrix.

        Algorithm:
            1. Initialize a boolean array of size m for rows and another
            boolean array of size n for columns.
            2. Traverse the matrix. Whenever matrix[r][c] == 0, mark
            rows_zeros[r] and cols_zeros[c] as True.
            3. Traverse the matrix again.
            4. If rows_zeros[r] or cols_zeros[c] is True, set matrix[r][c]
            to zero.

        Time:
            O(m * n)
            Two complete matrix traversals are performed.

        Space:
            O(m + n)
            The row and column marker arrays require m + n boolean entries.
        """

        rows, cols = len(matrix), len(matrix[0])

        rows_zeros = [False] * rows
        cols_zeros = [False] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rows_zeros[r] = True
                    cols_zeros[c] = True

        for r in range(rows):
            for c in range(cols):
                if rows_zeros[r] or cols_zeros[c]:
                    matrix[r][c] = 0

    def set_matrix_zeros_space_optimal(self, matrix: list[list[int]]) -> None:
        """
        Intuition:
            The separate row and column arrays can be eliminated by using
            the first row and first column of the matrix as marker storage.

            For every zero at matrix[r][c], mark:
            - matrix[r][0] = 0 to indicate that row r must be zeroed.
            - matrix[0][c] = 0 to indicate that column c must be zeroed.

            However, the first row and first column are shared marker
            storage, so two boolean variables are needed to remember
            whether either of them originally contained a zero.

        Algorithm:
            1. Check whether the first column contains a zero and store
            the result in first_row.
            2. Check whether the first row contains a zero and store
            the result in first_col.
            3. Traverse the matrix, excluding the first row and column.
            Whenever a zero is found, mark its row and column by
            setting matrix[r][0] and matrix[0][c] to zero.
            4. Traverse the remaining matrix again. If either marker
            matrix[r][0] or matrix[0][c] is zero, set matrix[r][c]
            to zero.
            5. If first_row is True, zero the first column.
            6. If first_col is True, zero the first row.

        Time:
            O(m * n)
            The algorithm performs a constant number of matrix traversals.

        Space:
            O(1)
            Only two boolean variables are used, and the first row and
            column serve as markers within the original matrix.
        """

        rows, cols = len(matrix), len(matrix[0])

        first_col = False

        for r in range(rows):
            if matrix[r][0] == 0:
                first_col = True
                break

        first_row = False

        for c in range(cols):
            if matrix[0][c] == 0:
                first_row = True
                break

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_col:
            for r in range(rows):
                matrix[r][0] = 0

        if first_row:
            for c in range(cols):
                matrix[0][c] = 0

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (matrix: list[list[int]], expected: list[list[int]])
        (
            [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
            [
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 1]
            ]
        ),
        (
            [
                [0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]
            ],
            [
                [0, 0, 0, 0],
                [0, 4, 5, 0],
                [0, 3, 1, 0]
            ]
        ),
    ]

    for nums, expected in test_cases:
        original_nums = deepcopy(nums)

        solution.set_matrix_zeros_space_optimal(nums)

        assert nums == expected, (
            f"\n\nTest case failed!\n"
            f"nums = {original_nums}\n"
            f"expected = {expected}\n"
            f"got = {nums}\n"
        )

        print(
            f"nums = {original_nums}\n"
            f"expected = {expected}\n"
            f"got = {nums}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")