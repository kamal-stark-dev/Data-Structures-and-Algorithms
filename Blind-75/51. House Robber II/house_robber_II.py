class Solution:
    """
    Problem:
        - Given an array of integers where each element represents the money
          stored in a house, return the maximum amount of money that can be
          robbed without robbing two adjacent houses.
        - The houses are arranged in a circle, meaning the first and last
          houses are also adjacent.
        - Robbing two adjacent houses triggers the security system.

    Approach:
        1. Because the houses form a circle, the first and last houses
           cannot both be robbed.
        2. Therefore, split the problem into two linear House Robber problems:
               - Exclude the last house: nums[0 ... n - 2]
               - Exclude the first house: nums[1 ... n - 1]
        3. Find the maximum amount for both cases and take the larger result.

    Constraints:
        - 1 <= nums.length <= 100
        - 0 <= nums[i] <= 1000

    Notes:
        - For a single house, simply return nums[0].
        - Each solution below uses the same recurrence but stores or
          processes the subproblem results differently.
    """

    def house_robber_II_recursion(self, nums: list[int]) -> int:
        """
        Intuition:
            - Since the houses are arranged in a circle, the first and last
              houses cannot both be robbed.
            - Consider two independent cases:
                1. Exclude the last house.
                2. Exclude the first house.
            - Each case becomes the standard linear House Robber problem.
            - For every house, we have two choices:
                - Skip the current house.
                - Rob the current house and skip the next house.

        Algorithm:
            - Define dfs(i, end) as the maximum money that can be robbed
              from house i through house end.
            - For each house:
                - Skip it: dfs(i + 1, end)
                - Rob it: nums[i] + dfs(i + 2, end)
            - Take the maximum of these two choices.
            - Solve both circular cases:
                - dfs(0, n - 2): exclude the last house.
                - dfs(1, n - 1): exclude the first house.
            - Return the larger result.

        Time:
            O(2^n)

        Space:
            O(n)
            - O(n) recursion stack in the worst case.
        """

        def dfs(i: int, end: int) -> int:
            if i > end:
                return 0

            return max(
                dfs(i + 1, end),             # skip
                nums[i] + dfs(i + 2, end)    # rob
            )

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(
            dfs(0, n - 2),  # exclude last
            dfs(1, n - 1)   # exclude first
        )

    def house_robber_II_memoization(self, nums: list[int]) -> int:
        """
        Intuition:
            - The recursive solution repeatedly calculates the same
              subproblems.
            - Cache the result for every house so that each subproblem
              is solved only once.
            - As in the recursive solution, split the circular problem
              into two linear ranges.

        Algorithm:
            - Define rob_range(start, end) to solve the linear House
              Robber problem between start and end.
            - Use dfs(i) to represent the maximum money that can be robbed
              from house i through end.
            - Before calculating dfs(i), check whether its result is already
              present in the memoization dictionary.
            - Store:
                  memo[i] = max(
                      dfs(i + 1),
                      nums[i] + dfs(i + 2)
                  )
            - Solve both cases:
                - rob_range(0, n - 2): exclude the last house.
                - rob_range(1, n - 1): exclude the first house.
            - Return the maximum of the two results.

        Time:
            O(n)
            - There are O(n) unique states and each state is computed once.

        Space:
            O(n)
            - O(n) for the memoization dictionary.
            - O(n) recursion stack in the worst case.
        """

        def rob_range(start: int, end: int) -> int:
            memo = {}

            def dfs(i: int) -> int:
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                memo[i] = max(
                    dfs(i + 1),
                    nums[i] + dfs(i + 2)
                )

                return memo[i]

            return dfs(start)

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(
            rob_range(0, n - 2),
            rob_range(1, n - 1)
        )

    def house_robber_II_tabulation(self, nums: list[int]) -> int:
        """
        Intuition:
            - The memoization solution solves each state once, but still
              uses recursion.
            - We can build the solutions from smaller subproblems to larger
              subproblems using bottom-up dynamic programming.
            - After splitting the circular problem into two linear ranges,
              each range follows the standard House Robber recurrence.

        Algorithm:
            - Define dp[i] as the maximum money that can be robbed from
              houses 0 through i.
            - For every house i, there are two choices:
                - Skip house i: dp[i - 1]
                - Rob house i: nums[i] + dp[i - 2]
            - Therefore:
                  dp[i] = max(dp[i - 1],
                              nums[i] + dp[i - 2])
            - Solve two cases:
                - nums[:-1]: exclude the last house.
                - nums[1:]: exclude the first house.
            - Return the maximum result from the two cases.

        Time:
            O(n)
            - Each house is processed a constant number of times.

        Space:
            O(n)
            - The dp array stores the result for every house.
        """

        def rob_range(houses: list[int]) -> int:
            n = len(houses)

            if n == 1:
                return houses[0]

            dp = [0] * n

            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(
                    dp[i - 1],
                    houses[i] + dp[i - 2]
                )

            return dp[-1]

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(
            rob_range(nums[:-1]),  # exclude last
            rob_range(nums[1:])    # exclude first
        )

    def house_robber_II_optimal(self, nums: list[int]) -> int:
        """
        Intuition:
            - The tabulation solution only needs the previous two DP values
              to calculate the current value.
            - There is no need to store the entire dp array.
            - Maintain two variables:
                - prev: maximum money from two houses before the current one.
                - curr: maximum money from the previous house.
            - This reduces the DP space from O(n) to O(1).

        Algorithm:
            - Define rob_range(houses) to solve the linear House Robber
              problem using constant extra space.
            - For every house:
                - Skip it: keep curr.
                - Rob it: prev + house.
            - Update:
                  prev, curr = curr, max(curr, prev + house)
            - Since the houses form a circle, solve two cases:
                - nums[:-1]: exclude the last house.
                - nums[1:]: exclude the first house.
            - Return the maximum result from the two cases.

        Time:
            O(n)
            - Each house is processed once.

        Space:
            O(1)
            - Only two variables are used for the DP state.
            - Note: Python slicing with nums[:-1] and nums[1:] creates
              new lists, which technically requires O(n) temporary memory.
        """

        def rob_range(houses: list[int]) -> int:
            prev, curr = 0, 0

            for house in houses:
                prev, curr = curr, max(curr, prev + house)

            return curr

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(
            rob_range(nums[:-1]),
            rob_range(nums[1:])
        )


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], expected: int)
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
        ([4], 4),
    ]

    for nums, expected in test_cases:
        result = solution.house_robber_II_optimal(nums)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")