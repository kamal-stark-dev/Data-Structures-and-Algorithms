from collections import deque
from disjoint_set_union import DisjointSetUnion

class Solution:
    """
    Problem:
        Given n nodes labeled from 0 to n - 1 and a list of undirected
        edges, determine whether the graph forms a valid tree.

        A valid tree must satisfy two conditions:
            1. It must be connected.
            2. It must not contain any cycle.

        For an undirected graph with n nodes, another useful property is:
            A connected graph is a tree if and only if it has exactly n - 1 edges.

        Since the graph contains no duplicate edges or self-loops, we can
        use any of the following approaches:
            - DFS: Check for cycles and connectivity.
            - BFS: Check for cycles and connectivity.
            - DSU: Detect cycles while building connected components.

    Approach:
        1. First check whether the number of edges is exactly n - 1.
           If not, the graph cannot be a tree.
        2. Use either DFS/BFS to verify that all nodes are connected and
           that no cycle exists.
        3. Alternatively, use Disjoint Set Union (DSU) to detect cycles
           and verify that all nodes belong to one connected component.

    Constraints:
        - 1 <= n <= 2000
        - 0 <= edges.length <= 5000
        - edges[i].length == 2
        - 0 <= a_i, b_i < n
        - a_i != b_i
        - No duplicate edges or self-loops.

    Notes:
        - The graph is undirected, so every edge [u, v] is represented as
          both u -> v and v -> u in the adjacency list.
        - In DFS/BFS, the parent node must be ignored when checking for
          cycles because the edge back to the parent is expected.
        - With exactly n - 1 edges, checking connectivity is enough to
          establish that the graph is a tree.
        - DSU detects a cycle when an edge connects two nodes that already
          belong to the same connected component.
    """

    def graph_valid_tree_dfs(self, n: int, edges: list[list[int]]) -> bool:
        """
        Check whether the graph forms a valid tree using DFS.

        Intuition:
            A tree must be connected and must not contain a cycle.

            We can use DFS to explore the graph:
                - If we encounter an already visited node that is not the
                  parent of the current node, we have found a cycle.
                - After DFS finishes, every node must have been visited;
                  otherwise, the graph is disconnected.

            We can also use the important tree property that a tree with
            n nodes must contain exactly n - 1 edges. Therefore, if the
            edge count is different, we can immediately return False.

        Algorithm:
            1. Check whether len(edges) == n - 1.
               If not, return False.
            2. Build an adjacency list for the undirected graph.
            3. Start DFS from node 0.
            4. Keep track of the parent of each node.
            5. If a neighbor is the parent, ignore it because this is the
               normal edge back to the node we came from.
            6. If a neighbor has already been visited, a cycle exists.
               Return False.
            7. Otherwise, recursively visit the neighbor.
            8. After DFS completes, check whether all n nodes were visited.
               If yes, the graph is connected and therefore is a tree.

        Time:
            O(n + E), where E = len(edges).

            Building the adjacency list takes O(E), and DFS visits every
            node and edge at most once.

        Space:
            O(n + E).

            The adjacency list requires O(n + E) space, while the visited
            set and recursion stack require O(n) additional space.
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
        Check whether the graph forms a valid tree using BFS.

        Intuition:
            A tree must be connected and contain no cycles.

            BFS can detect a cycle by checking whether we encounter a
            previously visited neighbor that is not the parent of the
            current node.

            As with DFS, we first check that the graph contains exactly
            n - 1 edges. If that condition holds and BFS can reach every
            node without finding a cycle, the graph is a valid tree.

        Algorithm:
            1. Check whether len(edges) == n - 1.
               If not, return False.
            2. Build an adjacency list for the undirected graph.
            3. Start BFS from node 0.
            4. Store both the current node and its parent in the queue.
            5. For every neighbor:
                - Ignore the parent node.
                - If the neighbor is already visited, a cycle exists.
                - Otherwise, add the neighbor to the queue.
            6. After BFS finishes, check whether all n nodes were visited.
            7. If every node was visited without finding a cycle, the graph
               is a valid tree.

        Time:
            O(n + E), where E = len(edges).

            Building the adjacency list takes O(E), and BFS processes each
            node and edge at most once.

        Space:
            O(n + E).

            The adjacency list takes O(n + E) space, while the visited set
            and BFS queue require O(n) additional space.
        """

        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        queue = deque([(0, -1)])
        visited.add(0)

        while queue:
            node, parent = queue.popleft()

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False

                visited.add(neighbor)
                queue.append((neighbor, node))

        return len(visited) == n

    def graph_valid_tree_dsu(self, n: int, edges: list[list[int]]) -> bool:
        """
        Check whether the graph forms a valid tree using Disjoint Set Union.

        Intuition:
            DSU (Union-Find) is useful for detecting cycles and tracking
            connected components.

            Initially, every node belongs to its own component.

            For every edge (u, v):
                - If u and v are already in the same component, adding this
                  edge creates a cycle.
                - Otherwise, merge their two components.

            Since a tree with n nodes must contain exactly n - 1 edges,
            we first verify the edge count. If every edge can be added
            without creating a cycle, the graph has no cycles. With n - 1
            edges, this also guarantees that all nodes form one connected
            component.

        Algorithm:
            1. Check whether len(edges) == n - 1.
               If not, return False.
            2. Create a DSU containing n separate components.
            3. For every edge (u, v):
                - Attempt to union u and v.
                - If union returns False, u and v are already connected,
                  so the edge creates a cycle. Return False.
            4. After processing all edges, check that there is exactly
               one connected component.
            5. Return True if there is one component.

        Time:
            O(E * α(n)), where E = len(edges) and α(n) is the inverse
            Ackermann function.

            With path compression and union by rank/size, α(n) grows
            extremely slowly and is effectively constant for practical
            input sizes.

        Space:
            O(n).

            The DSU stores parent/rank/size information for each node.
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
        result = solution.graph_valid_tree_bfs(n, edges)

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