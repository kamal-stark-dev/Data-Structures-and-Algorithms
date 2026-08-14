from utils import TreeNode, level_order_traversal_with_null
from typing import Optional

class Solution:
    """
    Problem:
        Construct a binary tree from its preorder and inorder traversals.

        Given two integer arrays, `preorder` and `inorder`, representing
        the preorder and inorder traversals of the same binary tree,
        reconstruct and return the original binary tree.

        Preorder traversal visits nodes in the order:
            root -> left subtree -> right subtree

        Inorder traversal visits nodes in the order:
            left subtree -> root -> right subtree

        The values in the tree are guaranteed to be unique.

    Approach:
        1. Use preorder to identify the root of each subtree.
        2. Use inorder to determine which values belong to the left
           and right subtrees.
        3. Recursively construct the left and right subtrees.

    Constraints:
        - 1 <= preorder.length <= 3000
        - inorder.length == preorder.length
        - Values in both traversals are unique.
        - Every value in inorder also appears in preorder.

    Notes:
        - The first value in preorder is always the root of the tree
          or current subtree.
        - The position of that value in inorder separates the left
          and right subtrees.
    """

    def construct_binary_tree_from_preorder_and_inorder_traversal_dfs(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        Reconstructs the binary tree using recursive DFS.

        Intuition:
            - The first value in preorder is always the root of the
              current subtree.
            - Find that root in inorder. All values to its left belong
              to the left subtree, while all values to its right belong
              to the right subtree.
            - Recursively repeat the same process for both subtrees.

        Algorithm:
            1. If either traversal is empty, return None.
            2. Take the first value from preorder as the root.
            3. Find the root's index in inorder.
            4. Use that index to split preorder and inorder into the
               left and right subtree portions.
            5. Recursively construct the left and right subtrees.
            6. Return the constructed root.

        Time:
            O(n^2) in the worst case.

            Finding the root in inorder takes O(n) per recursive call,
            and slicing the traversal arrays also takes O(n).
            In a highly unbalanced tree, this results in O(n^2) time.

        Space:
            O(n).

            Array slicing creates new lists, and the recursion can also
            reach O(n) depth in the worst case.
        """

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.construct_binary_tree_from_preorder_and_inorder_traversal_dfs(preorder[1: mid + 1], inorder[:mid])
        root.right = self.construct_binary_tree_from_preorder_and_inorder_traversal_dfs(preorder[mid + 1:], inorder[mid + 1:])

        return root


    def construct_binary_tree_from_preorder_and_inorder_traversal_hashmap_dfs(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        Reconstructs the binary tree using DFS and a hashmap.

        Intuition:
            - Preorder tells us which node should be created next.
              The first unused value in preorder is always the root
              of the current subtree.
            - The hashmap stores each value's index in inorder, allowing
              us to find the root's position in O(1) time.
            - The inorder range is used to determine the boundaries of
              the left and right subtrees.
            - Unlike the basic DFS solution, this approach avoids
              repeatedly searching inorder and avoids creating sliced
              copies of the traversal arrays.

        Algorithm:
            1. Build a hashmap mapping each inorder value to its index.
            2. Maintain `pre_idx` to point to the next root in preorder.
            3. Define a DFS function that receives the current inorder
               range `[left, right]`.
            4. If the range is empty, return None.
            5. Use `preorder[pre_idx]` as the current root and increment
               `pre_idx`.
            6. Look up the root's index in the inorder hashmap.
            7. Recursively construct the left subtree using
               `[left, mid - 1]`.
            8. Recursively construct the right subtree using
               `[mid + 1, right]`.
            9. Return the constructed root.

        Time:
            O(n).

            Building the hashmap takes O(n), and each node is processed
            exactly once. Hashmap lookups take O(1) on average.

        Space:
            O(n).

            The hashmap requires O(n) space, and the recursion stack can
            also require O(n) space in the worst case.
        """

        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)


    def construct_binary_tree_from_preorder_and_inorder_traversal_dfs_optimal(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        Reconstructs the binary tree using an optimized DFS with boundaries.

        Intuition:
            - Preorder determines the order in which nodes are created.
            - Inorder determines when the current subtree has reached
              its boundary.
            - Instead of searching for each root in inorder or storing
              an inorder hashmap, use `inIdx` to track the current
              position in inorder.
            - The `limit` parameter represents the value that marks the
              boundary of the current subtree.
            - When `inorder[inIdx] == limit`, the current subtree is
              complete and the recursion returns to its parent.

            For example, when constructing a node's left subtree, the
            node itself acts as the boundary. Once that node is reached
            in inorder, there are no more nodes belonging to the left
            subtree.

        Algorithm:
            1. Maintain `preIdx` for the next value to consume from
               preorder and `inIdx` for the next value to inspect in
               inorder.
            2. Define a DFS function that receives an inorder boundary
               called `limit`.
            3. If all preorder values have been consumed, return None.
            4. If the current inorder value equals `limit`, advance
               `inIdx` and return None because the current subtree
               has reached its boundary.
            5. Create a root using `preorder[preIdx]` and increment
               `preIdx`.
            6. Recursively build the left subtree using the current
               root value as its boundary.
            7. Recursively build the right subtree using the same
               boundary inherited by the current subtree.
            8. Return the constructed root.

        Time:
            O(n).

            Each node is processed once, and neither traversal requires
            searching or slicing.

        Space:
            O(n).

            No additional hashmap is required, but the recursive call
            stack can contain up to O(n) calls for a highly unbalanced
            tree.
        """

        preIdx = inIdx = 0

        def dfs(limit: int) -> Optional[TreeNode]:
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inIdx < len(inorder) and inorder[inIdx] == limit:
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1

            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root

        return dfs(float("inf"))


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (preorder: list[int], inorder: list[int], expected: list[int | None])
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
    ]

    for preorder, inorder, expected in test_cases:
        root: TreeNode = solution.construct_binary_tree_from_preorder_and_inorder_traversal_dfs_optimal(preorder, inorder)
        result: list[int | None] = level_order_traversal_with_null(root)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"preorder = {preorder}\n"
            f"inorder = {inorder}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"preorder = {preorder}\n"
            f"inorder = {inorder}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")