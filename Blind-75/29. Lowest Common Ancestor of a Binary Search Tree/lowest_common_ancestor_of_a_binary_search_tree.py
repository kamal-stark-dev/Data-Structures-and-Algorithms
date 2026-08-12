from utils import TreeNode, build_tree_from_list

class Solution:
    """
    Problem:
    - Given a Binary Search Tree (BST) and two nodes `p` and `q`,
      find their lowest common ancestor (LCA).
    - The LCA is the lowest node in the tree that has both `p` and
      `q` as descendants. A node is considered a descendant of itself.
    - Since the tree is a BST, for every node:
        - Values in the left subtree are smaller.
        - Values in the right subtree are larger.
    - `p` and `q` are guaranteed to exist in the BST and all node
      values are unique.

    Approach:
    1. Use the BST property to determine where `p` and `q` can be located
       relative to the current node.
    2. If both `p` and `q` are smaller than the current node, their LCA
       must be in the left subtree.
    3. If both `p` and `q` are larger than the current node, their LCA
       must be in the right subtree.
    4. Otherwise, the current node is the first node where the paths to
       `p` and `q` split, so it is their lowest common ancestor.
    5. Implement the same logic using both recursion and iteration.

    Constraints:
    - Number of nodes: [2, 10^5]
    - -10^9 <= Node.val <= 10^9
    - All node values are unique.
    - p != q
    - Both `p` and `q` exist in the BST.

    Notes:
    - The BST property allows us to avoid traversing the entire tree.
    - A node can be the LCA of itself and another node.
    - The solution takes O(h) time, where `h` is the height of the BST.
    - In the worst case, a highly unbalanced BST has h = n.
    """

    def lowest_common_ancestor_of_a_binary_search_tree_recursive(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Find the lowest common ancestor of `p` and `q` recursively.

        Intuition:
        - In a BST, all values in the left subtree are smaller than the
          current node, while all values in the right subtree are larger.
        - If both `p` and `q` are smaller than the current node, their LCA
          must be somewhere in the left subtree.
        - If both `p` and `q` are larger than the current node, their LCA
          must be somewhere in the right subtree.
        - Otherwise, the current node is the LCA because `p` and `q` are
          on different sides of the current node, or one of them is the
          current node itself.

        Algorithm:
        - If `root`, `p`, or `q` is missing, return `None`.
        - If both `p` and `q` are smaller than `root`, recursively search
          the left subtree.
        - If both `p` and `q` are larger than `root`, recursively search
          the right subtree.
        - Otherwise, return `root` because it is the lowest node where the
          paths to `p` and `q` diverge.

        Time:
            O(h), where `h` is the height of the BST.

        Space:
            O(h), due to the recursive call stack.
        """

        if not root or not p or not q:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowest_common_ancestor_of_a_binary_search_tree_recursive(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowest_common_ancestor_of_a_binary_search_tree_recursive(root.right, p, q)

        return root


    def lowest_common_ancestor_of_a_binary_search_tree_iterative(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Find the lowest common ancestor of `p` and `q` iteratively.

        Intuition:
        - The BST property lets us determine which subtree can contain the
          LCA without searching both subtrees.
        - If both target values are greater than the current node, both
          targets must be in the right subtree.
        - If both target values are smaller than the current node, both
          targets must be in the left subtree.
        - Otherwise, the current node is the first node where the paths to
          `p` and `q` split, making it their lowest common ancestor.
        - This also handles the case where `root` is equal to `p` or `q`.

        Algorithm:
        - Start at the root.
        - While the current node exists:
            - If both `p` and `q` are greater than the current node,
              move to the right child.
            - If both `p` and `q` are smaller than the current node,
              move to the left child.
            - Otherwise, return the current node as the LCA.
        - Return `None` if no LCA is found.

        Time:
            O(h), where `h` is the height of the BST.

        Space:
            O(1), since only a pointer to the current node is maintained.
        """

        if not root or not p or not q:
            return None

        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr



if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (root: list[int | None], p: int, q: int, expected: int)
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
    ]

    for nums, p, q, expected in test_cases:
        root = build_tree_from_list(nums)
        result = solution.lowest_common_ancestor_of_a_binary_search_tree_iterative(root, TreeNode(p), TreeNode(q))
        result = result.val

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