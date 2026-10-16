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

    def trapping_rain_water_brute_force(self, heights: list[int]) -> int:
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

        n = len(heights)
        trappedWater = 0

        for i in range(n):
            leftMax = rightMax = heights[i]

            for j in range(i):
                leftMax = max(leftMax, heights[j])

            for j in range(i + 1, n):
                rightMax = max(rightMax, heights[j])

            trappedWater += min(leftMax, rightMax) - heights[i]

        return trappedWater

    def trapping_rain_water_prefix_suffix(self, heights: list[int]) -> int:
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

        n = len(heights)

        prefix = [-1] * n
        suffix = [-1] * n

        prefix[0] = heights[0]

        for i in range(1, n):
            prefix[i] = max(heights[i], prefix[i - 1])

        suffix[n - 1] = heights[n - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = max(heights[i], suffix[i + 1])

        trappedWater = 0

        for i in range(n):
            trappedWater += min(prefix[i], suffix[i]) - heights[i]

        return trappedWater

    def trapping_rain_water_two_pointers(self, heights: list[int]) -> int:
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

        left, right = 0, len(heights) - 1
        leftMax, rightMax = heights[left], heights[right]

        trappedWater = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, heights[left])
                trappedWater += leftMax - heights[left]

            else:
                right -= 1
                rightMax = max(rightMax, heights[right])
                trappedWater += rightMax - heights[right]

        return trappedWater


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (heights: list[int], expected: int)
        (
            [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
            6
        ),
        (
            [4, 2, 0, 3, 2, 5],
            9
        ),
    ]

    for heights, expected in test_cases:
        result = solution.trapping_rain_water_two_pointers(heights)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"heights = {heights}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"heights = {heights}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")