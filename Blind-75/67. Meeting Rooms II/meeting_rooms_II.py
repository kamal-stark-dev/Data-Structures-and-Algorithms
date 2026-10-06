import heapq
from collections import defaultdict

class Interval:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    """
    Problem:
        Given a list of meeting intervals, find the minimum number of
        meeting rooms required so that no two conflicting meetings use
        the same room.

        A meeting interval is represented as [start, end]. If one meeting
        ends at the exact time another meeting starts, they do not conflict.

    Approach:
        1. Sort meetings by their start time.
        2. Track the end time of meetings currently occupying rooms.
        3. Reuse a room whenever a meeting has ended before the next meeting starts.
        4. The maximum number of simultaneously active meetings is the
           minimum number of rooms required.

    Constraints:
        - 0 <= intervals.length <= 100,000
        - 0 <= intervals[i].start < intervals[i].end <= 1,000,000

    Notes:
        - Meetings ending at time t can be reused by meetings starting at t.
        - The three implementations below solve the same problem using:
          a min-heap, a line sweep, and two pointers.
    """

    def meeting_rooms_II_min_heap(self, intervals: list[Interval]) -> int:
        """
        Intuition:
            - Sort meetings by their start time.
            - Maintain a min-heap containing the end times of meetings
              currently occupying rooms.
            - The smallest end time tells us which room becomes available first.
            - If that room is free before or exactly when the current meeting
              starts, reuse it.
            - Otherwise, allocate a new room.

        Algorithm:
            - Sort intervals by start time.
            - For each meeting:
                1. If the earliest-ending meeting ends <= current start,
                   remove it from the heap because its room can be reused.
                2. Push the current meeting's end time into the heap.
            - The heap size represents the number of rooms currently required.
            - The maximum heap size is therefore the minimum number of rooms
              needed.

        Time:
            O(n log n)

        Space:
            O(n)

        Where n is the number of meetings.
        """

        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

    def meeting_rooms_II_line_sweep(self, intervals: list[Interval]) -> int:
        """
        Intuition:
            - Instead of processing complete intervals, process only their
                start and end events.
            - A meeting starting at time t requires one additional room.
            - A meeting ending at time t frees one room.
            - By processing these events in chronological order, we can find
                the maximum number of rooms being used at the same time.

        Algorithm:
            - Create a map where:
                start -> +1
                end   -> -1
            - For every interval:
                1. Add +1 at its start time.
                2. Add -1 at its end time.
            - Sort all event times.
            - Maintain a running count of currently occupied rooms.
            - The maximum value of this count is the minimum number of rooms
                required.

            Because the problem states that (0,8) and (8,10) do not conflict,
            an end event at time t is applied together with the start event
            at t through the net change stored in the map.

        Time:
            O(n log n)

        Space:
            O(n)

        Where n is the number of meetings.
        """

        mp = defaultdict(int)

        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1

        prev, res = 0, 0

        for num in sorted(mp):
            prev += mp[num]
            res = max(res, prev)

        return res

    def meeting_rooms_II_two_pointers(self, intervals: list[Interval]) -> int:
        """
        Intuition:
            - We only care about when meetings start and when meetings end.
            - Sort all start times and end times separately.
            - Use two pointers to determine whether the next event is a
                meeting starting or a meeting ending.
            - If a meeting starts before the earliest current ending meeting,
                another room is required.
            - Otherwise, a room has become available and can be reused.

        Algorithm:
            - Store all start times in one sorted array.
            - Store all end times in another sorted array.
            - Use two pointers:
                s -> next meeting start
                e -> earliest meeting end
            - While there are unprocessed starts:
                1. If starts[s] < ends[e]:
                    A new meeting starts before any room becomes available,
                    so increment the number of rooms in use.
                2. Otherwise:
                    A meeting has ended, so decrement the number of rooms
                    currently in use and move the end pointer.
            - Track the maximum number of rooms used at any point.

            The strict comparison starts[s] < ends[e] is important because
            a meeting ending at time t can share its room with a meeting
            starting at time t.

        Time:
            O(n log n)

        Space:
            O(n)

        Where n is the number of meetings.
        """

        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            res = max(res, count)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (list[Interval], expected: int)
        (
            [Interval(0, 40), Interval(5, 10), Interval(15, 20)],
            2
        ),
        (
            [Interval(4, 9)],
            1
        ),
    ]

    for intervals, expected in test_cases:
        result = solution.meeting_rooms_II_two_pointers(intervals)

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