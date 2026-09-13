from collections import deque

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

    def number_of_islands_dfs(self, grid: list[list[str]]) -> int:
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

        def dfs(r: int, c: int, grid: list[list[str]], visited: list[list[bool]]) -> None:
            rows, cols = len(grid), len(grid[0])

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or visited[r][c]:
                return

            visited[r][c] = True

            dfs(r + 1, c, grid, visited)
            dfs(r, c + 1, grid, visited)
            dfs(r - 1, c, grid, visited)
            dfs(r, c - 1, grid, visited)

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c, grid, visited)
                    islands += 1

        return islands

    def number_of_islands_bfs(self, grid: list[list[str]]) -> int:
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

        def bfs(r: int, c: int, grid: list[list[str]], visited: set[tuple[int, int]]):
            queue = deque()
            queue.append((r, c))

            while queue:
                row, col = queue.popleft() # use queue.pop() to make it iterative DFS

                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited:
                        continue

                    queue.append((r, c))
                    visited.add((r, c))

        rows, cols = len(grid), len(grid[0])
        visited = set()

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c, grid, visited)
                    islands += 1

        return islands


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (grid: list[list[str]], expected: int)
        (
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            1
        ),
        (
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            3
        ),
        (
            [
                ["1","0","1","0","1"],
                ["0","1","0","1","0"],
                ["1","0","1","0","1"],
                ["0","1","0","1","0"]
            ],
            10
        ),
    ]

    for grid, expected in test_cases:
        result = solution.number_of_islands_bfs(grid)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"grid = {grid}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"grid = {grid}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")