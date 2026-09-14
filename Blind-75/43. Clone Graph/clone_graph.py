from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

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

    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
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


def checkDeepCopy(node1: Optional[Node], node2: Optional[Node]) -> bool:
    """
    """

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
        result = solution.clone_graph(node)

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