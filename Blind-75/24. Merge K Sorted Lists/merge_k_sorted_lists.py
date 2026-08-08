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
        -

    Approach:
        1.
        2.
        3.

    Constraints:
        -

    Notes:
        -
    """

    def merge_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        """

        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next


    def merge_k_sorted_lists_brute_force(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Intuition:
            -

        Algorithm:
            -

        Time:
            O()

        Space:
            O()
        """

        nodes = []
        for list in lists:
            while list:
                nodes.append(list.val)
                list = list.next
        nodes.sort()

        dummy = curr = ListNode()
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next

        return dummy.next


    def merge_k_sorted_lists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Intuition:
            -

        Algorithm:
            -

        Time:
            O(n logn)

        Space:
            O(n)
        """

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None

                mergedLists.append(self.merge_lists(list1, list2))

            lists = mergedLists

        return lists[0]

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (lists: list[list[int]], expected: list[int])
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ]

    for lists, expected in test_cases:
        list_heads = []
        for list in lists:
            list_heads.append(build_linked_list(list))

        result = solution.merge_k_sorted_lists_brute_force(list_heads)
        result = get_list_back(result)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"lists = {lists}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"lists = {lists}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")