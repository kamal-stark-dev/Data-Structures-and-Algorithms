class Solution:
    """
    Problem:
        Given a string of digits where:
            "1" -> 'A', "2" -> 'B', ..., "26" -> 'Z',
        return the number of ways the entire string can be decoded.

        A digit can be decoded individually if it is between '1' and '9'.
        Two consecutive digits can be decoded together if they form a
        number between 10 and 26.

        A '0' cannot be decoded by itself.

    Approach:
        1. Recursion: Try decoding one digit or two digits at every position.
        2. Memoization: Cache the result for each index to avoid recomputation.
        3. Tabulation: Build the number of decoding ways from right to left.
        4. Space Optimization: Keep only the previous two DP states.

    Constraints:
        - 1 <= len(s) <= 100
        - s contains only digits.
        - The string may contain leading zeroes.
        - The answer fits in a 32-bit integer.

    Notes:
        The main recurrence is:

            dp[i] = dp[i + 1] + dp[i + 2]

        where:
            - dp[i + 1] represents decoding s[i] as a single digit.
            - dp[i + 2] represents decoding s[i:i+2] as a two-digit number.

        We only add dp[i + 2] when s[i:i+2] represents a valid number
        between 10 and 26.
    """

    def decode_ways_recursion(self, s: str) -> int:
        """
        Intuition:
            At every index, we have at most two choices:
                1. Decode the current digit by itself.
                2. Decode the current and next digits together.

            A single digit is valid when it is not '0'.
            Two digits are valid when they form a number from 10 to 26.

            We recursively explore both choices and add the number of valid
            decodings produced by each choice.

            Reaching the end of the string means we have found one complete
            valid decoding, so we return 1.

        Algorithm:
            1. Start a recursive DFS from index 0.
            2. If i reaches len(s), return 1 because a complete decoding
               has been found.
            3. If s[i] is '0', return 0 because '0' cannot be decoded alone.
            4. Decode s[i] as a single digit and recursively solve i + 1.
            5. If s[i] and s[i + 1] form a number between 10 and 26,
               recursively solve i + 2 and add that result.
            6. Return the total number of decoding ways.

        Time:
            O(2^n)

            In the worst case, every position branches into two recursive
            calls, producing an exponential recursion tree.

        Space:
            O(n)

            The maximum recursion depth is n.
        """

        def dfs(i: int) -> int:
            # valid decoding found
            if i == len(s):
                return 1

            # invalid decoding
            if s[i] == '0':
                return 0

            res = dfs(i + 1)

            if i < len(s) - 1:
                if (
                    s[i] == '1' or
                    (s[i] == '2' and s[i + 1] < '7')
                ):
                    res += dfs(i + 2)

            return res

        return dfs(0)


    def decode_ways_memoization(self, s: str) -> int:
        """
        Intuition:
            The recursive solution repeatedly solves the same subproblem.

            For example, when different decoding paths reach the same index i,
            the number of ways to decode the suffix starting at i is always
            the same.

            Therefore, we store the answer for every index after calculating
            it once. This converts the exponential recursion into a linear
            dynamic programming solution.

        Algorithm:
            1. Create a memoization dictionary where dp[i] represents the
               number of ways to decode s[i:].
            2. Set dp[len(s)] = 1 because reaching the end represents one
               valid decoding.
            3. For each recursive call:
                - Return the cached value if i has already been solved.
                - Return 0 if s[i] is '0'.
                - Count the ways obtained by decoding one digit.
                - If the next two digits form a number between 10 and 26,
                  also count the ways obtained by decoding two digits.
            4. Store the result for index i in dp.
            5. Return the result starting from index 0.

        Time:
            O(n)

            There are only n possible indices, and each index is solved once.
            Each state performs O(1) work.

        Space:
            O(n)

            The memoization dictionary stores one result for each index,
            and the recursion stack can also grow to O(n).
        """

        dp = {len(s): 1}

        def dfs(i: int) -> int:
            # valid decoding found
            if i in dp:
                return dp[i]

            # invalid decoding
            if s[i] == '0':
                return 0

            res = dfs(i + 1)

            if i < len(s) - 1:
                if (
                    s[i] == '1' or
                    (s[i] == '2' and s[i + 1] < '7')
                ):
                    res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)


    def decode_ways_tabulation(self, s: str) -> int:
        """
        Intuition:
            The memoized solution tells us that the answer at index i depends
            only on the answers at i + 1 and i + 2.

            Instead of using recursion, we can calculate these values
            iteratively from right to left.

            dp[i] represents the number of ways to decode the suffix s[i:].

            If s[i] is not '0', we can always decode it as one digit and
            inherit dp[i + 1]. If s[i:i+2] is between 10 and 26, we can also
            decode those two digits together and add dp[i + 2].

        Algorithm:
            1. If the first character is '0', return 0 because the entire
               string cannot be decoded.
            2. Initialize dp[n] = 1, representing the valid empty suffix.
            3. Iterate from index n - 1 down to 0.
            4. If s[i] is '0', set dp[i] = 0.
            5. Otherwise, set dp[i] = dp[i + 1] because the current digit
               can be decoded individually.
            6. If s[i:i+2] forms a valid number between 10 and 26, add
               dp[i + 2].
            7. Return dp[0].

        Time:
            O(n)

            Every character is processed once, with constant work per index.

        Space:
            O(n)

            The DP dictionary stores the result for every index.
        """

        if s[0] == '0':
            return 0

        n = len(s)
        dp = {n: 1}

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < n and (
                s[i] == '1' or
                (s[i] == '2' and s[i + 1] < '7')
            ):
                dp[i] += dp[i + 2]

        return dp[0]


    def decode_ways_optimal(self, s: str) -> int:
        """
        Intuition:
            The tabulation solution only needs the next two DP states:

                dp[i] depends on dp[i + 1] and dp[i + 2]

            Therefore, we do not need to store the entire DP array.

            We maintain three values:
                - next_ways:
                    dp[i + 1], the number of ways to decode the suffix
                    starting one position after i.

                - next_next_ways:
                    dp[i + 2], the number of ways to decode the suffix
                    starting two positions after i.

                - current_ways:
                    dp[i], the number of ways to decode the suffix
                    starting at i.

            After calculating dp[i], we shift these three values one position
            to the left and continue.

        Algorithm:
            1. Initialize dp[n] = 1 conceptually by setting next_ways = 1.
            2. Start from the last character and move toward the beginning.
            3. If s[i] is '0', current_ways = 0 because it cannot be decoded
               individually.
            4. Otherwise, current_ways starts as next_ways because s[i]
               can be decoded as a single digit.
            5. If s[i:i+2] forms a valid number between 10 and 26, add
               next_next_ways because the two digits can be decoded together.
            6. Shift the states:
                   dp[i + 1] -> next_ways
                   dp[i + 2] -> next_next_ways
            7. After processing the entire string, next_ways contains dp[0],
               which is the answer.

        Time:
            O(n)

            We scan the string exactly once and perform constant work at
            every index.

        Space:
            O(1)

            Only three variables are maintained regardless of the input size.
        """

        current_ways = 0
        next_ways = 1
        next_next_ways = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                current_ways = 0
            else:
                current_ways = next_ways

            # check if we can decode two digits together
            if i < len(s) - 1 and (
                s[i] == '1' or
                (s[i] == '2' and s[i + 1] < '7')
            ):
                current_ways += next_next_ways

            # move the window one position to the left
            current_ways, next_ways, next_next_ways = (
                0,
                current_ways,
                next_ways
            )

        return next_ways


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (s: str, expected: int)
        ("11106", 2),
        ("12", 2),
        ("226", 3),
        ("06", 0),
    ]

    for s, expected in test_cases:
        result = solution.decode_ways_optimal(s)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"s = {s}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"s = {s}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")