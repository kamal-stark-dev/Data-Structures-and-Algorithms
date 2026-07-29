class Solution:
    """
    Given an array of non-negative integers where each element represents the
    height of a vertical line, find the two lines that, together with the x-axis,
    form a container that holds the maximum amount of water.

    The container cannot be tilted.

    Constraints:
        n == height.length
        2 <= n <= 10^5
        0 <= height[i] <= 10^4
    """

    def container_with_most_water_brute_force(self, height: list[int]) -> int:
        """
        Finds the maximum amount of water that can be contained using
        the brute-force approach.

        This method checks every possible pair of vertical lines,
        computes the area formed by each pair, and returns the
        largest area found.

        Time: O(n^2)
        Space: O(1)
        """

        max_area = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                curr_area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, curr_area)

        return max_area


    def container_with_most_water_two_pointer(self, height: list[int]) -> int:
        """
        Finds the maximum amount of water that can be contained using
        the two-pointer technique.

        Two pointers start at the leftmost and rightmost lines.
        At each step, the area is calculated, and the pointer
        corresponding to the shorter line is moved inward, since
        moving the taller line cannot increase the area while the
        width decreases.

        Time: O(n)
        Space: O(1)
        """

        max_area = 0

        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            max_area = max(max_area, width * min_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1, 1], 1),
    ]

    for height, expected in test_cases:
        result = solution.container_with_most_water_two_pointer(height)

        assert result == expected

        print(
            f"height = {height}\n"
            f"got = {result}, expected = {expected}\n"
        )

    print("#######################\nAll test cases passed!!\n#######################")

