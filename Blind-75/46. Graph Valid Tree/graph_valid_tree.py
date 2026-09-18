from collections import deque
from disjoint_set_union import DisjointSetUnion

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

    def graph_valid_tree_dfs(self, n: int, edges: list[list[int]]) -> bool:
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

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True

        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        return dfs(0, -1) and len(visited) == n

    def graph_valid_tree_bfs(self, n: int, edges: list[list[int]]) -> bool:
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

        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        queue = deque([(0, -1)])

        while queue:
            node, parent = queue.popleft()
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False

                queue.append((neighbor, node))

        return len(visited) == n

    def graph_valid_tree_dsu(self, n: int, edges: list[list[int]]) -> bool:
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

        if len(edges) != n - 1:
            return False

        dsu = DisjointSetUnion(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return False

        return dsu.getComponentCount() == 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (n: int, edges: list[list[int]], expected: bool)
        (
            5,
            [[0, 1], [0, 2], [0, 3], [1, 4]],
            True
        ),
        (
            5,
            [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],
            False
        ),
        (
            6,
            [[0, 1], [2, 3], [3, 4], [4, 5], [5, 2]],
            False
        ),
    ]

    for n, edges, expected in test_cases:
        result = solution.graph_valid_tree_dsu(n, edges)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"n = {n}\n"
            f"edges = {edges}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"n = {n}\n"
            f"edges = {edges}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")