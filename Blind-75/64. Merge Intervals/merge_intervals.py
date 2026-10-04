from collections import defaultdict

class Solution:
    """
    Problem:
    Given an array of intervals, merge all overlapping intervals
    and return an array of non-overlapping intervals that cover
    all the intervals in the input.

    Approach:
        1. Sorting:
        - Sort intervals by their starting points.
        - Iterate through the sorted intervals and compare each
            interval with the last interval in the result.
        - If they overlap, merge them by updating the ending point.
        - Otherwise, append the current interval to the result.

        2. Line Sweep:
        - Use a hashmap to track the number of intervals starting
            and ending at each point.
        - Increment the count at each starting point and decrement
            it at each ending point.
        - Traverse the sorted points while maintaining an active
            interval count.
        - Start a new merged interval when the count changes from
            zero to positive, and close it when the count returns to
            zero.

        3. Return the merged, non-overlapping intervals.

    Constraints:
        - 1 <= intervals.length <= 10^4
        - intervals[i].length == 2
        - 0 <= starti <= endi <= 10^4

    Notes:
        - Intervals that share an endpoint are considered overlapping.
        - Sorting is the simpler and more efficient approach for
        general use.
        - The line sweep approach processes interval boundaries
        using a difference map.
        - The sorting approach modifies the input list in place.
        - Both approaches return intervals in ascending order.
    """

    def merge_intervals_sorting(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Intuition:
            Sorting intervals by their starting points ensures that
            any interval overlapping with the current interval will
            appear next to it or later in the sorted list.

            By comparing each interval with the last merged interval,
            we can either extend the existing interval or add a new
            non-overlapping interval.

        Algorithm:
            1. Sort intervals by their starting points.
            2. Initialize the result with the first interval.
            3. Iterate through the remaining intervals:
            - If the current interval starts before or at the
                end of the last merged interval, they overlap.
                Extend the last merged interval's end to the
                maximum of both ending points.
            - Otherwise, append the current interval as a
                new non-overlapping interval.
            4. Return the result.

        Time:
            O(n log n)
            Sorting takes O(n log n), and traversing the intervals
            takes O(n).

        Space:
            O(n)
            The result stores up to n intervals. Sorting is in-place,
            requiring O(log n) auxiliary space on average for the
            sorting implementation.
        """

        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res

    def merge_intervals_line_sweep(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Intuition:
            Every interval contributes an opening event at its
            starting point and a closing event at its ending point.

            By tracking the number of active intervals at each
            boundary, we can determine when a merged interval
            begins and ends.

            When the active count becomes positive, a merged
            interval is active. When it returns to zero, the
            current merged interval is complete.

        Algorithm:
            1. Create a hashmap to record boundary events:
            - Increment the count at each interval's start.
            - Decrement the count at each interval's end.
            2. Sort all unique boundary points.
            3. Traverse the sorted points while maintaining
            the number of active intervals:
            - If no merged interval is currently open,
                start one at the current point.
            - Update the active count using the events
                at the current point.
            - When the active count reaches zero, close
                the merged interval at the current point
                and append it to the result.
            4. Return the merged intervals.

        Time:
            O(n log n)
            Building the hashmap takes O(n), sorting the
            unique boundary points takes O(n log n), and
            traversing them takes O(n).

        Space:
            O(n)
            The hashmap, sorted boundary points, and result
            require O(n) space, where n is the number of
            input intervals.
        """

        mp = defaultdict(int)

        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1

        interval = []
        res = []
        have = 0

        for i in sorted(mp):
            if not interval:
                interval.append(i)

            have += mp[i]

            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (intervals: list[list[int]], expected: list[list[int]])
        (
            [[1,3],[2,6],[8,10],[15,18]],
            [[1,6],[8,10],[15,18]]
        ),
        (
            [[1,4],[4,5]],
            [[1,5]]
        ),
        (
            [[4,7],[1,4]],
            [[1,7]]
        ),
    ]

    for intervals, expected in test_cases:
        result = solution.merge_intervals_line_sweep(intervals)

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