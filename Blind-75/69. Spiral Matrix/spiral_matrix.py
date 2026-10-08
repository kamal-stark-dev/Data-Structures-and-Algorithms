class Solution:
    """
    Problem:
        - Given an m x n matrix, return all elements of the matrix
          in spiral order.

    Approach:
        1. Maintain four boundaries: top, bottom, left, and right.
        2. Traverse the current outer layer from left to right,
           then top to bottom, then right to left, and finally
           bottom to top.
        3. After traversing each side, shrink the corresponding
           boundary and repeat until all elements are visited.

    Constraints:
        - 1 <= m, n <= 10
        - -100 <= matrix[i][j] <= 100
        - The matrix contains at least one row and one column.

    Notes:
        - The boundary checks before traversing the bottom row and
          left column prevent duplicate elements when the remaining
          layer has only one row or one column.
    """

    def spiral_matrix(self, matrix: list[list[int]]) -> list[int]:
        """
        Intuition:
            - Treat the matrix as a series of concentric layers.
            - For each layer, traverse its four sides in clockwise
              order: top -> right -> bottom -> left.
            - Four pointers (`top`, `bottom`, `left`, `right`) define
              the current unvisited layer. After traversing a side,
              move its boundary inward.

        Algorithm:
            - Initialize `top`, `bottom`, `left`, and `right` to the
              outer boundaries of the matrix.
            - While there are still unvisited rows and columns:
                1. Traverse the top row from left to right.
                2. Move `top` down by one.
                3. Traverse the right column from top to bottom.
                4. Move `right` left by one.
                5. If rows remain, traverse the bottom row from
                   right to left and move `bottom` up.
                6. If columns remain, traverse the left column from
                   bottom to top and move `left` right.
            - Continue until all matrix elements have been added
              to the result.

        Time:
            O(m * n)

        Space:
            O(m * n)
        """

        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        res = []

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (matrix: list[list[int]], expected: list[int])
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        ),
    ]

    for matrix, expected in test_cases:
        result = solution.spiral_matrix(matrix)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"matrix = {matrix}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"matrix = {matrix}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")