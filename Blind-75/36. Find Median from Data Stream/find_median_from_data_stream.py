import heapq

class MedianFinder:
    """
    Maintain the median of a stream of integers using two heaps.

    The numbers are divided into two halves:
        - smallHeap: a max heap containing the smaller half of the numbers.
          Python only provides a min heap, so values are stored as negatives.
        - largeHeap: a min heap containing the larger half of the numbers.

    The heaps are kept balanced so that their sizes differ by at most one.
    Therefore:
        - If both heaps have the same size, the median is the average of
          their two top elements.
        - If one heap has one extra element, its top element is the median.

    This allows numbers to be added in O(log n) time and the median to be
    retrieved in O(1) time.

    Problem:
        Implement a data structure that supports adding integers from a
        data stream and finding the median of all numbers seen so far.

    Approach:
        1. Add every number to smallHeap, treating it as a max heap by
           storing its negative.
        2. If the largest value in the smaller half is greater than the
           smallest value in the larger half, move that value from
           smallHeap to largeHeap to restore ordering.
        3. Rebalance the heaps whenever their sizes differ by more than one.

    Constraints:
        - -10^5 <= num <= 10^5
        - There is at least one element before findMedian is called.
        - At most 5 * 10^4 calls are made to addNum and findMedian.

    Notes:
        - smallHeap contains the smaller half of the values.
        - largeHeap contains the larger half of the values.
        - The top of smallHeap is the largest value in the smaller half.
        - The top of largeHeap is the smallest value in the larger half.
        - Python's heapq is a min-heap, so smallHeap stores negative values.
    """

    def __init__(self):
        """
        Initialize two empty heaps used to maintain the data stream.

        smallHeap is implemented as a max heap using negative values,
        while largeHeap is a normal min heap.

        Time:
            O(1)

        Space:
            O(1)
        """
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        """
        Add an integer to the data stream while maintaining both heaps.

        Intuition:
            - Keep the smaller half of the numbers in smallHeap and the
              larger half in largeHeap.
            - Since Python only provides a min heap, store negative values
              in smallHeap to simulate a max heap.
            - After inserting a number, restore the ordering between the
              two heaps and then rebalance their sizes.

        Algorithm:
            1. Push the new number into smallHeap as a negative value.
            2. If the largest value in smallHeap is greater than the smallest
               value in largeHeap, move that value to largeHeap.
            3. If smallHeap has more than one extra element, move its maximum
               value to largeHeap.
            4. If largeHeap has more than one extra element, move its minimum
               value to smallHeap.

        Time:
            O(log n), where n is the number of elements currently stored.

        Space:
            O(n), where n is the number of elements currently stored.
        """
        heapq.heappush(self.smallHeap, -num)

        if self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            val = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        elif len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -val)

    def findMedian(self) -> float:
        """
        Return the median of all numbers currently in the data stream.

        Intuition:
            - The two heaps represent the lower and upper halves of the
              sorted data.
            - If both halves have the same number of elements, the median
              is the average of their boundary values.
            - If one heap has one extra element, its top value is the median.

        Algorithm:
            1. Compare the sizes of the two heaps.
            2. If their sizes are equal, average the maximum value from
               smallHeap and the minimum value from largeHeap.
            3. Otherwise, return the top value from the larger heap.

        Time:
            O(1)

        Space:
            O(1) auxiliary space.
        """
        n1, n2 = len(self.smallHeap), len(self.largeHeap)

        if n1 == n2:
            return (-self.smallHeap[0] + self.largeHeap[0]) / 2

        if n1 > n2:
            return -self.smallHeap[0]

        return self.largeHeap[0]


class Solution:
    def find_median_from_data_stream(self, calls: list[str], inputs: list[list[int]]) -> list[float | None]:
        """
        Simulate the MedianFinder API using a sequence of operations.

        Each entry in calls represents an operation:
            - "MedianFinder": initialize the data structure.
            - "addNum": add the corresponding integer from inputs.
            - "findMedian": return the current median.

        The inputs list contains the arguments for each operation. For
        "addNum", the corresponding entry contains one integer, while
        constructor and "findMedian" calls contain an empty list.

        Args:
            calls:
                A list of operation names to execute.
            inputs:
                A list of argument lists corresponding to each operation.

        Returns:
            A list containing None for constructor/addNum operations and
            the median value for each findMedian operation.

        Time:
            O(m log n), where m is the number of operations and n is the
            maximum number of elements stored in MedianFinder.

        Space:
            O(n), for the two heaps storing the data stream.
        """
        medianFinder = MedianFinder()
        outputs: list[float | None] = []

        for call, input in zip(calls, inputs):
            if call == "MedianFinder":
                outputs.append(None)

            if call == "addNum":
                medianFinder.addNum(input[0])
                outputs.append(None)

            elif call == "findMedian":
                median = medianFinder.findMedian()
                outputs.append(median)

        return outputs


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (calls: list[str], inputs: list[list[int]], expected: list[float | None])
        (["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], [[], [1], [2], [], [3], []], [None, None, None, 1.5, None, 2.0]),
    ]

    for calls, inputs, expected in test_cases:
        result = solution.find_median_from_data_stream(calls, inputs)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"calls = {calls}\n"
            f"inputs = {inputs}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"calls = {calls}\n"
            f"inputs = {inputs}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")