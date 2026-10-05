class Interval:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    """
    Problem:
        Given an array of meeting intervals, determine whether a person
        can attend all meetings without any time conflicts.

        Two meetings conflict if they overlap. However, meetings that
        touch at the same time are allowed, e.g. (0, 8) and (8, 10)
        do not conflict.

    Approach:
        1. Brute force: Compare every pair of meetings and check whether
           their time ranges overlap.
        2. Sorting: Sort meetings by their start time and only compare
           each meeting with the previous meeting.
        3. If any two consecutive meetings overlap, a conflict exists.

    Constraints:
        - 0 <= intervals.length <= 500
        - 0 <= intervals[i].start < intervals[i].end <= 1,000,000

    Notes:
        - Meetings ending exactly when another meeting starts are allowed.
        - Therefore, (0, 8) and (8, 10) are not considered overlapping.
    """

    def meeting_rooms_brute_force(self, intervals: list[Interval]):
        """
        Intuition:
            Check every pair of meetings. If any two meetings overlap,
            the person cannot attend both.

        Two intervals A and B overlap when:

            max(A.start, B.start) < min(A.end, B.end)

        If this condition is true, their common time range has a
        positive length, so there is a conflict.

        Algorithm:
            1. Iterate through every meeting A.
            2. Compare A with every meeting B that comes after it.
            3. Check whether A and B overlap.
            4. If any pair overlaps, return False.
            5. If no pair overlaps, return True.

        Time:
            O(n^2)

        Space:
            O(1)

        Note:
            We use a strict '<' comparison when checking overlap so that
            meetings such as (0, 8) and (8, 10) are allowed.
        """

        n = len(intervals)

        for i in range(n):
            A = intervals[i]

            for j in range(i + 1, n):
                B = intervals[j]

                if min(A.end, B.end) > max(A.start, B.start):
                    return False

        return True

    def meeting_rooms_sorting(self, intervals: list[Interval]):
        """
        Intuition:
            After sorting meetings by their start time, any meeting can
            only conflict with the meeting immediately before it.

            If the previous meeting ends after the current meeting starts,
            the two meetings overlap.

            If the previous meeting ends exactly when the current meeting
            starts, there is no conflict.

        Algorithm:
            1. Sort all meetings by their start time.
            2. Iterate through the sorted meetings.
            3. Compare each meeting with the previous meeting.
            4. If the previous meeting ends after the current meeting
               starts, return False.
            5. If no adjacent meetings overlap, return True.

        Time:
            O(n log n)

        Space:
            O(1) auxiliary space, excluding the sorting implementation.

        Note:
            The condition is:

                previous.end > current.start

            rather than >= because meetings such as (0, 8) and
            (8, 10) do not conflict.
        """

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (intervals: list[Interval], expected: bool)
        (
            [Interval(0, 30), Interval(5, 10), Interval(15, 20)],
            False
        ),
        (
            [Interval(5, 8), Interval(9, 15)],
            True
        ),
    ]

    for intervals, expected in test_cases:
        result = solution.meeting_rooms_sorting(intervals)

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