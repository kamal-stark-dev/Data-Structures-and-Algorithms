from utils import TreeNode, build_tree_from_list
from typing import Optional
from collections import deque

class Solution:
    """
    Problem:
        Given the root of a binary tree, determine whether it is a valid
        binary search tree (BST).

        A valid BST must satisfy:
        - Every value in the left subtree is strictly less than the node's value.
        - Every value in the right subtree is strictly greater than the node's value.
        - Both subtrees must also satisfy the BST property.

    Approach:
        1. Perform a DFS traversal while maintaining a valid value range
           `(low, high)` for each node.
        2. For the left subtree, update the upper bound to the current node's value.
        3. For the right subtree, update the lower bound to the current node's value.
        4. If any node falls outside its allowed range, the tree is invalid.

    Constraints:
        - The number of nodes is in the range [1, 10^4].
        - -2^31 <= Node.val <= 2^31 - 1.

    Notes:
        - The BST property must be checked against all ancestors, not just
          the node's immediate children.
        - Bounds are strict because duplicate values are not allowed in a BST.
    """

    def validate_binary_search_tree_dfs(self, root: Optional[TreeNode]) -> bool:
        """
        Validate the binary tree using depth-first search with value bounds.

        Intuition:
            - A node's value is constrained not only by its parent, but also
              by every ancestor above it.
            - For example, if a node is in the right subtree of a node with
              value 5, it must be greater than 5, even if it is the left child
              of a node with value 10.
            - Pass the valid `(low, high)` range down the tree to enforce all
              ancestor constraints.

        Algorithm:
            - Start with the root having the range `(-inf, inf)`.
            - If the current node is outside its valid range, return False.
            - For the left child, keep the lower bound and set the upper bound
              to the current node's value.
            - For the right child, set the lower bound to the current node's
              value and keep the upper bound.
            - Recursively validate both subtrees.
            - An empty subtree is valid by definition.

        Time:
            O(n), where n is the number of nodes in the tree.
            Each node is visited exactly once.

        Space:
            O(h), where h is the height of the tree, due to the recursion stack.
            In the worst case, h = n for a completely skewed tree.
        """

        def helper(node, low, high):
            if not node:
                return True
            if node.val >= high or node.val <= low:
                return False

            return (
                helper(node.left, low, node.val)
                and
                helper(node.right, node.val, high)
            )

        low, high = float("-inf"), float("inf")
        return helper(root, low, high)


    def validate_binary_search_tree_bfs(self, root: Optional[TreeNode]) -> bool:
        """
        Validate the binary tree using breadth-first search with value bounds.

        Intuition:
            - Each node must satisfy a valid range determined by its ancestors.
            - Instead of passing these bounds recursively, store the node and
              its valid `(low, high)` range together in a queue.
            - A node is invalid if its value is not strictly between its bounds.

        Algorithm:
            - Return True immediately if the tree is empty.
            - Initialize a queue with the root and the range `(-inf, inf)`.
            - Remove one node and its bounds from the queue.
            - If the node's value is outside the bounds, return False.
            - Add the left child with the range `(low, node.val)`.
            - Add the right child with the range `(node.val, high)`.
            - Continue until all nodes have been processed.
            - If every node satisfies its valid range, return True.

        Time:
            O(n), where n is the number of nodes in the tree.
            Each node is added to and removed from the queue exactly once.

        Space:
            O(w), where w is the maximum width of the tree.
            In the worst case, w = O(n).
        """

        if not root:
            return True

        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            node, low, high = queue.popleft()

            if not (low < node.val < high):
                return False

            if node.left:
                queue.append((node.left, low, node.val))
            if node.right:
                queue.append((node.right, node.val, high))

        return True


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums, expected)
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([67], True),
    ]

    for nums, expected in test_cases:
        root = build_tree_from_list(nums)
        result = solution.validate_binary_search_tree_bfs(root)

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