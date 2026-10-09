from copy import deepcopy

class Solution:
    """
    Problem:
        - Given an n x n square matrix, rotate the matrix 90 degrees clockwise.
        - The rotation must be performed in-place.
        - The final matrix should contain the rotated values without allocating
          another 2D matrix.

    Approach:
        1. Brute Force:
           - Create a new n x n matrix.
           - For every element matrix[i][j], place it at
             rotated[j][n - i - 1].
           - Copy the rotated matrix back into the original matrix.

        2. Rotate by Four Cells:
           - Process the matrix layer by layer, starting from the outer layer.
           - For each position, rotate four corresponding cells at once.
           - Move inward until all layers have been processed.

        3. Reverse and Transpose:
           - Reverse the matrix vertically.
           - Transpose the matrix by swapping matrix[i][j] with matrix[j][i].
           - These two operations together produce a 90-degree clockwise rotation.

    Constraints:
        - n == matrix.length == matrix[i].length
        - 1 <= n <= 20
        - -1000 <= matrix[i][j] <= 1000

    Notes:
        - The matrix is always square.
        - The rotation must be performed in-place.
        - A 90-degree clockwise rotation maps:
              matrix[i][j] -> matrix[j][n - i - 1]
    """

    def rotate_image_brute_force(self, matrix: list[list[int]]) -> None:
        """
        Intuition:
            - A 90-degree clockwise rotation moves the element at
              matrix[i][j] to rotated[j][n - i - 1].
            - Since modifying the original matrix directly can overwrite
              values that are still needed, use a separate matrix to store
              the rotated result first.
            - Finally, copy the result back into the original matrix.

        Algorithm:
            1. Create an empty n x n matrix called rotated.
            2. Traverse every element of the original matrix.
            3. Place matrix[i][j] at rotated[j][n - i - 1].
            4. Copy every element from rotated back into matrix.

        Time:
            O(n^2)

        Space:
            O(n^2)
        """

        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated[j][n - i - 1] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]

    def rotate_image_rotate_by_four_cells(self, matrix: list[list[int]]) -> None:
        """
        Intuition:
            - Instead of creating another matrix, rotate four corresponding
              cells at the same time.
            - For a clockwise rotation, four cells form a cycle:
                  top-left -> top-right
                  top-right -> bottom-right
                  bottom-right -> bottom-left
                  bottom-left -> top-left
            - Each four-cell rotation is performed using one temporary
              variable, so the matrix remains in-place.
            - After processing the outer layer, move inward to the next layer.

        Algorithm:
            1. Maintain `left` and `right` boundaries for the current layer.
            2. For every position in the current layer:
               - Save the top-left value.
               - Move bottom-left to top-left.
               - Move bottom-right to bottom-left.
               - Move top-right to bottom-right.
               - Move the saved top-left to top-right.
            3. Move the boundaries inward.
            4. Continue until all layers have been rotated.

        Time:
            O(n^2)

        Space:
            O(1)
        """

        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                topleft = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom - i][left]

                matrix[bottom - i][left] = matrix[bottom][right - i]

                matrix[bottom][right - i] = matrix[top + i][right]

                matrix[top + i][right] = topleft

            right -= 1
            left += 1

    def rotate_image_reverse_and_transpose(self, matrix: list[list[int]]) -> None:
        """
        Intuition:
            - A 90-degree clockwise rotation can be achieved using two
              simpler matrix operations:
                  1. Reverse the matrix vertically.
                  2. Transpose the matrix.
            - Reversing vertically moves the bottom row to the top.
            - Transposing then swaps rows and columns, producing the
              required clockwise rotation.
            - Both operations can be performed directly on the original
              matrix, so no extra 2D matrix is required.

        Algorithm:
            1. Reverse the rows of the matrix.
               Example:
                   [1, 2, 3]       [7, 8, 9]
                   [4, 5, 6]  ->   [4, 5, 6]
                   [7, 8, 9]       [1, 2, 3]

            2. Transpose the matrix by swapping matrix[i][j] and
               matrix[j][i] for j > i.
               Only the upper triangular half is processed to avoid
               swapping every pair twice.

            3. The resulting matrix is the original matrix rotated
               90 degrees clockwise.

        Time:
            O(n^2)

        Space:
            O(1)
        """

        # Reverse matrix vertically
        matrix.reverse()

        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (matrix: list[list[int]], expected: list[list[int]])
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]
            ]
        ),
        (
            [
                [5,   1,  9, 11],
                [2,   4,  8, 10],
                [13,  3,  6,  7],
                [15, 14, 12, 16]
            ]
            ,
            [
                [15, 13,  2,  5],
                [14,  3,  4,  1],
                [12,  6,  8,  9],
                [16,  7, 10, 11]
            ]
        ),
    ]

    for matrix, expected in test_cases:
        original_matrix = deepcopy(matrix)

        # matrix gets updated inplace
        solution.rotate_image_reverse_and_transpose(matrix)

        assert matrix == expected, (
            f"\n\nTest case failed!\n"
            f"matrix = {original_matrix}\n"
            f"expected = {expected}\n"
            f"got = {matrix}\n"
        )

        print(
            f"matrix = {original_matrix}\n"
            f"expected = {expected}\n"
            f"got = {matrix}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")