class Solution:
    """
    Problem:
    Given an integer array `nums`, where each element
    represents the maximum jump length from that index,
    determine whether it is possible to reach the last
    index starting from the first index.

    Approach:
        1. Recursion: Explore every possible jump from the
        current index using DFS.
        2. Memoization: Cache the results of previously
        visited indices to avoid redundant computations.
        3. Tabulation: Use bottom-up dynamic programming to
        determine whether each index can reach the end.
        4. Greedy: Traverse backward, maintaining the leftmost
        index from which the last index is reachable.

    Constraints:
        - 1 <= nums.length <= 10^4
        - 0 <= nums[i] <= 10^5

    Notes:
        - Initially positioned at index 0.
        - Each element represents the maximum jump length,
        not the exact jump length.
        - You can jump any distance from 1 to nums[i].
        - The last index is considered reachable from itself.
        - The greedy approach optimizes time and space
        complexity to O(n) and O(1), respectively.
        - All approaches assume a non-empty input array.
    """

    def jump_game_recursion(self, nums):
        """
        Intuition:
            At every index, explore all possible jumps and
            recursively check whether any path reaches the
            last index.

        Algorithm:
            1. Define a DFS function taking the current index.
            2. If the current index is the last index,
            return True.
            3. Calculate the farthest reachable index.
            4. Explore every index within the jump range
            using recursion.
            5. If any recursive call returns True, return True.
            6. If no path reaches the destination, return False.

        Time:
            O(2^n) upper bound due to exploring multiple
            possible paths without caching results.

        Space:
            O(n) for the maximum recursion stack depth.
        """
        def dfs(i: int) -> bool:
            if i == len(nums) - 1:
                return True

            end = min(len(nums) - 1, i + nums[i])

            for j in range(i + 1, end + 1):
                if dfs(j):
                    return True

            return False

        return dfs(0)

    def jump_game_memoization(self, nums):
        """
        Intuition:
            The recursive approach may solve the same
            subproblem multiple times. Memoization stores
            the result for each index so it is computed
            only once.

        Algorithm:
            1. Define a DFS function taking the current index.
            2. If the result is already in memo, return it.
            3. If the current index is the last index,
            return True.
            4. If nums[i] is 0, return False because no
            further jump is possible.
            5. Calculate the farthest reachable index.
            6. Recursively explore every reachable index.
            7. If any recursive call returns True, store
            True in memo and return True.
            8. Otherwise, store False in memo and return False.

        Time:
            O(n^2), since each index is computed once and
            may explore up to O(n) subsequent indices.

        Space:
            O(n) for the memoization dictionary and
            recursion stack.
        """
        def dfs(i: int) -> bool:
            if i in memo:
                return memo[i]

            if i == len(nums) - 1:
                return True

            if nums[i] == 0:
                memo[i] = False
                return False

            end = min(len(nums) - 1, i + nums[i])

            for j in range(i + 1, end + 1):
                if dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        memo = {}
        return dfs(0)

    def jump_game_tabulation(self, nums):
        """
        Intuition:
            Solve the problem bottom-up by starting at the
            last index and working backward. An index is
            reachable if it can jump to any index that is
            already known to reach the destination.

        Algorithm:
            1. Create a boolean DP array initialized to False.
            2. Mark the last index as True.
            3. Iterate backward from the second-last index.
            4. Calculate the farthest reachable index
            from the current position.
            5. Check all reachable positions. If any of
            them has dp[j] = True, mark dp[i] = True
            and stop checking further positions.
            6. Return dp[0] to determine whether the
            first index can reach the last index.

        Time:
            O(n^2), since each index may explore up to
            O(n) subsequent positions.

        Space:
            O(n) for the DP array.
        """
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            end = min(n - 1, i + nums[i])

            for j in range(i + 1, end + 1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]

    def jump_game_greedy(self, nums):
        """
        Intuition:
            Instead of exploring every possible jump,
            work backward from the last index and maintain
            the leftmost index that can reach the destination.

            If the current index can reach the current
            leftmost reachable index, update the target
            to the current index.

        Algorithm:
            1. Initialize last_idx to the last index.
            2. Iterate backward from the second-last index
            to the first index.
            3. If i + nums[i] >= last_idx, the current
            index can reach the destination or a
            position that can reach it.
            4. Update last_idx = i.
            5. After traversal, return True if last_idx
            is 0, otherwise return False.

        Time:
            O(n), since the array is traversed once.

        Space:
            O(1), since only a single variable is required.
        """
        last_idx = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_idx:
                last_idx = i

        return last_idx == 0

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums, expected)
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([3, 3, 1, 0, 4], True),
        ([2, 0], True),
        ([0], True),
        ([2, 0, 0], True),
        ([0, 2, 3], False),
    ]

    approaches = [
        ("Recursion", solution.jump_game_recursion),
        ("Memoization", solution.jump_game_memoization),
        ("Tabulation", solution.jump_game_tabulation),
        ("Greedy", solution.jump_game_greedy),
    ]

    for name, method in approaches:
        print(f"\n{'#' * 30}")
        print(f"Approach: {name}")
        print(f"{'#' * 30}")

        for nums, expected in test_cases:
            result = method(nums)

            assert result == expected, (
                f"\nTest case failed!\n"
                f"Approach = {name}\n"
                f"nums = {nums}\n"
                f"expected = {expected}\n"
                f"got = {result}\n"
            )

            print(
                f"\nnums = {nums}\n"
                f"expected = {expected}\n"
                f"got = {result}"
            )

    print("\n#######################\nAll test cases passed!!\n#######################")