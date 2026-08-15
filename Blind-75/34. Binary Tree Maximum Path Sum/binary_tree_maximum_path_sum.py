from utils import TreeNode, build_tree_from_list
from typing import Optional

class Solution:
    """
    Problem:
        Given the root of a binary tree, find the maximum path sum of any
        non-empty path in the tree.

        A path can start and end at any nodes, does not need to pass through
        the root, and cannot visit the same node more than once.

    Approach:
        1. For each node, calculate the maximum downward path sum that can
           be obtained from its left and right subtrees.
        2. Treat the current node as the highest node in a path and calculate
           the path sum using both its left and right contributions.
        3. Keep track of the maximum path sum found anywhere in the tree.

    Constraints:
        - Number of nodes is in the range [1, 3 * 10^4].
        - Node values are in the range [-1000, 1000].

    Notes:
        - A path may contain nodes from both the left and right subtrees,
          with the current node connecting them.
        - A negative subtree contribution should be ignored because adding
          it would decrease the path sum.
        - The path does not have to include the root.
    """

    def binary_tree_maximum_path_sum_dfs_brute(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum binary tree path sum using a brute-force DFS.

        Intuition:
            - For every node, consider that node as the highest/connecting
              node of a potential path.
            - To calculate the best path through that node, independently
              find the best downward path from its left and right subtrees.
            - If a subtree's best downward path has a negative sum, ignore it.
            - The `dfs` function visits every node as a potential path
              junction, while `getMax` recomputes the best downward path
              for each subtree.

        Algorithm:
            1. `getMax` recursively calculates the maximum downward path
               starting from a given node.
            2. For each node visited by `dfs`, calculate:
                   node.val + left_max + right_max
               where `left_max` and `right_max` are the best non-negative
               downward paths from the two subtrees.
            3. Update `res` with the maximum path sum found.
            4. Continue DFS through the left and right children.

        Time:
            O(n^2)

        Space:
            O(h), recursive call stack.

        Where:
            - n is the number of nodes.
            - h is the height of the tree.

        Note:
            The O(n^2) time complexity comes from repeatedly calling
            `getMax` for overlapping subtrees. In the worst case, such as
            a highly unbalanced tree, this results in quadratic work.
        """

        def getMax(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = getMax(root.left)
            right = getMax(root.right)
            path = root.val + max(left, right)
            return max(0, path) # ignore the path if sum is negative

        res = float("-inf")
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0

            left = getMax(root.left)
            right = getMax(root.right)
            res = max(res, root.val + left + right)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res


    def binary_tree_maximum_path_sum_dfs(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum binary tree path sum using a single DFS.

        Intuition:
            - At each node, there are two different values to consider.
            - The path passing through the current node can use both its left
              and right subtree contributions.
            - The path returned to the parent can only use one side, because
              a path that continues upward cannot branch into both children.
            - Negative subtree contributions are ignored because they would
              reduce the total path sum.
            - A global `res` keeps track of the best complete path found
              anywhere in the tree.

        Algorithm:
            1. Recursively calculate the best downward path from the left
               subtree.
            2. Recursively calculate the best downward path from the right
               subtree.
            3. Ignore negative contributions using `max(0, ...)`.
            4. Treat the current node as the highest node of a potential
               complete path:
                   root.val + left_max + right_max
            5. Update `res` with this complete path sum.
            6. Return the best single-branch path to the parent:
                   root.val + max(left_max, right_max)

        Time:
            O(n)

        Space:
            O(h), recursion call stack.

        Where:
            - n is the number of nodes.
            - h is the height of the tree.
            - O(h) space is used by the recursive call stack.
        """

        res = float("-inf")

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0

            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))

            res = max(res, root.val + left_max + right_max)
            return root.val + max(left_max, right_max)

        dfs(root)
        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (root: list[int | None], expected: int)
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([3, 9, 20, None, None, 15, 7], 47),
    ]

    for nums, expected in test_cases:
        root = build_tree_from_list(nums)
        result = solution.binary_tree_maximum_path_sum_dfs_brute(root)

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