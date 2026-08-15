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