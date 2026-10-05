class Solution:
    """
    Problem:

        Given a list of intervals, remove the minimum number of intervals
        such that the remaining intervals do not overlap.

        Two intervals are considered non-overlapping if the end of one
        interval is equal to the start of another.

    Approach:

        1. Sort the intervals based on their start time.
        2. Greedily keep track of the interval with the smallest end time
           among overlapping intervals.
        3. When two intervals overlap, remove the interval that ends later,
           as keeping the interval with the smaller end gives us more room
           for future intervals.

    Constraints:

        - 1 <= intervals.length <= 100,000
        - intervals[i].length == 2
        - -50,000 <= start_i < end_i <= 50,000

    Notes:

        - Intervals that only touch at a common point are considered
          non-overlapping.
        - When intervals overlap, keeping the interval with the smaller
          end time is always the better greedy choice.
        - The problem can also be viewed as maximizing the number of
          non-overlapping intervals and subtracting that count from the
          total number of intervals.
    """

    def non_overlapping_intervals_greedy_sort_by_start(self, intervals: list[list[int]]) -> int:
        """
        Intuition:

            Sort intervals by their start time. When the current interval
            overlaps with the previously selected interval, one of them
            must be removed.

            To leave as much space as possible for future intervals, we
            should keep the interval that ends earlier. Therefore, when
            two intervals overlap, we keep the smaller end time and remove
            the other interval.

        Algorithm:

            1. Sort the intervals by their start time.
            2. Initialize prevEnd as negative infinity.
            3. For every interval:
                - If its start is before prevEnd, it overlaps with the
                  previously kept interval.
                - Increment the removal count.
                - Keep the interval with the smaller end time.
                - Otherwise, keep the current interval.
            4. Return the total number of removed intervals.

        Time:

            O(n log n)

        Space:

            O(1) auxiliary space
            (ignoring the space used internally by sorting)
        """

        intervals.sort()

        ans = 0
        prevEnd = float("-inf")

        for start, end in intervals:
            if prevEnd > start:
                ans += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return ans

    def non_overlapping_intervals_greedy_sort_by_end(self, intervals: list[list[int]]) -> int:
        """
        Intuition:

            Instead of deciding which interval to remove, we can think of
            maximizing the number of intervals we keep.

            If intervals are sorted by their end time, we can always keep
            the earliest-ending interval whenever possible. An interval
            that ends earlier leaves more room for all subsequent intervals.

            Every overlapping interval is therefore removed.

        Algorithm:

            1. Sort the intervals by their end time.
            2. Initialize prevEnd as negative infinity.
            3. For every interval:
                - If its start is before prevEnd, it overlaps with the
                  previously selected interval, so remove it.
                - Otherwise, keep it and update prevEnd to its end.
            4. Return the number of removed intervals.

        Time:

            O(n log n)

        Space:

            O(1) auxiliary space
            (ignoring the space used internally by sorting)
        """

        intervals.sort(key=lambda x: x[1])

        ans = 0
        prevEnd = float("-inf")

        for start, end in intervals:
            if prevEnd > start:
                ans += 1
            else:
                prevEnd = end

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (intervals: list[list[int]], expected: int)
        (
            [[1, 2], [2, 4], [1, 4]],
            1
        ),
        (
            [[1, 2], [2, 4]],
            0
        ),
        (
            [[1, 2], [1, 2], [1, 2]],
            2
        )
    ]

    for intervals, expected in test_cases:
        result = solution.non_overlapping_intervals_greedy_sort_by_end(intervals)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"intervals = {intervals}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"intervals = {intervals}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")