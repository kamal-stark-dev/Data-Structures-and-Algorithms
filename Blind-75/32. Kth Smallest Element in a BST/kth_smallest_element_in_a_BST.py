from utils import TreeNode, build_tree_from_list
from typing import Optional

class Solution:
    """
    Problem:
        Given the root of a Binary Search Tree (BST) and an integer k,
        return the kth smallest value (1-indexed) among all nodes in the tree.

    Approach:
        Implement multiple solutions using different traversal techniques:
        1. Store the inorder traversal in a list and return the kth element.
        2. Use recursive inorder DFS while tracking the remaining k.
        3. Use iterative inorder DFS with an explicit stack.
        4. Use Morris inorder traversal to achieve O(1) auxiliary space.

    Constraints:
        - The number of nodes is n.
        - 1 <= k <= n <= 10^4
        - 0 <= Node.val <= 10^4

    Notes:
        - In a BST, inorder traversal visits nodes in ascending order.
        - Therefore, the kth visited node during inorder traversal is the
          kth smallest element.
        - The iterative DFS and Morris traversal avoid storing all node values.
    """

    def kth_smallest_element_in_a_BST_brute_force(self, root: Optional[TreeNode], k: int) -> int:
        """
        Return the kth smallest value using a brute-force approach.

        Intuition:
            - A BST's inorder traversal is sorted, but we can avoid relying on
                the BST property by collecting every node's value first.
            - After collecting all values, sort them in ascending order.
            - The kth element in the sorted list is the kth smallest value.

        Algorithm:
            1. Traverse the entire tree using preorder DFS.
            2. Store every node's value in `res`.
            3. Sort `res` in ascending order.
            4. Return `res[k - 1]` since k is 1-indexed.

        Time:
            O(n log n), where n is the number of nodes.
            Traversing the tree takes O(n), and sorting the n values takes
            O(n log n).

        Space:
            O(n), for storing the values of all nodes.
            The recursive DFS stack additionally requires O(h), where h is
            the height of the tree.
        """

        res = []
        def preorder(node: Optional[TreeNode]) -> None:
            if not node:
                return

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        res.sort()
        return res[k - 1]


    def kth_smallest_element_in_a_BST_inorder(self, root: Optional[TreeNode], k: int) -> int:
        """
        Return the kth smallest value using inorder traversal and a list.

        Intuition:
            - An inorder traversal of a BST visits nodes in sorted order.
            - Store every visited value in a list, then return the value
              at index k - 1 because k is 1-indexed.

        Algorithm:
            1. Perform a recursive inorder traversal: left -> root -> right.
            2. Append each node's value to `res`.
            3. Return `res[k - 1]`.

        Time:
            O(n), where n is the number of nodes in the tree.
            Every node is visited and stored.

        Space:
            O(n), for the result list and the recursive call stack.
        """

        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res[k - 1]


    def kth_smallest_element_in_a_BST_dfs(self, root: Optional[TreeNode], k: int) -> int:
        """
        Return the kth smallest value using recursive inorder DFS.

        Intuition:
            - Inorder traversal of a BST produces values in ascending order.
            - Instead of storing the entire traversal, keep track of how many
              nodes remain before reaching the kth smallest node.
            - Once k reaches zero, save the current node's value and stop
              traversing unnecessary parts of the tree.

        Algorithm:
            1. Recursively traverse the left subtree.
            2. Decrement `cnt` when visiting the current node.
            3. When `cnt` becomes zero, the current node is the kth smallest.
            4. Otherwise, recursively traverse the right subtree.
            5. Use an early-return check to avoid unnecessary traversal after
               the answer has been found.

        Time:
            O(n) in the worst case, where n is the number of nodes.
            In practice, the early return may avoid visiting some nodes.

        Space:
            O(h), where h is the height of the tree, due to the recursion stack.
        """

        cnt = k
        res = root.val

        def dfs(node: TreeNode):
            nonlocal cnt, res
            if not node:
                return

            dfs(node.left)

            if cnt == 0: # for early return when res is found
                return
            cnt -= 1
            if cnt == 0:
                res = node.val
                return

            dfs(node.right)

        dfs(root)
        return res


    def kth_smallest_element_in_a_BST_iterative_dfs(self, root: Optional[TreeNode], k: int) -> int:
        """
        Return the kth smallest value using iterative inorder DFS.

        Intuition:
            - Inorder traversal of a BST produces nodes in ascending order.
            - An explicit stack can simulate recursive inorder traversal
              without storing all node values.
            - Stop as soon as the kth node is visited.

        Algorithm:
            1. Start at the root and push every node along the leftmost path
               onto the stack.
            2. Pop the top node, which is the next node in inorder traversal.
            3. Decrement k.
            4. If k becomes zero, return the current node's value.
            5. Otherwise, move to the current node's right subtree and repeat.

        Time:
            O(h + k), where h is the height of the tree.
            We first traverse down a path of at most h nodes and then visit
            nodes until reaching the kth smallest element.

            More generally, the worst-case time is O(n).

        Space:
            O(h), where h is the height of the tree, for the explicit stack.
        """

        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() # leftmost node
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right # go right and repeat


    def kth_smallest_element_in_a_BST_morris_traversal(self, root: Optional[TreeNode], k: int) -> int:
        """
        Return the kth smallest value using Morris inorder traversal.

        Intuition:
            - Inorder traversal of a BST produces values in ascending order.
            - Morris traversal performs inorder traversal without recursion
              or an explicit stack.
            - It temporarily modifies the tree by creating a "thread" from
              each node's inorder predecessor back to the current node.
            - The temporary links are removed after they are no longer needed,
              restoring the original tree structure.

        Algorithm:
            1. Start with `curr` at the root.
            2. If `curr` has no left child:
                - Visit `curr`.
                - Decrement k.
                - Move to `curr.right`.
            3. Otherwise, find the inorder predecessor (`ip`) of `curr`,
               which is the rightmost node in `curr.left`.
            4. If the predecessor has no thread:
                - Create a temporary thread from `ip` to `curr`.
                - Move to `curr.left`.
            5. If the predecessor already points to `curr`:
                - Remove the temporary thread.
                - Visit `curr`.
                - Decrement k.
                - Move to `curr.right`.
            6. Return the current node's value when k reaches zero.

        Time:
            O(n), where n is the number of nodes.
            Although finding an inorder predecessor can require walking
            through multiple nodes, each edge is traversed only a constant
            number of times during Morris traversal.

        Space:
            O(1) auxiliary space.
            Morris traversal uses temporary pointers in the tree instead of
            recursion or an explicit stack.
        """

        curr= root

        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                # find inorder predecessor
                ip = curr.left
                while ip.right and ip.right != curr:
                    ip = ip.right

                if not ip.right: # create thread to curr
                    ip.right = curr
                    curr = curr.left
                else: # delete thread to curr
                    ip.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (root: list[int | None], k: int, expected: int)
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ]

    for nums, k, expected in test_cases:
        root = build_tree_from_list(nums)
        result = solution.kth_smallest_element_in_a_BST_morris_traversal(root, k)

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