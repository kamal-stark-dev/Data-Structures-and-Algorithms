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
        Given the heads of two sorted singly linked lists, merge them into a
        single sorted linked list by reusing the existing nodes. Return the
        head of the merged list.

    Approach:
        1. Compare the current nodes of both linked lists.
        2. Append the smaller node to the merged list.
        3. Continue until one list is exhausted, then attach the remaining nodes.

    Constraints:
        - The number of nodes in both lists is in the range [0, 50].
        - -100 <= Node.val <= 100.
        - Both input lists are sorted in non-decreasing order.

    Notes:
        - Three solutions are provided:
            * Brute force using a Python list.
            * Recursive merge.
            * Iterative merge (optimal).
        - The recursive and iterative solutions reuse the existing nodes instead
        of allocating new ones.
    """

    def merge_two_sorted_lists_brute_force(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
            Since both linked lists are already sorted, another simple solution is
            to extract all values into a Python list, sort them, and rebuild a new
            linked list from the sorted values.

        Algorithm:
            1. Convert both linked lists into Python lists.
            2. Combine the two lists.
            3. Sort the combined list.
            4. Construct and return a new linked list from the sorted values.

        Time:
            O((n + m) log(n + m))

        Space:
            O(n + m)

        Where n is the size of list1 and m is the size of list2.
        """

        list1 = get_list_back(list1)
        list2 = get_list_back(list2)
        list1.extend(list2)
        list1.sort()
        return build_linked_list(list1)


    def merge_two_sorted_lists_recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
            Since both lists are sorted, the smaller of the two current nodes must
            appear next in the merged list. Recursively merge the remainder of the
            lists after selecting that node.

        Algorithm:
            1. If either list is empty, return the other list.
            2. Compare the current nodes of both lists.
            3. Recursively merge the remainder of the lists.
            4. Return the smaller node as the current head.

        Time:
            O(n + m)

        Space:
            O(n + m)
            (Recursive call stack)

        Where n is the size of list1 and m is the size of list2.
        """

        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.merge_two_sorted_lists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_sorted_lists_recursive(list1, list2.next)
            return list2


    def merge_two_sorted_lists_iterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
            Traverse both sorted lists simultaneously and always append the smaller
            current node to the merged list. Once one list is exhausted, append the
            remaining nodes from the other list.

        Algorithm:
            1. Create a dummy node to simplify list construction.
            2. Compare the current nodes of both lists.
            3. Append the smaller node to the merged list and advance its pointer.
            4. Repeat until one list becomes empty.
            5. Attach the remaining nodes from the non-empty list.
            6. Return the node following the dummy node.

        Time:
            O(n + m)

        Space:
            O(1)

        Where n is the size of list1 and m is the size of list2.
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


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (head: Optional[ListNode], expected)
        (build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        (build_linked_list([]), build_linked_list([]), []),
        (build_linked_list([]), build_linked_list([67]), [67]),
        (build_linked_list([69]), build_linked_list([]), [69]),
    ]

    for list1, list2, expected in test_cases:
        result = solution.merge_two_sorted_lists_iterative(list1, list2)
        result = get_list_back(result)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"list1 = {get_list_back(list1)}\n"
            f"list2 = {get_list_back(list2)}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"list1 = {get_list_back(list1)}\n"
            f"list2 = {get_list_back(list2)}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")