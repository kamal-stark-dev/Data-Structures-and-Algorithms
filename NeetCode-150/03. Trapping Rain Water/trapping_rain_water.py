class Solution:
    """
    Problem:
        Given n non-negative integers representing an elevation map where
        the width of each bar is 1, compute how much water can be trapped
        between the bars after raining.

    Approach:
        1. Brute Force:
            For each bar, find the maximum height to its left and right.
            The trapped water is the minimum of these two maximum heights
            minus the current bar's height.

        2. Prefix and Suffix Maximums:
            Precompute the maximum height to the left and right of every
            bar using prefix and suffix arrays. Use these arrays to
            calculate the trapped water at each position.

        3. Two Pointers:
            Use left and right pointers with leftMax and rightMax to
            calculate trapped water in a single traversal without
            allocating additional arrays.

    Constraints:
        - 1 <= n <= 2 * 10^4
        - 0 <= heights[i] <= 10^5
        - n == len(heights)
        - Each bar has a width of 1.

    Notes:
        - Water trapped at index i is determined by the tallest bars
          to its left and right.
        - Water at index i = min(leftMax, rightMax) - heights[i].
        - The total trapped water is the sum of the water trapped
          at every index.
        - The brute-force approach repeatedly calculates maximums.
        - The prefix/suffix approach trades O(n) extra space for
          linear time complexity.
        - The two-pointer approach achieves O(n) time and O(1)
          auxiliary space.
    """

    def trapping_rain_water_brute_force(self, heights: list[int]) -> int:
        """
        Intuition:
            The amount of water trapped above a bar depends on the
            tallest bar to its left and the tallest bar to its right.

            The shorter of these two boundaries determines the maximum
            water level. Subtracting the current bar's height gives
            the water trapped at that position.

        Algorithm:
            1. Iterate through every index i in the elevation map.
            2. Find leftMax by scanning all bars to the left of i,
               including the current bar.
            3. Find rightMax by scanning all bars to the right of i,
               including the current bar.
            4. Calculate the water trapped at i:
                   min(leftMax, rightMax) - heights[i]
            5. Add the result to trappedWater.
            6. Return the total trapped water.

        Time:
            O(n^2) - For each of the n bars, scan the bars to its
            left and right, requiring O(n) work per bar.

        Space:
            O(1) - Only a constant number of variables are used.
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
            Instead of repeatedly scanning the bars to find the maximum
            heights on both sides, precompute these values.

            prefix[i] stores the tallest bar from index 0 through i.
            suffix[i] stores the tallest bar from index i through n - 1.

            These values allow the trapped water at each index to be
            calculated in O(1) time.

        Algorithm:
            1. Create prefix and suffix arrays of length n.
            2. Build prefix from left to right:
                   prefix[i] = max(heights[i], prefix[i - 1])
            3. Build suffix from right to left:
                   suffix[i] = max(heights[i], suffix[i + 1])
            4. For every index i, calculate:
                   min(prefix[i], suffix[i]) - heights[i]
            5. Add the water trapped at each index to trappedWater.
            6. Return the total trapped water.

        Time:
            O(n) - Building both arrays and calculating the total
            each require a single linear traversal.

        Space:
            O(n) - The prefix and suffix arrays each store n elements.
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
            The water trapped at any index depends on the smaller of
            the maximum heights on its left and right.

            Use two pointers, left and right, to process the elevation
            map from both ends. Maintain leftMax and rightMax to track
            the tallest bars encountered from each direction.

            If leftMax < rightMax, the left side determines the water
            level at the current left position. The right side has a
            sufficiently tall boundary, so the trapped water can be
            calculated without knowing the exact maximum to the right.

            Otherwise, process the right position symmetrically.

            This eliminates the need for prefix and suffix arrays.

        Algorithm:
            1. Initialize left = 0 and right = n - 1.
            2. Initialize leftMax and rightMax using the heights
               at the two endpoints.
            3. While left < right:
                a. If leftMax < rightMax:
                    - Move left one position to the right.
                    - Update leftMax.
                    - Add leftMax - heights[left] to trappedWater.
                b. Otherwise:
                    - Move right one position to the left.
                    - Update rightMax.
                    - Add rightMax - heights[right] to trappedWater.
            4. Return trappedWater.

        Time:
            O(n) - Each pointer moves inward at most n - 1 times,
            so every position is processed at most once.

        Space:
            O(1) - Only pointers, maximum heights, and the running
            total are maintained.
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