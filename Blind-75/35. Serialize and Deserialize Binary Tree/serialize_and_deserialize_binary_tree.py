from utils import TreeNode, build_tree_from_list, get_list_back_with_null
from collections import deque
from typing import Optional

class Solution:
    """
    Problem:
        - Design an algorithm to serialize a binary tree into a string and
          deserialize the string back into the original binary tree.
        - The serialized representation must preserve both node values and
          the tree structure.

    Approach:
        1. DFS Serialization/Deserialization:
            - Perform preorder traversal: root -> left -> right.
            - Store "N" for every None node so that the exact tree structure
              can be reconstructed.
            - During deserialization, consume the serialized values in the
              same preorder order and recursively rebuild the tree.

        2. BFS Serialization/Deserialization:
            - Perform level-order traversal using a queue.
            - Store "N" for every None child.
            - During deserialization, process nodes level by level and attach
              the next serialized values as their left and right children.

    Constraints:
        - The number of nodes in the tree is in the range [0, 10^4].
        - -1000 <= Node.val <= 1000.

    Notes:
        - Null markers ("N") are required to preserve the structure of the
          tree, especially when a node has only one child.
        - Both DFS and BFS approaches run in O(n) time.
        - The serialized string contains O(n) values, including null markers.
    """

    def serialize_binary_tree_dfs(self, root: Optional[TreeNode]) -> str:
        """
        Intuition:
            - A binary tree cannot be reconstructed from only its node values;
              we also need to know where the None children occur.
            - Use preorder DFS traversal (root -> left -> right).
            - Append "N" whenever we encounter a None node. This preserves
              enough structural information to reconstruct the exact tree.

        Algorithm:
            - Initialize an empty result list.
            - Recursively visit the tree using preorder traversal.
            - For each node:
                1. If the node is None, append "N".
                2. Otherwise, append its value.
                3. Recursively serialize its left subtree.
                4. Recursively serialize its right subtree.
            - Join all values with commas to produce the serialized string.

        Time:
            O(n), where n is the number of nodes in the tree.
            Each node and each null child position is processed once.

        Space:
            O(n), for the serialized result and the recursion stack.
        """

        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)


    def deserialize_binary_tree_dfs(self, data: str) -> Optional[TreeNode]:
        """
        Intuition:
            - The serialized string was created using preorder traversal, so
              we can reconstruct the tree by reading the values in the exact
              same order.
            - "N" represents a None node and tells us when a subtree ends.
            - Maintain an index pointing to the next value to consume.

        Algorithm:
            - Split the serialized string into individual values.
            - Initialize an index at the beginning of the list.
            - Recursively rebuild the tree:
                1. If the current value is "N", consume it and return None.
                2. Otherwise, create a TreeNode using the current value.
                3. Recursively construct the left subtree.
                4. Recursively construct the right subtree.
            - Return the reconstructed root.

        Time:
            O(n), where n is the number of serialized values.
            Every serialized value is processed exactly once.

        Space:
            O(n), for the split values, recursion stack, and reconstructed tree.
        """

        values = data.split(",")
        self.i = 0

        def dfs() -> Optional[TreeNode]:
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

    def serialize_binary_tree_bfs(self, root: Optional[TreeNode]) -> str:
        """
        Intuition:
            - Instead of recursively traversing the tree, process it level
              by level using BFS.
            - Store "N" for None children so that the exact structure,
              including missing children, is preserved.
            - A queue allows us to visit nodes in level-order.

        Algorithm:
            - If the root is None, return "N".
            - Initialize a queue with the root.
            - While the queue is not empty:
                1. Remove the next node from the queue.
                2. If it is None, append "N".
                3. Otherwise, append its value.
                4. Add its left and right children to the queue.
            - Join the collected values with commas.

        Time:
            O(n), where n is the number of nodes in the tree.
            Each node and its child positions are processed once.

        Space:
            O(n), for the queue and serialized result.
        """

        if not root:
            return "N"

        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                res.append("N")
                continue

            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(res)


    def deserialize_binary_tree_bfs(self, data: str) -> Optional[TreeNode]:
        """
        Intuition:
            - The serialized data is in level-order, so reconstruct the tree
              in the same order.
            - Each non-null node has two corresponding serialized positions:
              one for its left child and one for its right child.
            - A queue keeps track of nodes whose children still need to be
              assigned.

        Algorithm:
            - Split the serialized string into values.
            - If the first value is "N", the tree is empty, so return None.
            - Create the root from the first value and put it into a queue.
            - Maintain an index pointing to the next serialized value.
            - While the queue is not empty:
                1. Remove the next parent node.
                2. Read the next value for its left child.
                3. If it is not "N", create the left child and add it to
                   the queue.
                4. Read the next value for its right child.
                5. If it is not "N", create the right child and add it to
                   the queue.
            - Return the reconstructed root.

        Time:
            O(n), where n is the number of serialized values.
            Each value is processed exactly once.

        Space:
            O(n), for the queue, serialized values, and reconstructed tree.
        """

        values = data.split(",")
        if values[0] == "N":
            return None

        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()

            if values[index] != "N":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1

            if values[index] != "N":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        return root


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int | None], expected: list[int | None])
        ([1, 2, 3, None, None, 4, 5], [1, 2, 3, None, None, 4, 5]),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
    ]

    for nums, expected in test_cases:
        root = build_tree_from_list(nums)

        ser = solution.serialize_binary_tree_bfs(root)
        deser = solution.deserialize_binary_tree_bfs(ser)

        result = get_list_back_with_null(deser)

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