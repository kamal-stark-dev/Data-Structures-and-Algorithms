from collections import deque

class Solution:
    """
    Problem:
        Given an m x n grid of heights, water can flow from a cell to a
        neighboring cell if the neighboring cell has height less than or
        equal to the current cell.

        The Pacific Ocean touches the top and left edges of the grid,
        while the Atlantic Ocean touches the bottom and right edges.

        Return all cells from which water can flow to both oceans.

    Approach:
        1. Instead of starting from every cell and checking whether water
           can reach both oceans, reverse the direction of the search.
        2. Start DFS/BFS from the ocean boundaries and move to neighboring
           cells whose height is greater than or equal to the current cell.
        3. Find the cells reachable from the Pacific and the cells reachable
           from the Atlantic. Their intersection is the answer.

    Constraints:
        - 1 <= m, n <= 200
        - 0 <= heights[r][c] <= 10^5

    Notes:
        The important observation is to reverse the water-flow direction.

        Normally, water flows from a higher/equal cell to a lower/equal cell.
        When searching backwards from an ocean, we can move from a cell to a
        neighboring cell only when:

            heights[neighbor] >= heights[current]

        This allows us to determine which cells can eventually reach each
        ocean without running a search from every individual cell.
    """

    def pacific_atlantic_water_flow_dfs(
        self,
        heights: list[list[int]]
    ) -> list[list[int]]:
        """
        Intuition:
            Normally, water flows from a higher/equal cell to a lower/equal
            neighboring cell. Checking every cell independently would require
            many DFS traversals.

            Instead, reverse the direction of the problem.

            Start DFS from the cells touching the Pacific Ocean and imagine
            water flowing backwards from the ocean into the island.

            From the current cell, we can move to a neighboring cell only if
            the neighboring cell is at least as high as the current cell:

                heights[nr][nc] >= heights[r][c]

            This is the reverse of the original water-flow condition.

            We perform the same process from the Atlantic Ocean.

            Any cell visited by both searches can send water to both oceans.

        Algorithm:
            1. Create two sets:
                   pac -> cells reachable from the Pacific
                   atl -> cells reachable from the Atlantic

            2. Run DFS from every cell on the left and top boundaries for
               the Pacific Ocean.

            3. Run DFS from every cell on the right and bottom boundaries for
               the Atlantic Ocean.

            4. During DFS, move to a neighboring cell only when:
                   heights[nr][nc] >= heights[r][c]

               This guarantees that the original water-flow direction would
               allow water to eventually travel from that neighbor to the
               current cell and then into the ocean.

            5. Iterate through the Pacific set and add cells that are also
               present in the Atlantic set to the result.

        Time:
            O(m * n)

            Each cell can be visited at most once for the Pacific DFS and
            once for the Atlantic DFS.

            Therefore:

                O(m * n) + O(m * n) = O(m * n)

        Space:
            O(m * n)

            The Pacific and Atlantic sets can each contain up to m * n cells.

            Additionally, the recursive DFS uses the call stack. In the
            worst case it can also reach O(m * n) depth.
        """

        def dfs(
            r: int,
            c: int,
            ocean: set[tuple[int, int]],
            prevHeight: int
        ) -> None:
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in ocean
                or heights[r][c] < prevHeight
            ):
                return

            ocean.add((r, c))

            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        rows, cols = len(heights), len(heights[0])

        pac, atl = set(), set()

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        res = []

        for (r, c) in pac:
            if (r, c) in atl:
                res.append([r, c])

        return res

    def pacific_atlantic_water_flow_bfs(
        self,
        heights: list[list[int]]
    ) -> list[list[int]]:
        """
        Intuition:
            Instead of starting from every cell and trying to determine
            whether water can reach both oceans, reverse the problem.

            Start BFS from all cells touching an ocean and move backwards
            into the grid.

            Original water flow:

                higher/equal cell -> lower/equal cell

            Reverse search:

                lower/equal current cell -> higher/equal neighbor

            Therefore, from a current cell we can visit a neighboring cell
            only when:

                heights[neighbor] >= heights[current]

            We perform one BFS starting from the Pacific boundaries and
            another BFS starting from the Atlantic boundaries.

            A cell reachable from both BFS traversals is a cell from which
            water can flow to both oceans.

        Algorithm:
            1. Create two boolean matrices:
                   pac[r][c] -> True if (r, c) can reach the Pacific
                   atl[r][c] -> True if (r, c) can reach the Atlantic

            2. Put all Pacific boundary cells into the Pacific BFS queue:
                   - left column
                   - top row

            3. Put all Atlantic boundary cells into the Atlantic BFS queue:
                   - right column
                   - bottom row

            4. For each BFS, visit a neighboring cell only if:
                   - it is inside the grid,
                   - it has not already been visited, and
                   - its height is greater than or equal to the current cell.

            5. After both BFS traversals finish, iterate through the grid.
               If:

                   pac[r][c] == True
                   and
                   atl[r][c] == True

               then water can flow from that cell to both oceans, so add
               [r, c] to the result.

        Time:
            O(m * n)

            Each cell is processed at most once in the Pacific BFS and once
            in the Atlantic BFS.

            The final traversal over the grid is also O(m * n).

            Therefore the overall complexity remains:

                O(m * n)

        Space:
            O(m * n)

            The Pacific and Atlantic boolean matrices each require O(m * n)
            space.

            The BFS queues can also contain O(m * n) cells in the worst case.

            Therefore the overall auxiliary space is O(m * n).
        """

        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]

        def bfs(source: list[tuple[int, int]], ocean: list[list[bool]]):
            queue = deque(source)

            while queue:
                r, c = queue.popleft()
                ocean[r][c] = True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0
                        or nr >= rows
                        or nc < 0
                        or nc >= cols
                        or ocean[nr][nc]
                        or heights[nr][nc] < heights[r][c]
                    ):
                        continue

                    queue.append((nr, nc))

        pacific = []
        atlantic = []

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []

        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (heights: list[list[int]], expected: list[list[int]])
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4]
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        ),
        (
            [
                [1]
            ],
            [[0, 0]]
        ),
    ]

    for heights, expected in test_cases:
        result = solution.pacific_atlantic_water_flow_bfs(heights)

        assert sorted(result) == sorted(expected), (
            f"\n\nTest case failed!\n"
            f"heights = {heights}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"heights = {heights}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")