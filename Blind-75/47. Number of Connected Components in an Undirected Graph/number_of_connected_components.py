from collections import deque
from disjoint_set_union import DisjointSetUnion

class Solution:
    """
    Problem:
        - Given an undirected graph with n nodes and a list of edges,
          return the number of connected components in the graph.

        - A connected component is a group of nodes where every node
          is reachable from every other node in that group.

    Approach:
        1. Build an adjacency list to represent the undirected graph.
        2. Traverse the graph using DFS or BFS and mark every visited node.
        3. Every time we find an unvisited node, it represents the start
           of a new connected component.
        4. Alternatively, use Disjoint Set Union (DSU) to merge nodes
           connected by an edge and count the remaining sets.

    Constraints:
        - 1 <= n <= 2000
        - 1 <= edges.length <= 5000
        - No repeated edges.
        - The graph is undirected.

    Notes:
        - Isolated nodes are also considered connected components.
        - DFS and BFS explicitly traverse the graph.
        - DSU keeps track of connected groups without explicitly
          traversing the graph.
    """

    def number_of_connected_components_dfs(
        self, n: int, edges: list[list[int]]
    ) -> int:
        """
        Intuition:
            - Initially, every node can be considered the start of a
              potential connected component.
            - If we start DFS from an unvisited node, DFS will visit every
              node belonging to the same connected component.
            - Therefore, each time we encounter an unvisited node, we have
              discovered one new connected component.

        Algorithm:
            - Build an adjacency list for the undirected graph.
            - Maintain a set of visited nodes.
            - Iterate through every node from 0 to n - 1.
            - If the node has not been visited:
                1. Run DFS from that node.
                2. DFS marks every node reachable from it as visited.
                3. Increment the component count.
            - Return the total number of components.

        Time:
            O(n + E), where E is the number of edges.
            - Building the adjacency list takes O(E).
            - DFS visits every node and edge at most once.

        Space:
            O(n + E)
            - The adjacency list stores all nodes and edges.
            - The visited set uses O(n) space.
            - The recursive DFS call stack can use O(n) space.
        """

        def dfs(node: int) -> None:
            if node in visited:
                return

            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        components = 0
        visited = set()

        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1

        return components

    def number_of_connected_components_bfs(
        self, n: int, edges: list[list[int]]
    ) -> int:
        """
        Intuition:
            - Every unvisited node represents a possible new connected
              component.
            - Starting BFS from that node visits every node that can be
              reached from it.
            - Once BFS finishes, the entire connected component has been
              visited.
            - Therefore, we increment the component count once for every
              BFS traversal.

        Algorithm:
            - Build an adjacency list for the undirected graph.
            - Maintain a set of visited nodes.
            - Iterate through every node from 0 to n - 1.
            - For every unvisited node:
                1. Add it to a queue.
                2. Mark it as visited.
                3. Repeatedly remove nodes from the queue.
                4. Add their unvisited neighbors to the queue.
                5. Continue until the queue becomes empty.
                6. Increment the component count.
            - Return the total number of components.

        Time:
            O(n + E), where E is the number of edges.
            - Building the adjacency list takes O(E).
            - BFS visits every node and edge at most once.

        Space:
            O(n + E)
            - The adjacency list stores all nodes and edges.
            - The visited set uses O(n) space.
            - The BFS queue can contain O(n) nodes.
        """

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        components = 0
        visited = set()

        for node in range(n):
            if node in visited:
                continue

            queue = deque([node])
            visited.add(node)

            while queue:
                node = queue.popleft()

                for neighbor in adj[node]:
                    if neighbor in visited:
                        continue

                    visited.add(neighbor)
                    queue.append(neighbor)

            components += 1

        return components

    def number_of_connected_components_dsu(
        self, n: int, edges: list[list[int]]
    ) -> int:
        """
        Intuition:
            - Initially, every node belongs to its own separate set,
              so there are n connected components.
            - For every edge (u, v), u and v belong to the same connected
              component, so we merge their sets.
            - If the two nodes already belong to the same set, the edge
              does not reduce the number of components.
            - After processing all edges, the number of remaining sets is
              exactly the number of connected components.

        Algorithm:
            - Initialize a Disjoint Set Union structure with n nodes.
            - Initially, every node is its own component.
            - For every edge [u, v]:
                1. Find the representative of u.
                2. Find the representative of v.
                3. If their representatives are different, union the two
                   sets and decrease the component count.
            - Return the number of remaining components.

        Time:
            O(E * α(n)), where E is the number of edges and α(n) is the
            inverse Ackermann function.
            - With path compression and union by rank/size, each DSU
              operation is effectively constant time for practical input
              sizes.

        Space:
            O(n)
            - The DSU stores parent/rank or size information for each node.
        """

        dsu = DisjointSetUnion(n)

        for u, v in edges:
            dsu.union(u, v)

        return dsu.getComponentCount()


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (n: int, edges: list[list[int]], expected: int)
        (
            5,
            [[0, 1], [1, 2], [3, 4]],
            2
        ),
        (
            5,
            [[0, 1], [1, 2], [2, 3], [3, 4]],
            1
        ),
    ]

    for n, edges, expected in test_cases:
        result = solution.number_of_connected_components_dfs(n, edges)

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