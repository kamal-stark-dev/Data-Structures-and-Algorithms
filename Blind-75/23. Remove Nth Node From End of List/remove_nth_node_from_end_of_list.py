from typing import Optional


class ListNode:
    """
    Represents a node in a singly linked list.

    Attributes:
        val: Integer value stored in the node.
        next: Reference to the next node in the list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(nums: Optional[list[int]] = None) -> Optional[ListNode]:
    """
    Builds a singly linked list from a list of integers.

    Args:
        nums: List of integer values.

    Returns:
        The head of the constructed linked list.

    Example:
        build_linked_list([1, 2, 3])
        -> 1 -> 2 -> 3 -> None
    """
    if nums is None:
        return None

    dummy = ListNode()
    curr = dummy

    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next


def get_list_back(head: Optional[ListNode]) -> list[int]:
    """
    Converts a linked list back into a Python list.

    Args:
        head: Head of the linked list.

    Returns:
        A list containing the node values in order.

    Example:
        1 -> 2 -> 3 -> None
        -> [1, 2, 3]
    """
    curr = head
    nums = []

    while curr:
        nums.append(curr.val)
        curr = curr.next

    return nums


class Solution:
    """
    LeetCode 19: Remove Nth Node From End of List.

    Problem:
        Given the head of a singly linked list, remove the nth node
        from the end of the list and return the head of the modified list.

    Approaches:
        1. Brute force using an array of node references.
        2. Two-pass solution by first calculating the list length.
        3. Recursive solution by processing nodes from the end.
        4. Two-pointer solution that removes the node in one pass.

    Key Insight:
        In the two-pointer approach, maintain a fixed distance of `n`
        nodes between the right and left pointers. When the right pointer
        reaches the end, the left pointer is positioned immediately before
        the node that needs to be removed.

    Constraints:
        - 1 <= number of nodes <= 30
        - 0 <= Node.val <= 100
        - 1 <= n <= number of nodes
    """

    def remove_nth_node_from_end_of_list_brute_force(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end using an auxiliary array.

        Intuition:
            Store references to every node in a Python list. This gives
            direct access to the node at any index.

            If the linked list contains `size` nodes, the nth node from
            the end is located at index `size - n` from the beginning.

        Algorithm:
            1. Traverse the linked list and store every node in `nodes`.
            2. Calculate the index of the node to remove:
               `removeIndex = len(nodes) - n`.
            3. If the node to remove is the head, return `head.next`.
            4. Otherwise, connect the previous node directly to the
               node after the node being removed.
            5. Return the original head.

        Example:
            [1, 2, 3, 4, 5], n = 2

            removeIndex = 5 - 2 = 3

            Remove node at index 3 -> value 4.

            Result:
                [1, 2, 3, 5]

        Time:
            O(n), where n is the number of nodes.

        Space:
            O(n), because every node reference is stored in an array.
        """

        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        removeIndex = len(nodes) - n

        if removeIndex == 0:
            return head.next

        nodes[removeIndex - 1].next = nodes[removeIndex].next

        return head


    def remove_nth_node_from_end_of_list_two_pass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end using two passes.

        Intuition:
            First determine the total number of nodes in the list.
            Once the size is known, the nth node from the end can be
            converted into an index from the beginning.

            The node to remove has zero-based index:
                size - n

            Therefore, its previous node is at index:
                size - n - 1

        Algorithm:
            1. Traverse the list once to calculate its size.
            2. If `n == size`, the head itself must be removed.
            3. Otherwise, calculate the position of the previous node.
            4. Traverse the list a second time until reaching that node.
            5. Skip the target node by updating the `next` pointer.
            6. Return the head.

        Example:
            [1, 2, 3, 4, 5], n = 2

            size = 5
            target index = 5 - 2 = 3

            The node at index 3 is `4`, so:
                3 -> 5

            Result:
                [1, 2, 3, 5]

        Time:
            O(n), because the list is traversed at most twice.

        Space:
            O(1), because only a constant number of pointers are used.
        """

        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next

        # Removing the head.
        if size == n:
            delNode = head
            head = head.next
            del delNode
            return head

        # Find the node immediately before the target node.
        idx = size - n
        i = 1
        curr = head

        while i < idx:
            i += 1
            curr = curr.next

        delNode = curr.next

        if curr.next:
            curr.next = curr.next.next

        del delNode

        return head


    def remove_nth_node_from_end_of_list_recursion(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end using recursion.

        Intuition:
            Recursion allows us to process the linked list from the end
            back toward the beginning.

            Every time the recursive call returns, we move one position
            backward from the end. By decrementing `n`, we can identify
            the nth node from the end.

        Algorithm:
            1. Recursively process the remainder of the linked list.
            2. When recursion returns, decrement `n`.
            3. When `n` becomes zero, the current node is the node to remove.
            4. Return the current node's next node to skip it.
            5. For all other nodes, return the current node unchanged.

        Example:
            [1, 2, 3, 4, 5], n = 2

            Recursion reaches the end and unwinds:

                5 -> position 1 from end
                4 -> position 2 from end

            Therefore, node `4` is removed.

            Result:
                [1, 2, 3, 5]

        Time:
            O(n), because every node is visited once.

        Space:
            O(n), because the recursive call stack can contain
            all nodes in the list.
        """

        def rec(node, n):
            """
            Recursively removes the nth node from the end.

            Args:
                node: Current node being processed.
                n: Mutable counter tracking the position from the end.

            Returns:
                The head of the modified sublist.
            """

            if not node:
                return None

            node.next = rec(node.next, n)

            # We are now processing nodes from the end toward the head.
            n[0] -= 1

            if n[0] == 0:
                # Remove the current node.
                return node.next

            return node

        return rec(head, [n])


    def remove_nth_node_from_end_of_list_two_pointers(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end using two pointers.

        Intuition:
            Keep two pointers, `left` and `right`, separated by `n`
            nodes.

            Once `right` reaches the end of the list, `left` will be
            positioned immediately before the node that needs to be
            removed.

            A dummy node is placed before the head so that removing the
            head uses the exact same logic as removing any other node.

        Algorithm:
            1. Create a dummy node pointing to `head`.
            2. Set `left` to the dummy and `right` to the head.
            3. Move `right` forward by `n` nodes.
            4. Move both pointers forward together until `right`
               reaches the end.
            5. At this point, `left.next` is the node to remove.
            6. Skip that node with:
                   left.next = left.next.next
            7. Return `dummy.next`.

        Example:
            [1, 2, 3, 4, 5], n = 2

            After moving `right` two nodes ahead, maintain the same
            distance while moving both pointers.

            When `right` reaches the end:

                left -> 3
                         |
                         v
                         4 -> 5

            `left.next` is node `4`, so remove it:

                3 -> 5

            Result:
                [1, 2, 3, 5]

        Why the dummy node helps:
            If `n` equals the length of the list, the head must be
            removed. Without a dummy node, this requires a special case.
            With a dummy node:

                dummy -> 1 -> 2 -> 3

            `left` naturally ends at `dummy`, so:
                left.next = left.next.next

            removes the head without special handling.

        Time:
            O(n), because the right and left pointers each traverse
            the list at most once.

        Space:
            O(1), because only a constant number of pointers are used.

        Follow-up:
            This is a one-pass solution because we do not need to first
            calculate the length of the linked list.
        """

        dummy = left = ListNode(0, head)
        right = head

        # Create a gap of n nodes between left and right.
        while n > 0:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end.
        while right:
            left = left.next
            right = right.next

        # left.next is the nth node from the end.
        left.next = left.next.next

        return dummy.next


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], n: int, expected: list[int])
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ]

    for nums, n, expected in test_cases:
        head = build_linked_list(nums)

        head = solution.remove_nth_node_from_end_of_list_two_pointers(
            head,
            n,
        )

        result = get_list_back(head)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"nums = {nums}\n"
            f"n = {n}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"nums = {nums}\n"
            f"n = {n}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")