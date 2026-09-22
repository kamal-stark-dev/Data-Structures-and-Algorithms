class Solution:
    """
    Problem:
        Given a string s, return the longest palindromic substring in s.

    Approach:
        1. Brute force: Check every possible substring and verify whether it
           is a palindrome.
        2. Dynamic programming: Use dp[i][j] to determine whether the
           substring s[i:j + 1] is a palindrome.
        3. Expand around center: Treat every character and every gap between
           characters as a potential center and expand while characters match.

    Constraints:
        - 1 <= s.length <= 1000
        - s consists of only digits and English letters.

    Notes:
        - If multiple longest palindromic substrings exist, returning any one
          of them is valid.
        - For example, both "bab" and "aba" are valid answers for "babad".
    """

    def longest_palindromic_substring_brute_force(self, s: str) -> str:
        """
        Intuition:
            Generate every possible substring and check whether it is a
            palindrome. Keep track of the longest valid palindrome found.

        Algorithm:
            1. Iterate over every possible starting index i.
            2. Iterate over every possible ending index j.
            3. Skip the substring if its length is not greater than the
               longest palindrome found so far.
            4. Use two pointers to check whether s[i:j + 1] is a palindrome.
            5. If it is a palindrome, update the result and its length.

        Time:
            O(n^3) in the worst case.
            There are O(n^2) substrings, and checking a substring can take O(n).

        Space:
            O(1) auxiliary space, excluding the returned substring.
        """

        res, resLen = "", 0
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                if j - i + 1 <= resLen:
                    continue

                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r:
                    resLen = j - i + 1
                    res = s[i: j + 1]

        return res

    def longest_palindromic_substring_dp(self, s: str) -> str:
        """
        Intuition:
            A substring s[i:j + 1] is a palindrome if its first and last
            characters are equal and the substring between them is also a
            palindrome.

            This allows us to reuse previously computed results instead of
            checking each substring independently.

        Algorithm:
            1. Create a 2D dp table where dp[i][j] indicates whether
               s[i:j + 1] is a palindrome.
            2. Iterate i from right to left so that dp[i + 1][j - 1] has
               already been computed.
            3. A substring is a palindrome when:
               - s[i] == s[j], and
               - its length is at most 3, or its inner substring is a
                 palindrome.
            4. Whenever a palindrome longer than the current result is found,
               update its starting index and length.
            5. Return the longest palindromic substring.

        Time:
            O(n^2), because every pair (i, j) is evaluated once.

        Space:
            O(n^2) for the DP table.
        """

        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx: resIdx + resLen]

    def longest_palindromic_substring_two_pointers(self, s: str) -> str:
        """
        Intuition:
            Every palindrome has a center. The center can be:
            - A single character for odd-length palindromes.
            - The gap between two characters for even-length palindromes.

            Expand outward from each possible center while the characters
            on both sides are equal.

        Algorithm:
            1. Treat each character as the center of an odd-length palindrome.
            2. Expand left and right while the characters match.
            3. Update the longest palindrome whenever a longer one is found.
            4. Treat each gap between adjacent characters as the center of an
               even-length palindrome.
            5. Expand outward using the same process.
            6. Return the longest palindrome found.

        Time:
            O(n^2) in the worst case, because there are O(n) centers and
            each center can require O(n) expansion.

        Space:
            O(1) auxiliary space, excluding the returned substring.
        """

        resIdx, resLen = 0, 0
        n = len(s)

        for i in range(n):
            # Odd-length palindrome: center is s[i].
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # Even-length palindrome: center is between s[i] and s[i + 1].
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx: resIdx + resLen]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (s: str, expected_length: int)
        ("babad", 3),
        ("cbbd", 2),
        ("racecar", 7),
        ("jake", 1)
    ]

    for s, expected in test_cases:
        result = solution.longest_palindromic_substring_two_pointers(s)

        assert len(result) == expected and result == result[::-1], (
            f"\n\nTest case failed!\n"
            f"s = {s}\n"
            f"expectedLen = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"s = {s}\n"
            f"expectedLen = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")