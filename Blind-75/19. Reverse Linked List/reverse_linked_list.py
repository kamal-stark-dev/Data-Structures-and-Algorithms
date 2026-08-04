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


def build_linked_list(nums: Optional[list[int]] = None) -> ListNode:
    """
    Builds a singly linked list from a list of integers.

    Args:
        nums: List of integer values.

    Returns:
        The head of the constructed linked list.
    """
    if nums is None:
        return []

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
        Given the head of a singly linked list, reverse the list
        and return the new head.

    Approach:
        1. Brute Force:
           - Copy all node values into an array.
           - Reverse the array.
           - Construct a new linked list from the reversed values.

        2. Recursion:
           - Recursively reverse the remainder of the list.
           - During the recursion unwind, reverse each link.

        3. Iteration:
           - Traverse the list once while keeping track of
             previous and current nodes.
           - Reverse each pointer in-place.

    Constraints:
        - Number of nodes is in the range [0, 5000].
        - -5000 <= Node.val <= 5000.

    Notes:
        - The iterative approach is the most space-efficient,
          requiring only O(1) extra space.
        - The recursive approach is elegant but uses O(n)
          call stack space.
    """

    def reverse_linked_list_brute_force(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
            Since reversing a Python list is straightforward,
            first extract all node values into an array. Reverse
            the array and rebuild a new linked list using the
            reversed values.

        Algorithm:
            1. Traverse the linked list and store every value.
            2. Reverse the list of values.
            3. Build and return a new linked list from the
            reversed values.

        Time:
            O(n)

        Space:
            O(n)
        """

        nums = get_list_back(head)
        nums.reverse()
        return build_linked_list(nums)


    def reverse_linked_list_recursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
            Let recursion reverse everything after the current
            node. Once the smaller subproblem is solved, make the
            next node point back to the current node. Finally,
            disconnect the current node's original forward link.

        Algorithm:
            1. If the list is empty, return None.
            2. Recursively reverse the remainder of the list.
            3. Set head.next.next = head to reverse the edge.
            4. Set head.next = None to avoid cycles.
            5. Return the new head obtained from the deepest
            recursive call.

        Time:
            O(n)

        Space:
            O(n)
            (Recursive call stack)
        """

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverse_linked_list_recursion(head.next)
            head.next.next = head
        head.next = None

        return newHead


    def reverse_linked_list_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
            Reverse the links one node at a time while traversing
            the list. Maintain references to the previous, current,
            and next nodes so no part of the list is lost.

        Algorithm:
            1. Initialize prev as None.
            2. Traverse the list using curr.
            3. Save curr.next.
            4. Reverse curr.next to point to prev.
            5. Advance prev and curr.
            6. Return prev as the new head.

        Time:
            O(n)

        Space:
            O(1)
        """

        prev, curr, nxt = None, head, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (head: Optional[ListNode], expected)
        (build_linked_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1]),
        (build_linked_list([1, 2]), [2, 1]),
        (build_linked_list([]), []),
        (build_linked_list([69]), [69]),
    ]

    for head, expected in test_cases:
        result = solution.reverse_linked_list_recursion(head)

        result = get_list_back(result)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"head = {get_list_back(head)}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"head = {get_list_back(head)}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")