from typing import Optional
import heapq
class ListNode:
    """
    Represents a node in a singly linked list.

    Attributes:
        val: Integer value stored in the node.
        next: Reference to the next node in the list, or None if this is
            the last node.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(nums: Optional[list[int]] = None) -> Optional[ListNode]:
    """
    Builds a singly linked list from a list of integers.

    Args:
        nums: List of integer values to store in the linked list. If None,
            an empty list is returned.

    Returns:
        The head of the constructed linked list, or None if nums is None.
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
    Converts a singly linked list into a Python list.

    Args:
        head: Head node of the linked list.

    Returns:
        A list containing the values of the linked list in order.
    """
    curr = head
    nums = []
    while curr:
        nums.append(curr.val)
        curr = curr.next
    return nums


class NodeWrapper:
    """
    Wraps a linked-list node so it can be stored in a min-heap.

    The heap compares wrappers using the value of their underlying
    linked-list nodes.
    """

    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    """
    Provides multiple approaches for merging k sorted linked lists.

    Each input linked list is assumed to be sorted in non-decreasing order.
    The methods return a single sorted linked list containing all nodes
    from the input lists.

    Approaches:
        - Brute force: Collect all values, sort them, and build a new list.
        - Iteration: Repeatedly scan all k lists for the smallest node.
        - Merge one by one: Sequentially merge each list into the result.
        - Min-heap: Maintain the smallest current node from each list.
        - Divide and conquer (recursive): Pairwise merge lists recursively.
        - Divide and conquer (iterative): Pairwise merge lists level by level.
    """

    def merge_lists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted linked list.

        The existing nodes are reused rather than creating new nodes.

        Args:
            list1: Head of the first sorted linked list.
            list2: Head of the second sorted linked list.

        Returns:
            The head of the merged sorted linked list.
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


    def merge_k_sorted_lists_brute_force(
        self,
        lists: list[Optional[ListNode]],
    ) -> Optional[ListNode]:
        """
        Merges k sorted linked lists using a brute-force approach.

        Intuition:
            Collect every node value from all input lists, sort the values,
            and construct a new linked list from the sorted values.

        Algorithm:
            1. Traverse every linked list and collect all node values.
            2. Sort all collected values.
            3. Create a new linked list using the sorted values.

        Args:
            lists: A list of heads of sorted linked lists.

        Returns:
            The head of a new sorted linked list containing all values.

        Complexity:
            Let n be the total number of nodes across all lists.
            Time: O(n logn)
            Space: O(n)
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


    def merge_k_sorted_lists_iteration(
        self,
        lists: list[Optional[ListNode]],
    ) -> Optional[ListNode]:
        """
        Merges k sorted linked lists by repeatedly scanning all lists.

        Intuition:
            At every step, the smallest possible next node must be the
            smallest current node among the k list heads.

        Algorithm:
            1. Scan all non-empty lists to find the smallest current node.
            2. Append that node to the result.
            3. Advance the corresponding list.
            4. Repeat until all lists are exhausted.

        Args:
            lists: A list of heads of sorted linked lists.

        Returns:
            The head of the merged sorted linked list.

        Complexity:
            Let n be the total number of nodes and k the number of lists.
            Time: O(n * k)
            Space: O(1), excluding the output list.
        """

        dummy = curr = ListNode()

        while True:
            minIdx = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minIdx == -1 or lists[i].val < lists[minIdx].val:
                    minIdx = i

            if minIdx == -1:
                break
            curr.next = lists[minIdx]
            lists[minIdx] = lists[minIdx].next
            curr = curr.next

        return dummy.next


    def merge_k_sorted_lists_merge_one_by_one(
        self,
        lists: list[Optional[ListNode]],
    ) -> Optional[ListNode]:
        """
        Merges k sorted linked lists sequentially.

        Intuition:
            Start with an empty result and merge each input list into the
            result one at a time.

        Algorithm:
            1. Initialize the merged result as an empty list.
            2. Merge the current result with the next input list.
            3. Continue until every list has been merged.

        Args:
            lists: A list of heads of sorted linked lists.

        Returns:
            The head of the merged sorted linked list.

        Complexity:
            Let n be the total number of nodes and k the number of lists.
            In the worst case, earlier nodes are repeatedly traversed.
            Time: O(n * k)
            Space: O(1), excluding the output list.
        """

        merged = None
        for i in range(len(lists)):
            merged = self.merge_lists(merged, lists[i])

        return merged


    def merge_k_sorted_lists_min_heap(
        self,
        lists: list[Optional[ListNode]],
    ) -> Optional[ListNode]:
        """
        Merges k sorted linked lists using a min-heap.

        Intuition:
            The smallest next node must be one of the current heads of
            the non-empty lists. A min-heap efficiently tracks these nodes.

        Algorithm:
            1. Add the head node of every non-empty list to the min-heap.
            2. Remove the smallest node from the heap.
            3. Append it to the result.
            4. If the removed node has a next node, add that node to the heap.
            5. Repeat until the heap is empty.

        Args:
            lists: A list of heads of sorted linked lists.

        Returns:
            The head of the merged sorted linked list.

        Complexity:
            Let n be the total number of nodes and k the number of lists.
            Each node is pushed to and popped from the heap once.
            Time: O(n logk)
            Space: O(k) for the heap, excluding the output list.
        """

        # Push the head of each non-empty list into the heap.
        minheap = []
        for head in lists:
            if head:
                heapq.heappush(minheap, NodeWrapper(head))

        dummy = curr = ListNode()

        while minheap:
            node = heapq.heappop(minheap).node

            if node.next:
                heapq.heappush(minheap, NodeWrapper(node.next))

            curr.next = node
            curr = curr.next

        return dummy.next


    def merge_k_sorted_lists_divide_and_conquer_recursive(
        self,
        lists: list[Optional[ListNode]],
    ) -> Optional[ListNode]:
        """
        Merges k sorted linked lists using recursive divide and conquer.

        Intuition:
            Instead of merging all lists at once, recursively divide the
            input into smaller groups until each group contains one list.
            Then merge pairs of lists while returning up the recursion tree.

        Algorithm:
            1. Divide the list range into two halves.
            2. Recursively merge each half.
            3. Merge the two resulting sorted lists.
            4. Continue until the entire range has been merged.

        Args:
            lists: A list of heads of sorted linked lists.

        Returns:
            The head of the merged sorted linked list, or None if lists
            is empty.

        Complexity:
            Let n be the total number of nodes and k the number of lists.
            Each level processes all n nodes, with O(log k) levels.
            Time: O(n logk)
            Space: O(logk) for the recursion stack.
        """

        def divide(lists, left, right):
            if left > right:
                return None

            if left == right:
                return lists[left]

            mid = (left + right) // 2

            left = divide(lists, left, mid)
            right = divide(lists, mid + 1, right)

            return conquer(left, right)

        def conquer(list1, list2):
            return self.merge_lists(list1, list2)

        if not lists:
            return None

        return divide(lists, 0, len(lists) - 1)


    def merge_k_sorted_lists_divide_and_conquer_iterative(
        self,
        lists: list[Optional[ListNode]],
    ) -> Optional[ListNode]:
        """
        Merges k sorted linked lists using iterative divide and conquer.

        Intuition:
            Merge lists in pairs during each round. After every round,
            the number of lists is approximately halved.

        Algorithm:
            1. Pair adjacent lists.
            2. Merge each pair using merge_lists().
            3. Store the merged lists in a new collection.
            4. Repeat until only one merged list remains.

        Args:
            lists: A list of heads of sorted linked lists.

        Returns:
            The head of the merged sorted linked list, or None if lists
            is empty.

        Complexity:
            Let n be the total number of nodes and k the number of lists.
            Each round processes all n nodes, and there are O(log k) rounds.
            Time: O(n logk)
            Space: O(k) for the intermediate list references.
        """

        if not lists:
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

        result = solution.merge_k_sorted_lists_divide_and_conquer_iterative(list_heads)
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