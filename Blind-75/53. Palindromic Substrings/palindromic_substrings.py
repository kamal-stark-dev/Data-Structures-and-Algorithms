class Solution:
    """
    Problem:
        Given a string s, return the number of palindromic substrings in it.

        A palindrome is a string that reads the same forwards and backwards.
        A substring is a contiguous sequence of characters within the string.

        Note that different occurrences of the same palindrome are counted
        separately.

    Approach:
        1. Brute Force:
           Generate every possible substring and check whether it is a
           palindrome.

        2. Dynamic Programming:
           Use dp[i][j] to determine whether the substring s[i:j + 1]
           is a palindrome based on its inner substring.

        3. Expand Around Center:
           Every palindrome has a center. For every character, expand
           outward to find odd-length and even-length palindromes.

    Constraints:
        - 1 <= s.length <= 1000
        - s consists of lowercase English letters.

    Notes:
        - Single characters are always palindromes.
        - For a palindrome of length >= 3, the first and last characters
          must match and the substring between them must also be a palindrome.
        - The center-expansion approach reduces the extra space required by
          the DP solution while maintaining O(n²) time.
    """

    def palindromic_substrings_brute_force(self, s: str) -> int:
        """
        Intuition:
            - Every substring is a potential palindrome.
            - Generate all possible substrings and directly compare each
              substring with its reversed version.
            - Count the substring whenever the two are equal.

        Algorithm:
            - Use two pointers i and j to represent every possible
              substring s[i:j + 1].
            - Reverse the substring and compare it with the original.
            - If they are equal, the substring is a palindrome and we
              increment the result.

        Time:
            O(n³)

            There are O(n²) possible substrings.
            Reversing/comparing a substring can take O(n) time.
            Therefore, the total complexity is O(n³).

        Space:
            O(n)

            Reversing a substring creates a temporary string of up to
            O(n) characters.

        """

        res = 0
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                if s[i:j + 1] == s[i: j + 1][::-1]:
                    res += 1

        return res

    def palindromic_substrings_dp(self, s: str) -> int:
        """
        Intuition:
            - Instead of repeatedly checking whether every substring is a
              palindrome from scratch, store the result for smaller
              substrings and reuse it.
            - A substring s[i:j + 1] is a palindrome if:
                1. s[i] == s[j], and
                2. The substring inside it, s[i + 1:j], is also a palindrome.
            - Single characters are always palindromes.
            - A substring of length 2 is a palindrome when both characters
              are equal.

        Algorithm:
            - Create a 2D DP table where dp[i][j] represents whether
              s[i:j + 1] is a palindrome.
            - Mark every single character as a palindrome.
            - Process substrings by increasing length.
            - For each substring:
                - Check whether its first and last characters match.
                - If its length is 2, it is a palindrome when those
                  characters match.
                - Otherwise, check dp[i + 1][j - 1].
            - Increment the result whenever dp[i][j] is True.

        Time:
            O(n²)

            There are O(n²) possible substrings and each DP state is
            calculated in O(1) time.

        Space:
            O(n²)

            The DP table contains n² boolean states.

        """

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res = 0

        for i in range(n):
            dp[i][i] = True
            res += 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                    if dp[i][j]:
                        res += 1

        return res

    def palindromic_substrings_two_pointers(self, s: str) -> int:
        """
        Intuition:
            - Every palindrome can be identified by its center.
            - Instead of generating every substring, treat each position
              as a possible center and expand outward while the characters
              on both sides are equal.
            - There are two types of palindrome centers:
                1. Odd-length palindromes have one character as their center.
                   Example: "racecar"
                2. Even-length palindromes have the gap between two characters
                   as their center.
                   Example: "abba"
            - By expanding around both types of centers, every palindromic
              substring is counted exactly once.

        Algorithm:
            - Define a helper function count_palindromes(l, r) that expands
              outward from the given center.
            - While l and r are valid indices and s[l] == s[r]:
                - Count the current palindrome.
                - Move l one step left.
                - Move r one step right.
            - For every index i:
                - Expand from (i, i) to find odd-length palindromes.
                - Expand from (i, i + 1) to find even-length palindromes.
            - Add the counts from both expansions to the result.

        Time:
            O(n²)

            There are O(n) possible centers, and each center can require
            O(n) expansion in the worst case.

        Space:
            O(1)

            Apart from the input string and a few variables, no additional
            data structure is required.

        """

        def count_palindromes(l: int, r: int) -> int:
            count = 0

            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        n = len(s)
        res = 0

        for i in range(n):
            # odd length palindromes
            res += count_palindromes(i, i)

            # even length palindromes
            res += count_palindromes(i, i + 1)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (s: str, expected: int)
        ("abc", 3),
        ("aaa", 6),
        ("racecar", 10),
    ]

    for s, expected in test_cases:
        result = solution.palindromic_substrings_two_pointers(s)

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