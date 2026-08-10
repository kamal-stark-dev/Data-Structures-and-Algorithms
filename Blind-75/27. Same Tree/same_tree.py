from utils import TreeNode, build_tree_from_list, level_order_traversal
from typing import Optional
from collections import deque

class Solution:
    """
    Problem:
        Given the roots of two binary trees p and q, determine whether
        the two trees are the same.

        Two binary trees are considered the same if they are structurally
        identical and corresponding nodes have the same value.

    Approach:
        1. Compare corresponding nodes from both trees.
        2. If both nodes are None, they represent the same empty subtree.
        3. If only one node is None or their values differ, the trees are
        not the same.
        4. Otherwise, continue comparing their left and right subtrees.

    Constraints:
        - The number of nodes in both trees is in the range [0, 100].
        - -10^4 <= Node.val <= 10^4.

    Notes:
        - The order of nodes matters because the trees must be structurally
        identical.
        - A tree with the same values but a different structure is not
        considered the same.
    """

    def same_tree_iterative_dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Intuition:
            - Compare corresponding nodes from both trees simultaneously.
            - Use a stack to perform depth-first traversal iteratively.
            - Each pair of corresponding nodes must either both be None or
              have the same value.

        Algorithm:
            - Initialize a stack with the root pair `(p, q)`.
            - While the stack is not empty:
                - Pop a pair of corresponding nodes.
                - If both nodes are None, continue.
                - If only one node is None or their values differ, return False.
                - Push the corresponding left and right child pairs.
            - If all corresponding nodes match, return True.

        Time:
            O(n), where n is the number of nodes visited.

        Space:
            O(h) on average and O(n) in the worst case, where h is the
            height of the trees.
        """

        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True


    def same_tree_dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Intuition:
            - Two trees are identical if their root nodes match and their
              corresponding left and right subtrees are also identical.
            - This naturally maps to recursive depth-first traversal.

        Algorithm:
            - If both nodes are None, return True because both subtrees
              are empty.
            - If only one node is None, return False because their structures
              are different.
            - If the node values differ, return False.
            - Recursively compare the left subtrees and right subtrees.
            - Return True only if both corresponding subtrees are identical.

        Time:
            O(n), where n is the number of nodes visited.

        Space:
            O(h) for the recursion stack, where h is the height of the trees.
            In the worst case, h = n.
        """

        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.same_tree_dfs(p.left, q.left) and self.same_tree_dfs(p.right, q.right)


    def same_tree_iterative_bfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Intuition:
            - Compare the two trees level by level using pairs of
              corresponding nodes.
            - Every pair must have the same structure and node value.

        Algorithm:
            - Initialize a queue with the root pair `(p, q)`.
            - While the queue is not empty:
                - Process each pair of corresponding nodes.
                - If both nodes are None, continue.
                - If only one node is None or their values differ, return False.
                - Add the corresponding left and right child pairs to
                  the queue.
            - If all corresponding nodes match, return True.

        Time:
            O(n), where n is the number of nodes visited.

        Space:
            O(h), where h is the maximum width of the trees.
            In the worst case, O(n).
        """

        queue = deque([(p, q)])

        while queue:
            q_len = len(queue)

            for _ in range(q_len):
                node1, node2 = queue.popleft()

                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False

                queue.append((node1.left, node2. left))
                queue.append((node1.right, node2.right))

        return True


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (p: list[int | None], q: list[int | None], expected: bool)
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
        ([67], [67], True),
    ]

    for list1, list2, expected in test_cases:
        p = build_tree_from_list(list1)
        q = build_tree_from_list(list2)

        result = solution.same_tree_dfs(p, q)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"list1 = {list1}\n"
            f"list2 = {list2}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"list1 = {list1}\n"
            f"list2 = {list2}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")