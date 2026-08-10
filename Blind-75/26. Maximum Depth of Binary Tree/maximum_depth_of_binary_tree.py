from utils import TreeNode, build_tree_from_list
from typing import Optional
from collections import deque


class Solution:
    """
    Problem:
        Given the root of a binary tree, return its maximum depth.

        The maximum depth is the number of nodes along the longest path
        from the root node down to the farthest leaf node.

    Approach:
        1. Iterative DFS:
            - Use a stack to traverse the tree depth-first.
            - Store each node together with its current depth.
            - Keep track of the maximum depth encountered.

        2. BFS:
            - Use a queue to traverse the tree level by level.
            - Increment the depth after processing each level.
            - The number of processed levels is the maximum depth.

        3. Recursive DFS:
            - Recursively calculate the maximum depth of the left and
              right subtrees.
            - The depth of the current node is one plus the larger
              subtree depth.

    Constraints:
        - The number of nodes is in the range [0, 10^4].
        - -100 <= Node.val <= 100.

    Notes:
        - An empty tree has a maximum depth of 0.
        - A tree containing only the root has a maximum depth of 1.
        - All three approaches visit every node at most once.
    """

    def maximum_depth_of_binary_tree_iterative_dfs(self, root: Optional[TreeNode]):
        """
        Intuition:
            - The maximum depth is the largest depth of any node in the tree.
            - We can perform a depth-first traversal using an explicit stack
              instead of recursion.
            - Each stack entry stores both the node and its depth.
            - Whenever we visit a node, update the maximum depth seen so far.

        Algorithm:
            - Return 0 if the tree is empty.
            - Initialize a stack with the root and its depth, 1.
            - While the stack is not empty:
                - Pop a node and its depth.
                - Update the maximum depth.
                - Add the left and right children to the stack with
                  depth + 1.
            - Return the maximum depth found.

        Time:
            O(n)

        Space:
            O(n)
            - In the worst case, the stack can contain O(n) nodes.
        """

        if not root:
            return 0

        stack = [[root, 1]]
        maxDepth = 0

        while stack:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)

            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])

        return maxDepth


    def maximum_depth_of_binary_tree_bfs(self, root: Optional[TreeNode]):
        """
        Intuition:
            - A binary tree can be traversed level by level using BFS.
            - Each level represents one additional node in the path from
              the root.
            - Therefore, the number of levels in the tree is its maximum depth.

        Algorithm:
            - Return 0 if the tree is empty.
            - Initialize a queue with the root.
            - While the queue is not empty:
                - Record the number of nodes in the current level.
                - Process all nodes belonging to that level.
                - Add their non-null children to the queue.
                - Increment the depth after the entire level is processed.
            - Return the final depth.

        Time:
            O(n)

        Space:
            O(n)
            - The queue can contain O(n) nodes in the worst case.
        """

        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            q_len = len(queue)

            for _ in range(q_len):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth


    def maximum_depth_of_binary_tree_dfs(self, root: Optional[TreeNode]):
        """
        Intuition:
            - The maximum depth of a tree is one more than the maximum
              depth of its left and right subtrees.
            - For an empty subtree, the depth is 0.
            - This naturally leads to a recursive DFS solution.

        Algorithm:
            - If the current node is None, return 0.
            - Recursively find the maximum depth of the left subtree.
            - Recursively find the maximum depth of the right subtree.
            - Return 1 plus the larger of the two subtree depths.

        Time:
            O(n)
            - Every node is visited exactly once.

        Space:
            O(log n) in case of a balanced tree,
            O(n) in case of a degenerated tree.
            - This space is used by the recursive call stack.
        """

        if not root:
            return 0

        return 1 + max(
            self.maximum_depth_of_binary_tree_dfs(root.left),
            self.maximum_depth_of_binary_tree_dfs(root.right),
        )


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (root: list[int | None], expected: int)
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([1], 1),
    ]

    for nums, expected in test_cases:
        head = build_tree_from_list(nums)

        result = solution.maximum_depth_of_binary_tree_dfs(head)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"head = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"head = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")