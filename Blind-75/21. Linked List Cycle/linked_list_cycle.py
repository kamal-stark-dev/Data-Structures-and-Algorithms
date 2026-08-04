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


def build_linked_list_with_loop(nums: Optional[list[int]] = None, pos: int=-1) -> Optional[ListNode]:
    """
    Builds a singly linked list from a list of integers and optionally
    creates a cycle.

    Args:
        nums:
            List of node values.

        pos:
            Index of the node that the tail should point to.
            If -1, no cycle is created.

    Returns:
        The head of the constructed linked list.
    """

    if not nums:
        return None

    head = curr = ListNode(nums[0])
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next

    if pos == -1:
        return head

    tail = curr
    curr = head
    idx = 0
    while idx < pos:
        curr = curr.next
        idx += 1

    tail.next = curr
    return head


class Solution:
    """
    Problem:
        Given the head of a singly linked list, determine whether the
        linked list contains a cycle.

        A cycle exists if a node can be reached again by continuously
        following the next pointers. Internally, LeetCode represents the
        cycle using `pos`, the index of the node that the tail connects to.
        This value is only used when constructing test cases and is not
        passed to the function.

    Approaches:
        1. Hash Set
            Store every visited node in a set. If a node is encountered
            again, a cycle exists.

        2. Fast and Slow Pointers (Floyd's Cycle Detection)
            Move one pointer one step at a time and another two steps.
            If the pointers ever meet, the list contains a cycle.

    Constraints:
        - Number of nodes is in the range [0, 10^4].
        - -10^5 <= Node.val <= 10^5.
        - The cycle position (`pos`) is either -1 or a valid node index.

    Follow-up:
        Can the problem be solved using O(1) extra memory?
    """

    def linked_list_cycle_hash_set(self, head: Optional[ListNode]) -> bool:
        """
        Detects whether a linked list contains a cycle using a hash set.

        Intuition:
            Traverse the list while keeping track of every visited node.
            If a node is encountered more than once, the traversal has
            entered a cycle.

        Algorithm:
            1. Initialize an empty set to store visited nodes.
            2. Traverse the linked list.
            3. If the current node is already in the set, return True.
            4. Otherwise, add the node to the set and continue.
            5. If traversal reaches None, return False.

        Time:
            O(n)

        Space:
            O(n)
        """

        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False


    def linked_list_cycle_fast_and_slow_pointers(self, head: Optional[ListNode]) -> bool:
        """
        Detects whether a linked list contains a cycle using Floyd's
        Cycle Detection Algorithm.

        Intuition:
            If a cycle exists, a fast pointer moving two nodes at a time
            will eventually catch up to a slow pointer moving one node
            at a time. If no cycle exists, the fast pointer will reach
            the end of the list.

        Algorithm:
            1. Initialize both slow and fast pointers at the head.
            2. Move the slow pointer one step and the fast pointer
            two steps in each iteration.
            3. If the pointers meet, return True.
            4. If the fast pointer reaches the end of the list,
            return False.

        Time:
            O(n)

        Space:
            O(1)
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (head: Optional[ListNode], expected: bool)
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([67], -1, False),
    ]

    for nums, pos, expected in test_cases:
        head = build_linked_list_with_loop(nums, pos)

        result = solution.linked_list_cycle_fast_and_slow_pointers(head)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"head = {nums}\n"
            f"pos = {pos}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"head = {nums}\n"
            f"pos = {pos}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")