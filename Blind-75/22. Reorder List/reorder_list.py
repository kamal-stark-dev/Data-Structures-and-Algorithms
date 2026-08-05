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
    """
    if nums is None:
        return None

    dummy = ListNode()
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next


def get_list_back(head: ListNode) -> list[int]:
    """
    Converts a linked list back into a Python list.

    Args:
        head: Head of the linked list.

    Returns:
        A list containing the node values in order.
    """
    curr = head
    nums = []
    while curr:
        nums.append(curr.val)
        curr = curr.next
    return nums


class Solution:
    """
    Problem:
        Reorder a singly linked list from:

            L0 → L1 → ... → Ln-1 → Ln

        into:

            L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

        The node values cannot be modified; only the links between
        nodes may be changed.

    Approach:
        1. Store all nodes in an array and reconnect from both ends
           (brute force).
        2. Recursively reorder by pairing nodes from the front and back.
        3. Find the middle, reverse the second half, and merge the
           two halves alternately (optimal).

    Constraints:
        - Number of nodes: [1, 5 * 10^4]
        - 1 <= Node.val <= 1000

    Notes:
        - All methods modify the linked list in-place.
        - The reverse-and-merge solution is the optimal approach.
    """

    def reorder_list_brute_force(self, head: Optional[ListNode]) -> None:
        """
        Intuition:
            Store every node in a list so the front and back nodes can be
            accessed directly. Then reconnect them in alternating order.

        Algorithm:
            1. Traverse the linked list and store each node in an array.
            2. Use two pointers, one at the beginning and one at the end.
            3. Alternately connect the left and right nodes.
            4. Terminate the reordered list with None.

        Time:
            O(n)

        Space:
            O(n)
        """

        if not head:
            return

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1

        nodes[i].next = None

        return


    def reorder_list_recursion(self, head: Optional[ListNode]) -> None:
        """
        Intuition:
            Reach the end of the list recursively, then reconnect nodes
            while the recursion unwinds. A front pointer moves forward
            as the recursion returns from the back.

        Algorithm:
            1. Recursively traverse to the last node.
            2. During backtracking, connect the current tail node after
            the current front node.
            3. Advance the front pointer.
            4. Stop when the front and back pointers meet or cross.

        Time:
            O(n)

        Space:
            O(n)
            (Recursive call stack)
        """

        def recurse(root: ListNode, curr: ListNode) -> ListNode:
            if not curr:
                return root

            root = recurse(root, curr.next)
            if not root:
                return None

            temp = None
            if root == curr or root.next == curr:
                curr.next = None
            else:
                temp = root.next
                root.next = curr
                curr.next = temp

            return temp

        head = recurse(head, head.next)


    def reorder_list_reverse_and_merge(self, head: Optional[ListNode]) -> None:
        """
        Intuition:
            Split the list into two halves, reverse the second half, then
            merge the two lists by alternating nodes. This avoids using
            extra memory while producing the required ordering.

        Algorithm:
            1. Use the slow and fast pointer technique to find the middle.
            2. Split the list into two halves.
            3. Reverse the second half.
            4. Merge the first half and reversed second half by
            alternating nodes.

        Time:
            O(n)

        Space:
            O(1)
        """

        # find middle element
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second list
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge the two lists one by one
        first, second = head, prev

        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2

        return


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], expected: list[int])
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([67], [67]),
    ]

    for nums, expected in test_cases:
        head = build_linked_list(nums)

        solution.reorder_list_reverse_and_merge(head) # returns None

        result = get_list_back(head)

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