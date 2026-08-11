from utils import TreeNode, build_tree_from_list
from typing import Optional
from collections import deque

class Solution:
    """
    Problem:
        Given two binary trees, root and subRoot, determine whether subRoot
        is a subtree of root.

        A subtree consists of a node and all of its descendants. Therefore,
        subRoot must match a subtree of root in both:
            - Node values
            - Tree structure

    Approaches:
        1. Recursive DFS + same_tree()
        2. BFS + same_tree()
        3. Iterative DFS + same_tree()
        4. Tree serialization + substring search

    Constraints:
        - root contains 1 to 2000 nodes.
        - subRoot contains 1 to 1000 nodes.
        - Node values are in the range [-10^4, 10^4].

    Notes:
        The key challenge is that matching only node values is not enough.
        The structure of the trees must also match.

        For example:

              4        4
             /          \
            1            1

        These trees have the same values but are not the same tree because
        the child is on a different side.
    """

    def same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Determine whether two binary trees are identical.

        Intuition:
            Two trees are identical if:
                1. Their current node values are equal.
                2. Their left subtrees are identical.
                3. Their right subtrees are identical.

            We recursively compare the corresponding nodes of both trees.

        Algorithm:
            1. If both nodes are None, the trees match at this position.
            2. If exactly one node is None, the structures differ.
            3. If their values differ, the trees differ.
            4. Recursively compare the left children.
            5. Recursively compare the right children.
            6. Both subtrees must match for the trees to be identical.

        Time:
            O(k), where k is the number of nodes in the smaller tree
            being compared.

        Space:
            O(h), where h is the height of the trees due to recursion.
        """

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)


    def subtree_of_another_tree_dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determine whether subRoot exists as a subtree of root using DFS.

        Intuition:
            Every node in root could potentially be the root of subRoot.

            At each node, we:
                1. Check whether the tree starting at this node is identical
                   to subRoot.
                2. If not, search the left subtree.
                3. If not, search the right subtree.

            The helper method same_tree performs the actual tree comparison.

        Algorithm:
            1. If subRoot is None, return True because an empty tree is
               considered a subtree.
            2. If root is None, return False because there is no node left
               to match subRoot.
            3. Check whether root and subRoot represent identical trees.
            4. If not, recursively search root.left.
            5. If not, recursively search root.right.

        Time:
            O(n * m), where:
                n = number of nodes in root
                m = number of nodes in subRoot.

            In the worst case, same_tree may compare O(m) nodes at many
            different nodes of root.

        Space:
            O(h_root + h_subRoot), where the space comes from recursive
            DFS calls and recursive tree comparisons.
        """

        if not subRoot:
            return True # as each tree contains a null node

        if not root:
            return False

        return (
            self.same_tree(root, subRoot) or
            self.subtree_of_another_tree_dfs(root.left, subRoot) or
            self.subtree_of_another_tree_dfs(root.right, subRoot)
        )


    def subtree_of_another_tree_bfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determine whether subRoot exists as a subtree of root using BFS.

        Intuition:
            Instead of recursively visiting every node, use a queue to
            traverse root level by level.

            Every node in root is a possible starting point for subRoot.
            At each node, use same_tree to determine whether the subtree
            rooted at that node is identical to subRoot.

        Algorithm:
            1. If subRoot is None, return True.
            2. If root is None, return False.
            3. Add root to a queue.
            4. While the queue is not empty:
                a. Remove a node from the queue.
                b. Check whether it matches subRoot using same_tree.
                c. Add its left child to the queue if it exists.
                d. Add its right child to the queue if it exists.
            5. Return False if no matching subtree is found.

        Time:
            O(n * m), where:
                n = number of nodes in root
                m = number of nodes in subRoot.

            In the worst case, same_tree can take O(m) time at each
            candidate node in root.

        Space:
            O(n + h_subRoot).

            The BFS queue can contain O(n) nodes in the worst case, while
            same_tree uses O(h_subRoot) recursion depth.
        """

        if not subRoot:
            return True
        if not root:
            return False

        queue = deque([root])

        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                node = queue.popleft()
                if self.same_tree(node, subRoot):
                    return True

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return False


    def subtree_of_another_tree_iterative_dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determine whether subRoot exists as a subtree using iterative DFS.

        Intuition:
            This approach is the iterative version of the recursive DFS
            solution.

            Instead of using the Python call stack, we explicitly maintain
            our own stack containing nodes that still need to be checked.

            Every node in root is a possible root of subRoot.

        Algorithm:
            1. If subRoot is None, return True.
            2. If root is None, return False.
            3. Push root onto a stack.
            4. While the stack is not empty:
                a. Pop a node.
                b. Check whether it matches subRoot using same_tree.
                c. Push its children onto the stack.
            5. Return False if no matching subtree is found.

        Time:
            O(n * m), where:
                n = number of nodes in root
                m = number of nodes in subRoot.

            In the worst case, same_tree may compare O(m) nodes for
            multiple nodes in root.

        Space:
            O(n + h_subRoot).

            The explicit DFS stack can contain O(n) nodes in the worst case,
            while same_tree uses O(h_subRoot) recursive space.
        """

        if not subRoot:
            return True
        if not root:
            return False

        stack = [root]

        while stack:
            node = stack.pop()

            if self.same_tree(node, subRoot):
                return True

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False


    def subtree_of_another_tree_serialize_and_find_substring(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determine whether subRoot is a subtree of root using serialization.

        Intuition:
            Convert both trees into strings using preorder traversal.

            The serialization must preserve both:
                - Node values
                - Tree structure

            Therefore, every None child is represented by a special marker.

            After serialization:
                tree structure matching
                    ↓
                becomes
                    ↓
                substring matching

            If the serialized subRoot appears inside the serialized root,
            then subRoot exists as a subtree of root.

        Why include None markers?
            Without None markers, different tree structures can produce the
            same preorder traversal.

            For example:

                1          1
               /            \
              2              2

            Both produce [1, 2] without null markers, even though their
            structures are different.

            Using a marker for None preserves the structure.

        Why prefix values with "="?
            The "=" separates node values from each other and prevents
            accidental matches involving parts of multi-digit or negative
            values.

            For example:
                "=12" should not accidentally match "=2".

        Algorithm:
            1. Serialize root using preorder traversal.
            2. Serialize subRoot using the same method.
            3. Check whether the serialized subRoot is a substring of the
               serialized root.
            4. If it is, return True; otherwise return False.

        Time:
            O(n + m), assuming linear-time substring matching, where:
                n = number of nodes in root
                m = number of nodes in subRoot.

            Serialization takes O(n + m), and substring matching is treated
            as O(n + m) for the intended algorithmic analysis.

        Space:
            O(n + m) for the serialized representations.

            Additionally, recursive serialization uses O(h) call-stack
            space, where h is the tree height.
        """

        def serialize(root: Optional[TreeNode]) -> str:
            """
            Serialize the tree using preorder traversal.

            Each node contributes its value, prefixed with "=" to avoid
            accidental substring matches between values.

            "X" is used for None children so that the serialization preserves
            the tree structure.

            Example:
                 1
                / \
               2   3

            becomes:
                "=1=2XX=3XX"

            Time:
                O(n), where n is the number of nodes.

            Space:
                O(n) for the serialized string + O(h) recursion stack.
            """

            if not root:
                return "X" # for null values - 'X'

            # preorder serialization
            return (
                f"={root.val}"
                + serialize(root.left)
                + serialize(root.right)
            )

        main_tree = serialize(root)
        sub_tree = serialize(subRoot)

        return sub_tree in main_tree


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (root: list[int | None], subRoot: list[int | None], expected: bool)
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    ]

    for nums, subNums, expected in test_cases:
        root = build_tree_from_list(nums)
        subRoot = build_tree_from_list(subNums)

        result = solution.subtree_of_another_tree_serialize_and_find_substring(root, subRoot)

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