class Solution:
    """
    Problem:
        Given a list of non-overlapping intervals sorted by start
        time and a new interval, insert the new interval while
        merging all overlapping intervals.

    Approach:
        1. Linear Approach:
           - Traverse intervals and append those before newInterval.
           - Merge all overlapping intervals with newInterval.
           - Append the merged interval and all remaining intervals.

        2. Binary Search Approach:
           - Use binary search to find the insertion position.
           - Insert newInterval into the sorted list.
           - Traverse the list and merge overlapping intervals.

    Constraints:
        - 0 <= intervals.length <= 10^4
        - intervals[i].length == 2
        - 0 <= starti <= endi <= 10^5
        - Intervals are sorted by start time and non-overlapping.
        - 0 <= start <= end <= 10^5

    Notes:
        - Intervals that share an endpoint are considered overlapping.
        - Both approaches have O(n) time complexity.
        - The linear approach does not modify the input list,
          but may modify newInterval.
        - The binary search approach modifies the input list.
    """

    def insert_interval_linear(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        Intuition:
            Since intervals are sorted and non-overlapping, we can
            process them in a single pass, separating intervals
            before, overlapping with, and after newInterval.

        Algorithm:
            1. Append all intervals that end before newInterval starts.
            2. Merge all intervals that overlap with newInterval.
            3. Append the merged newInterval to the result.
            4. Append all remaining intervals.
            5. Return the resulting list.

        Time:
            O(n) - Each interval is visited at most once.

        Space:
            O(n) - A separate result list is created.
        """

        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Merge all overlapping intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res

    def insert_interval_lower_bound(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        Intuition:
            Since intervals are sorted by start time, binary search
            can find the correct insertion position of newInterval.
            A single traversal can then merge all overlapping intervals.

        Algorithm:
            1. Use binary search to find the lower bound of
               newInterval's start time.
            2. Insert newInterval at the identified position.
            3. Traverse the updated list.
            4. Append an interval if it does not overlap with
               the last interval in the result.
            5. Otherwise, merge it with the last interval.
            6. Return the merged result.

        Time:
            O(n) - Binary search takes O(log n), list insertion
            takes O(n), and merging takes O(n).

        Space:
            O(n) - A separate result list is created.
        """

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        # Lower bound: find insertion position
        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)

        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            [[1, 3], [6, 9]],
            [2, 5],
            [[1, 5], [6, 9]]
        ),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]]
        ),
        (
            [],
            [5, 7],
            [[5, 7]]
        ),
        (
            [[1, 5]],
            [2, 3],
            [[1, 5]]
        ),
    ]

    for intervals, newInterval, expected in test_cases:
        result = solution.insert_interval_lower_bound(intervals, newInterval)

        assert result == expected, (
            f"\nTest case failed!\n"
            f"intervals = {intervals}\n"
            f"newInterval = {newInterval}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(f"intervals = {intervals}")
        print(f"newInterval = {newInterval}")
        print(f"expected = {expected}")
        print(f"got = {result}\n")

    print("#######################")
    print("All test cases passed!!")
    print("#######################")