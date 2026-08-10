from typing import Optional
from collections import deque

class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        val: The value stored in the node.
        left: Reference to the left child.
        right: Reference to the right child.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(nums: list[int | None]) -> Optional[TreeNode]:
    """
    Builds a binary tree from a level-order list representation.

    A value of None represents a missing child. The first element
    represents the root, and subsequent elements represent the left
    and right children of nodes in level-order.

    Args:
        nums: A list containing node values or None for missing nodes.

    Returns:
        The root of the constructed binary tree, or None if the input
        list is empty or its first element is None.

    Example:
        nums = [4, 2, 7, 1, 3, 6, 9]

        The resulting tree is:

              4
            /   \
           2     7
          / \   / \
         1   3 6   9
    """

    if not nums or nums[0] is None:
        return None

    root = TreeNode(nums[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nums):
        curr_node = queue.popleft()

        if i < len(nums):
            if nums[i] is not None:
                curr_node.left = TreeNode(nums[i])
                queue.append(curr_node.left)
            i += 1

        if i < len(nums):
            if nums[i] is not None:
                curr_node.right = TreeNode(nums[i])
                queue.append(curr_node.right)
            i += 1

    return root

def level_order_traversal(root: Optional[TreeNode]):
    """
    Traverses a binary tree in level-order using BFS.

    ```
    Nodes are visited from top to bottom and from left to right
    within each level.

    Args:
        root: The root of the binary tree.

    Returns:
        A list containing the values of the nodes in level-order.
        Returns an empty list if the tree is empty.

    Example:
        For the tree:

              4
            /   \
           2     7
          / \   / \
         1   3 6   9

        Returns:
            [4, 2, 7, 1, 3, 6, 9]
    """

    if not root:
        return []

    queue = deque([root])
    res = []

    while queue:
        queue_len = len(queue)

        for _ in range(queue_len):
            node = queue.popleft()
            res.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res


class Solution:
    """
    Solutions for LeetCode 226: Invert Binary Tree.

    Problem:
        Given the root of a binary tree, invert the tree and return
        its root.

    Approach:
        1. Visit every node in the binary tree.
        2. Swap the left and right children of each node.
        3. Continue until every node has been processed.

    Constraints:
        - The number of nodes is in the range [0, 100].
        - -100 <= Node.val <= 100

    Notes:
        - The tree is inverted in-place.
        - All three implementations visit every node exactly once.
        - BFS uses a queue.
        - Recursive DFS uses the call stack.
        - Iterative DFS uses an explicit stack.
    """

    def invert_binary_tree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree using Breadth-First Search (BFS).

        Intuition:
            - Inverting a tree means swapping the left and right
            children of every node.
            - BFS processes the tree level by level, so each node
            can be swapped when it is removed from the queue.

        Algorithm:
            1. Return None if the tree is empty.
            2. Add the root to a queue.
            3. Remove one node from the queue.
            4. Swap its left and right children.
            5. Add the new left and right children to the queue.
            6. Repeat until the queue is empty.
            7. Return the original root.

        Args:
            root: The root of the binary tree.

        Returns:
            The root of the inverted binary tree.

        Time:
            O(n), where n is the number of nodes in the tree.

        Space:
            O(n) in the worst case for the BFS queue.
        """

        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()

            # Swap left and right nodes.
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


    def invert_binary_tree_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree using recursive Depth-First Search (DFS).

        Intuition:
            - At every node, swap its left and right children.
            - Recursively invert the resulting left and right
            subtrees.

        Algorithm:
            1. Return None if the current node is None.
            2. Swap the current node's left and right children.
            3. Recursively invert the left subtree.
            4. Recursively invert the right subtree.
            5. Return the current node.

        Args:
            root: The root of the binary tree or subtree.

        Returns:
            The root of the inverted binary tree or subtree.

        Time:
            O(n), where n is the number of nodes in the tree.

        Space:
            O(h) for the recursive call stack, where h is the
            height of the tree. In the worst case, h = n.
        """

        if not root:
            return None

        root.left, root.right = root.right, root.left

        root.left = self.invert_binary_tree_dfs(root.left)
        root.right = self.invert_binary_tree_dfs(root.right)

        return root


    def invert_binary_tree_iterative_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree using iterative Depth-First Search (DFS).

        Intuition:
            - The recursive DFS approach can be converted to an
            iterative approach by explicitly maintaining a stack.
            - Every node is popped from the stack, its children are
            swapped, and its children are then added to the stack.

        Algorithm:
            1. Return None if the tree is empty.
            2. Add the root to a stack.
            3. Pop one node from the stack.
            4. Swap its left and right children.
            5. Add the new left and right children to the stack.
            6. Repeat until the stack is empty.
            7. Return the original root.

        Args:
            root: The root of the binary tree.

        Returns:
            The root of the inverted binary tree.

        Time:
            O(n), where n is the number of nodes in the tree.

        Space:
            O(h) on average for a balanced tree, where h is the
            height of the tree. In the worst case, the stack can
            contain O(n) nodes.
        """

        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()

            # Swap left and right nodes.
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (root: list[int | None], expected: list[int | None])
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([1, 2, 3, None, None, 4, 5], [1, 3, 2, 5, 4]),
        ([1, None, 2], [1, 2])
    ]

    for nums, expected in test_cases:
        head = build_tree_from_list(nums)

        head = solution.invert_binary_tree_iterative_dfs(head)

        result = level_order_traversal(head)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"root = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"root = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")