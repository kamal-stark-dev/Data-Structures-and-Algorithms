from utils import TreeNode, build_tree_from_list
from typing import Optional
from collections import deque

class Solution:
    """
    Problem:
    - Given the root of a binary tree, return the level order traversal
      of its nodes' values.
    - Level order traversal visits the tree one level at a time, from
      left to right.
    - The result should contain one list for each depth/level of the tree.

    Approach:
    1. DFS:
        - Traverse the tree recursively while keeping track of the current
          node's depth.
        - Use the depth as an index into the result list.
        - Create a new level when we first reach that depth.
    2. BFS:
        - Use a queue to process nodes level by level.
        - At the beginning of each iteration, record the number of nodes
          currently in the queue.
        - Process exactly those nodes to construct one level.
    3. Both approaches visit every node exactly once.

    Constraints:
    - Number of nodes: [0, 2000]
    - -1000 <= Node.val <= 1000

    Notes:
    - DFS naturally processes nodes in depth-first order, so the depth of
      each node is used to place its value into the correct level.
    - BFS naturally processes nodes level by level because a queue stores
      nodes in the order they are discovered.
    - If the tree is empty, return an empty list.
    """

    def binary_tree_level_order_traversal_dfs(self, root: Optional[TreeNode]):
        """
        Return the level order traversal using DFS.

        Intuition:
        - DFS normally explores one branch of the tree before moving to
          another branch, which does not directly produce level order.
        - We can still use DFS by keeping track of the depth of each node.
        - The depth tells us which sublist in `res` the node's value belongs to.
        - For example:
              depth 0 -> res[0]
              depth 1 -> res[1]
              depth 2 -> res[2]
        - Because we visit the left child before the right child, values
          within each level are also stored from left to right.

        Algorithm:
        - Initialize an empty result list.
        - Define a recursive DFS function that receives:
            - `node`: the current node.
            - `depth`: the node's depth in the tree.
        - If the node is `None`, return.
        - If this is the first node encountered at this depth, append a
          new empty list to `res`.
        - Append the current node's value to `res[depth]`.
        - Recursively visit the left child at `depth + 1`.
        - Recursively visit the right child at `depth + 1`.
        - Start DFS from the root at depth `0`.
        - Return `res`.

        Time:
            O(n), where `n` is the number of nodes in the tree.
            Every node is visited exactly once.

        Space:
            O(h) for the recursive call stack, where `h` is the height
            of the tree.

            The output itself requires O(n) space, but this is not
            counted as auxiliary space.
        """

        res = []

        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res


    def binary_tree_level_order_traversal_bfs(self, root: Optional[TreeNode]):
        """
        Return the level order traversal using BFS.

        Intuition:
        - BFS is a natural fit for level order traversal because it visits
          nodes based on their distance from the root.
        - A queue stores the nodes waiting to be processed.
        - At the beginning of each iteration, the queue contains exactly
          the nodes belonging to the current level.
        - By storing the current queue length, we can process only that
          level before moving on to the next one.

        Algorithm:
        - If the tree is empty, return an empty list.
        - Initialize a queue with the root node.
        - While the queue is not empty:
            - Store the current queue length as `qLen`.
            - Create an empty list for the current level.
            - Process exactly `qLen` nodes:
                - Remove a node from the front of the queue.
                - Add its value to the current level.
                - Add its left child to the queue if it exists.
                - Add its right child to the queue if it exists.
            - Append the completed level to `res`.
        - Return `res`.

        Time:
            O(n), where `n` is the number of nodes in the tree.
            Every node is added to and removed from the queue once.

        Space:
            O(w), where `w` is the maximum width of the tree.
            In the worst case, this can be O(n).

            The output itself requires O(n) space, but this is not
            counted as auxiliary space.
        """

        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            qLen = len(queue)
            level = []

            for _ in range(qLen):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (root: list[int | None], expected: list[list[int]])
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
        ([1], [[1]]),
        ([], []),
    ]

    for nums, expected in test_cases:
        root = build_tree_from_list(nums)
        result = solution.binary_tree_level_order_traversal_dfs(root)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")