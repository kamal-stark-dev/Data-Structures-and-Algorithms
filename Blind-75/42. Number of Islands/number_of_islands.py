from collections import deque
from disjoin_set_union import DisjoinSetUnion

class Solution:
    """
    Problem:
        Given an m x n binary grid containing '1' (land) and '0' (water),
        return the number of islands.

        An island is a group of horizontally or vertically adjacent land
        cells ('1'). Diagonal cells are not considered connected.

    Approach:
        1. DFS:
           Treat every unvisited land cell as the beginning of a new island.
           Run DFS to visit all land cells belonging to that island.

        2. BFS:
           Same idea as DFS, but use a queue to explore all connected land
           cells level by level.

        3. Disjoint Set Union (DSU):
           Treat every land cell as a separate set initially. Union adjacent
           land cells. Every successful union combines two previously
           disconnected islands, so the island count can be maintained
           during the process.

    Constraints:
        - 1 <= m, n <= 300
        - grid[i][j] is either '0' or '1'
        - Only horizontal and vertical connections count.

    Notes:
        - Diagonal connections do not form an island.
        - DFS and BFS explicitly track visited cells.
        - DSU represents each cell using a 1D index:
              index = row * number_of_columns + column
    """

    def number_of_islands_dfs(self, grid: list[list[str]]) -> int:
        """
        Intuition:
            Every unvisited '1' represents a new island.

            Once we find such a cell, we perform DFS from it and visit every
            horizontally or vertically connected land cell belonging to the
            same island.

            Therefore, after completely exploring one island, we increment
            the island count by one.

        Algorithm:
            1. Create a visited matrix initialized to False.
            2. Traverse every cell in the grid.
            3. If the current cell is land ('1') and has not been visited:
               - It is the starting point of a new island.
               - Perform DFS to visit the entire connected component.
               - Increment the island count.
            4. Return the total number of islands.

            During DFS, stop when:
            - The position goes outside the grid.
            - The current cell is water ('0').
            - The current cell has already been visited.

        Time:
            O(m * n)

            Every cell is visited at most once by DFS, and the outer loop
            also examines every cell once.

        Space:
            O(m * n)

            The visited matrix requires O(m * n) space.

            Additionally, recursive DFS can use O(m * n) call-stack space
            in the worst case.
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
            Every unvisited land cell ('1') is the starting point of a new
            island.

            We use BFS to explore all horizontally and vertically connected
            land cells starting from that cell. Once BFS finishes, the entire
            island has been visited, so we increment the island count.

            BFS and DFS solve the same connected-component problem; the main
            difference is that BFS uses a queue while DFS uses recursion.

        Algorithm:
            1. Create an empty set to store visited cells.
            2. Traverse every cell in the grid.
            3. When an unvisited land cell is found:
               - Start BFS from that cell.
               - Mark it as visited.
               - Add its valid neighboring land cells to the queue.
               - Continue until the queue becomes empty.
               - Increment the island count.
            4. Return the island count.

            For each cell, check its four possible neighbors:
                - right  -> (0, 1)
                - down   -> (1, 0)
                - left   -> (0, -1)
                - up     -> (-1, 0)

        Time:
            O(m * n)

            Every cell is processed at most once, and each processed cell
            checks four directions. Since four is constant, the total
            complexity is O(m * n).

        Space:
            O(m * n)

            The visited set can contain up to m * n cells, and the BFS queue
            can also contain O(m * n) cells in the worst case.
        """

        def bfs(r: int, c: int, grid: list[list[str]], visited: set[tuple[int, int]]):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

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

    def number_of_islands_disjoint_set_union(self, grid: list[list[str]]) -> int:
        """
        Intuition:
            Initially, every land cell can be considered a separate island.

            Whenever two horizontally or vertically adjacent land cells are
            found, they belong to the same island, so we union their sets.

            We start with the number of land cells as the island count.
            Every time a union operation successfully connects two different
            sets, two islands become one, so we decrement the island count.

            If union() returns False, the two cells were already part of the
            same connected component, so the island count does not change.

        Algorithm:
            1. Create a DSU containing one element for every grid cell.
            2. Traverse every cell in the grid.
            3. For every land cell:
               - Initially count it as one island.
               - Check its four neighboring cells.
               - If a neighboring cell is also land, attempt to union the
                 two cells.
               - If the union succeeds, decrement the island count because
                 two previously separate components have become one.
            4. Return the final island count.

            Since a 2D cell needs to be represented as a single DSU index,
            convert:

                (r, c) -> r * cols + c

        Time:
            O(m * n * α(m * n))

            We process every cell and at most four neighbors. Each DSU
            union/find operation takes amortized O(α(m * n)) time, where
            α is the inverse Ackermann function.

            Since α(n) grows extremely slowly, this is effectively
            O(m * n) in practice.

        Space:
            O(m * n)

            The DSU stores parent/rank/size information for every grid cell.
        """

        rows, cols = len(grid), len(grid[0])
        dsu = DisjoinSetUnion(rows * cols)

        def index(r, c):
            return r * cols + c

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0"):
                            continue

                        if dsu.union(index(r, c), index(nr, nc)):
                            islands -= 1

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
        result = solution.number_of_islands_disjoint_set_union(grid)

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