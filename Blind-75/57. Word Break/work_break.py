class Solution:
    """
    Problem:
        Given a string `s` and a dictionary of strings `wordDict`, return
        True if `s` can be segmented into a sequence of one or more
        dictionary words.

        A dictionary word can be reused multiple times.

    Approach:
        1. Recursion: Try every possible substring starting from the
           current index and recursively check whether the remaining
           string can be segmented.
        2. Memoization: Store the result for each starting index so that
           the same subproblem is not solved repeatedly.
        3. Tabulation: Build a DP array where dp[i] represents whether
           the first `i` characters of `s` can be segmented using words
           from the dictionary.

    Constraints:
        - 1 <= s.length <= 300
        - 1 <= wordDict.length <= 1000
        - 1 <= wordDict[i].length <= 20
        - s and wordDict[i] contain only lowercase English letters.
        - All words in wordDict are unique.

    Notes:
        - The same dictionary word can be reused multiple times.
        - A set is used for wordDict to provide average O(1) word lookup.
    """

    def word_break_recursion(self, s: str, wordDict: list[str]) -> bool:
        """
        Intuition:
            Starting from the beginning of the string, keep building the
            current substring character by character.

            Whenever the current substring forms a valid dictionary word,
            start a new word from the next character. We also continue
            extending the current substring because a longer dictionary
            word may exist.

            If we reach the end of the string with no unfinished word,
            the string can be successfully segmented.

        Algorithm:
            1. Convert wordDict into a set for fast lookup.
            2. Use DFS with index `i` and the currently formed word `curr`.
            3. Add s[i] to curr.
            4. If curr is a dictionary word, recursively try starting
               a new word from the next character.
            5. Also recursively continue extending curr.
            6. If the end of the string is reached, return True only when
               curr is empty, meaning the last word was already matched.

        Time:
            O(2^n * n)

        Space:
            O(n)
        """

        def dfs(i: int, curr: str) -> bool:
            if i == len(s):
                return True if curr == "" else False

            curr += s[i]

            if curr in words:
                if dfs(i + 1, ""):
                    return True

            return dfs(i + 1, curr)

        words = set(wordDict)

        return dfs(0, "")

    def word_break_memoization(self, s: str, wordDict: list[str]) -> bool:
        """
        Intuition:
            The important state is the index `i` from which we still need
            to segment the string.

            From index `i`, try every possible substring s[i:j]. If it is
            present in the dictionary, recursively check whether the
            remaining substring starting at `j` can be segmented.

            The same index can be reached through different choices of
            previous words, so we memoize the result for every index.

        Algorithm:
            1. Convert wordDict into a set for fast lookup.
            2. Define dfs(i) as whether s[i:] can be segmented.
            3. Try every substring s[i:j].
            4. If s[i:j] is a dictionary word, recursively solve dfs(j).
            5. If any choice returns True, memoize and return True.
            6. If no choice works, memoize False for index i.
            7. Start the recursion from index 0.

        Time:
            O(n^3)

        Space:
            O(n)
        """

        def dfs(i: int) -> bool:
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for j in range(i + 1, len(s) + 1):
                curr = s[i: j]

                if curr in words and dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        words = set(wordDict)
        memo = {}

        return dfs(0)

    def word_break_tabulation(self, s: str, wordDict: list[str]) -> bool:
        """
        Intuition:
            Convert the recursive solution into bottom-up dynamic
            programming.

            Let dp[i] represent whether the first `i` characters of `s`
            can be segmented into dictionary words.

            dp[0] is True because an empty prefix requires no words.

            For every position i that represents a valid segmentation,
            try every possible word ending at position j. If s[i:j] is
            present in the dictionary, then the prefix ending at j can
            also be segmented.

        Algorithm:
            1. Create a DP array of size n + 1.
            2. Set dp[0] = True because the empty string is considered
               successfully segmented.
            3. For every starting position i, try every ending position j.
            4. Form the substring s[i:j].
            5. If the substring exists in the dictionary and dp[i] is True,
               mark dp[j] as True.
            6. Return dp[n], which represents whether the entire string
               can be segmented.

        Time:
            O(n^3)

        Space:
            O(n)
        """

        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        words = set(wordDict)

        for i in range(n + 1):

            for j in range(i + 1, n + 1):
                word = s[i: j]

                if word in words and dp[i]:
                    dp[j] = True

        return dp[n]

    def word_break_tabulation_optimal(self, s: str, wordDict: list[str]) -> bool:
        """
        Intuition:
            This is an optimized version of the tabulation approach.

            Let dp[i] represent whether the first i characters of s can be
            successfully segmented into dictionary words.

            If dp[i] is False, it means there is no valid segmentation that
            reaches index i, so there is no point in trying to build words
            starting from i. We can simply skip that position.

            Additionally, we only need to check substrings whose length is
            at most the length of the longest word in the dictionary. Any
            substring longer than the longest dictionary word can never
            be a valid word.

            Therefore, from every reachable index i, we only check possible
            substrings from i to min(n, i + maxLen).

        Algorithm:
            1. Convert wordDict into a set for average O(1) word lookup.

            2. Find maxLen, the length of the longest word in wordDict.

            3. Create a DP array of size n + 1.

            4. Set dp[0] = True because the empty prefix is considered
            successfully segmented.

            5. Iterate through every index i from 0 to n.

            6. If dp[i] is False, skip this index because it cannot be
            reached through a valid segmentation.

            7. From index i, try every possible substring whose length is
            at most maxLen:
                s[i:j]

            The ending index j is limited to:
                min(n, i + maxLen)

            8. If s[i:j] exists in the dictionary, mark dp[j] as True
            because the prefix ending at j can now be segmented.

            9. Return dp[n], which represents whether the entire string
            can be segmented.

        Optimization:
            The basic tabulation solution checks all possible substrings,
            resulting in O(n^3) time because:

                - O(n^2) possible substrings
                - O(n) cost for creating/checking a substring in the
                worst case

            This version reduces the number of substrings checked by only
            considering words up to maxLen and by skipping unreachable
            positions where dp[i] is False.

        Time:
            O(n^2 * L) in the general case, where L is the maximum word
            length in wordDict.

            Since L <= n, the worst-case complexity is O(n^3).

            With the given constraints where each dictionary word has
            length at most 20, L is bounded by 20, making the practical
            complexity approximately O(n^2).

        Space:
            O(n) for the DP array and O(m) for the dictionary set,
            where m is the total number of characters stored in wordDict.
        """

        n = len(s)

        words = set(wordDict)
        maxLen = max((len(word) for word in words), default=0)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n + 1):
            if not dp[i]:
                continue

            for j in range(i + 1, min(n, i + maxLen) + 1):
                if s[i: j] in words:
                    dp[j] = True

        return dp[n]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (s: str, wordDict: list[str], expected: bool)
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cat", "cats", "and", "dog"], False),
    ]

    for s, wordDict, expected in test_cases:
        result = solution.word_break_tabulation_optimal(s, wordDict)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"s = {s}\n"
            f"wordDict = {wordDict}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"s = {s}\n"
            f"wordDict = {wordDict}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")