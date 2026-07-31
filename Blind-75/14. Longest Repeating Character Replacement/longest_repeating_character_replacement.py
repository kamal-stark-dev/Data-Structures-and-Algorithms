class Solution:
    """
   Problem:
        Given a string consisting of uppercase English letters and an integer
        k, return the length of the longest substring that can be transformed
        into a string of identical characters by replacing at most k characters.

    Approach:
        1. Brute Force:
            - Enumerate every possible substring.
            - Count the frequency of each character.
            - Check whether the substring can be made uniform using at most
              k replacements.

        2. Sliding Window:
            - Maintain a valid window using two pointers.
            - Track character frequencies inside the current window.
            - Shrink the window whenever more than k replacements are required.

        3. Optimized Sliding Window:
            - Track the maximum character frequency seen in the current window.
            - Avoid recomputing the maximum frequency each time the window
              changes, reducing unnecessary work while maintaining correctness.

    Constraints:
        - 1 <= s.length <= 10^5
        - s consists only of uppercase English letters.
        - 0 <= k <= s.length

    Notes:
        - A window of length L is valid if:
            L - (frequency of the most common character) <= k
        - This works because all other characters can be replaced to match
          the most frequent character.
    """

    def longest_repeating_character_replacement_brute_force(self, s: str, k: int) -> int:
        """
        Intuition:
            Consider every possible substring. For each substring, determine
            how many replacements are needed to make every character the same.
            If the required replacements exceed k, extending the substring
            further from the same starting position cannot make it valid.

        Algorithm:
            - Iterate over every possible starting index.
            - Expand the ending index one character at a time.
            - Maintain character frequencies for the current substring.
            - Let max_freq be the highest character frequency.
            - If:
                  substring_length - max_freq <= k
              update the answer.
            - Otherwise, stop expanding from the current start index.

        Time:
            O(n^2)

        Space:
            O(1), cause we've used seen array of fixed size 26 (for all uppercase English letters)
        """

        res = 0
        for i in range(len(s)):
            seen = [0] * 26
            for j in range(i, len(s)):
                seen[ord(s[j]) - ord('A')] += 1
                if (j - i + 1) - max(seen) <= k:
                    res = max(res, j - i + 1)
                else:
                    break

        return res


    def longest_repeating_character_replacement_sliding_window(self, s: str, k: int) -> int:
        """
        Intuition:
            Instead of checking every substring independently, maintain a
            sliding window that always represents the longest valid substring
            ending at the current position.

        Algorithm:
            - Expand the right pointer one character at a time.
            - Update the frequency of the newly added character.
            - Compute the maximum frequency in the current window.
            - While the window requires more than k replacements:
                  window_size - max_frequency > k
              shrink the window from the left.
            - Record the largest valid window encountered.

        Time:
            O(26 * n) = O(n)
            (Computing max(seen) costs O(26), which is constant.)

        Space:
            O(1), cause we've used seen array of fixed size 26 (for all uppercase English letters)
        """

        res = 0
        left = 0
        seen = [0] * 26

        for right in range(len(s)):
            seen[ord(s[right]) - ord('A')] += 1

            while (right - left + 1) - max(seen) > k:
                seen[ord(s[left]) - ord('A')] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


    def longest_repeating_character_replacement_sliding_window_optimal(self, s: str, k: int) -> int:
        """
        Intuition:
            The expensive part of the previous solution is repeatedly finding
            the maximum character frequency in the current window. Instead,
            keep track of the largest frequency seen while expanding the
            window.

            Although this maximum may become stale after shrinking the window,
            it never affects the correctness of the final answer because it
            only delays shrinking and never causes a valid answer to be missed.

        Algorithm:
            - Expand the window by moving the right pointer.
            - Update the frequency of the new character.
            - Update maxf with the largest frequency seen so far.
            - If:
                  window_size - maxf > k
              shrink the window from the left until it becomes valid.
            - Track the maximum valid window size.

        Time:
            O(n)

        Space:
            O(1), cause we've used seen array of fixed size 26 (for all uppercase English letters)
        """

        res = 0
        left = 0
        seen = [0] * 26
        maxf = 0

        for right in range(len(s)):
            seen[ord(s[right]) - ord('A')] += 1
            maxf = max(maxf, seen[ord(s[right]) - ord('A')])

            while (right - left + 1) - maxf > k:
                seen[ord(s[left]) - ord('A')] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (s:str, k:int, expected)
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("ABCC", 2, 4),
        ("AABC", 1, 3),
    ]

    for s, k, expected in test_cases:
        result = solution.longest_repeating_character_replacement_sliding_window_optimal(s, k)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"s = {s}\n"
            f"k = {k}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"s = {s}\n"
            f"k = {k}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")