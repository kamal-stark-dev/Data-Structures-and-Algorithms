from collections import defaultdict

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

    def merge_intervals_sorting(self, intervals: list[list[int]]) -> list[list[int]]:
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
            -

        Algorithm:
            -

        Time:
            O()

        Space:
            O()
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