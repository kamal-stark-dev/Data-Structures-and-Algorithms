from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class Solution:
    """
    Problem:
        Given a reference to a node in a connected undirected graph,
        return a deep copy (clone) of the entire graph.

        Each node contains:
            - val: an integer value
            - neighbors: a list of references to neighboring nodes

        A deep copy means that every node in the cloned graph must be
        a newly created object. The cloned nodes should preserve the
        same values and connections as the original graph, but must not
        share node objects with the original graph.

    Approach:
        We need to traverse every node in the original graph and create
        exactly one corresponding clone for each node.

        A hash map is used to maintain the relationship:

            original node -> cloned node

        This mapping is important because graphs can contain cycles.
        When we encounter a node that has already been cloned, we reuse
        its existing clone instead of creating another one.

        We can solve the problem using either:

        1. DFS (Depth-First Search)
            - Recursively traverse the graph.
            - Create a clone before visiting its neighbors.
            - Store the clone in the hash map.
            - Recursively clone every neighbor.

        2. BFS (Breadth-First Search)
            - Use a queue to traverse the graph level by level.
            - Create the clone of a node when it is first discovered.
            - Process its neighbors and connect their cloned nodes.

    Why do we need a hash map?

        Consider a graph containing a cycle:

            1 -> 2 -> 3 -> 1

        Without a hash map, DFS/BFS could repeatedly visit the same
        nodes forever or create multiple copies of the same node.

        The hash map guarantees:
            - Every original node gets exactly one clone.
            - Cycles can be handled safely.
            - The original and cloned graphs remain structurally identical.

    Constraints:
        - Number of nodes is in the range [0, 100].
        - 1 <= Node.val <= 100
        - Node values are unique.
        - There are no repeated edges.
        - There are no self-loops.
        - The graph is connected.
        - Every node can be reached from the given node.

    Complexity:
        Let V = number of vertices (nodes)
        Let E = number of edges.

        Time:
            O(V + E)

        Space:
            O(V)

        We visit every node and every edge once, while the hash map
        and traversal data structures require O(V) additional space.
    """

    def clone_graph_dfs(self, node: Optional[Node]) -> Optional[Node]:
        """
        Clone the graph using Depth-First Search (DFS).

        Intuition:
            We want to create one clone for every original node.

            For each node:
                1. If it has already been cloned, return the existing clone.
                2. Otherwise, create a new node with the same value.
                3. Store the original -> clone relationship immediately.
                4. Recursively clone all of its neighbors.
                5. Attach the cloned neighbors to the cloned node.

            The most important step is storing the clone in oldToNew
            BEFORE recursively visiting the neighbors.

            This handles cycles correctly.

            For example:

                1 <-> 2

            While cloning 1:
                clone 1
                store 1 -> clone 1
                visit 2

            While cloning 2:
                clone 2
                store 2 -> clone 2
                visit 1

            Node 1 is already present in oldToNew, so we return its
            existing clone instead of recursively cloning it again.

        Algorithm:
            1. Create an empty dictionary oldToNew.
            2. Define a recursive DFS function.
            3. If the current node already exists in oldToNew,
               return its clone.
            4. Create a new node with the same value.
            5. Store the mapping from the original node to its clone.
            6. Traverse every neighbor of the current node.
            7. Recursively clone each neighbor and add it to the
               cloned node's neighbors.
            8. Return the cloned node.
            9. If the input node is None, return None.

        Time:
            O(V + E)

            Every node and every edge is processed once.

        Space:
            O(V)

            The hash map stores V node mappings and the DFS recursion
            stack can contain up to O(V) nodes.
        """

        oldToNew = {}

        def dfs(node: Node) -> Node:
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node else None

    def clone_graph_bfs(self, node: Optional[Node]) -> Optional[Node]:
        """
        Clone the graph using Breadth-First Search (BFS).

        Intuition:
            We traverse the original graph using a queue.

            Whenever we encounter a node for the first time, we create
            its clone and store the mapping:

                original node -> cloned node

            When processing a node, we look at each of its neighbors.

            If a neighbor has not been cloned yet:
                - Create its clone.
                - Store it in oldToNew.
                - Add the original neighbor to the queue.

            Regardless of whether the neighbor is new or already cloned,
            we connect the current cloned node to the neighbor's clone.

            The hash map prevents us from creating multiple clones and
            allows BFS to safely handle cycles.

        Algorithm:
            1. If node is None, return None.
            2. Create an empty dictionary oldToNew.
            3. Create a queue and add the starting node.
            4. Create the clone of the starting node and store the mapping.
            5. While the queue is not empty:
                a. Remove the next original node from the queue.
                b. Iterate through all of its neighbors.
                c. If a neighbor has not been cloned:
                    - Create its clone.
                    - Store the mapping.
                    - Add the neighbor to the queue.
                d. Connect the current cloned node to the cloned neighbor.
            6. Return the clone corresponding to the starting node.

        Time:
            O(V + E)

            Every node is processed once and every edge is examined once.

        Space:
            O(V)

            The hash map and BFS queue can contain up to O(V) nodes.
        """

        if not node:
            return None

        oldToNew = {}

        queue = deque([node])
        oldToNew[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                oldToNew[curr].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]

def checkDeepCopy(node1: Optional[Node], node2: Optional[Node]) -> bool:
    """Checks if the graphs are a deep copy of each other or not."""

    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False

    # maps an original node object id to its cloned node object id
    mapping: dict[int, int] = dict()

    def dfs(n1: Optional[Node], n2: Optional[Node]) -> bool:
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False

        if n1.val != n2.val or id(n1) == id(n2):
            return False

        if len(n1.neighbors) != len(n2.neighbors):
            return False

        if id(n1) in mapping:
            # verify that this original node always maps to the exact same cloned node
            return mapping[id(n1)] == id(n2)

        # record mapping pair
        mapping[id(n1)] = id(n2)

        for neighbor1, neighbor2 in zip(n1.neighbors, n2.neighbors):
            if not dfs(neighbor1, neighbor2):
                return False

        return True

    return dfs(node1, node2)

def printGraph(start_node: Optional[Node]) -> None:
    """Returns adjacency list of the graph node."""

    if not start_node:
        return []

    graph = []
    visited = set()

    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        curr = queue.popleft()

        graph.append([neighbor.val for neighbor in curr.neighbors])

        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return graph

if __name__ == "__main__":
    solution = Solution()

    startNode = node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    test_cases = [
        # (node: Optional[Node], expected: Optional[Node])
        (startNode, startNode),
        (None, None),
        (Node(1), Node(1)),
    ]

    for node, expected in test_cases:
        result = solution.clone_graph_bfs(node)

        assert checkDeepCopy(result, expected), (
            f"\n\nTest case failed!\n"
            f"node = {printGraph(node)}\n"
            f"expected = {printGraph(expected)}\n"
            f"got = {printGraph(result)}\n"
        )

        print(
            f"node = {printGraph(node)}\n"
            f"expected = {printGraph(expected)}\n"
            f"got = {printGraph(result)}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")