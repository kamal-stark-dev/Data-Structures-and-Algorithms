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

def get_list_back_with_null(root: Optional[TreeNode]):
    """
    Traverses a binary tree in level-order using Breadth-First Search (BFS).

    Nodes are visited from top to bottom and from left to right within
    each level. Missing children are represented by `None` values so that
    the structure of the tree is preserved in the resulting list.

    Trailing `None` values are removed because they do not provide any
    additional structural information.

    Args:
        root: The root node of the binary tree. If `root` is `None`,
            the tree is empty.

    Returns:
        A list containing the node values in level-order, with `None`
        used as a placeholder for missing children. Returns an empty
        list if the tree is empty.

    Example:
        For the tree:

              3
             / \
            9   20
               /  \
              15   7

        Returns:
            [3, 9, 20, None, None, 15, 7]

        The two `None` values represent the missing children of node `9`.
    """

    if not root:
        return []

    queue = deque([root])
    res = []

    while queue:
        node = queue.popleft()

        if node is None:
            res.append(None)
            continue

        res.append(node.val)

        # add children even if they are None
        queue.append(node.left)
        queue.append(node.right)

    # Remove trailing None values.
    # They don't provide additional structural information
    while res and res[-1] is None:
        res.pop()

    return res