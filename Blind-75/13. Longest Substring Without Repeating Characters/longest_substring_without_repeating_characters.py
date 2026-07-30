class Solution:
    """
    Problem:
        Given a string s, find the length of the longest substring without
        duplicate characters. A substring is a contiguous sequence of characters
        within the string.

    Approach:
        1. Brute Force: Check every possible substring starting at each index
           using a set to detect duplicates.
        2. Sliding Window: Expand a window with `right`, shrink from `left`
           with a set until duplicates are removed.
        3. Optimized Sliding Window: Use a hash map to store last seen indices
           and jump `left` directly past the previous duplicate.

    Constraints:
        - 0 <= s.length <= 10^5
        - s consists of English letters, digits, symbols and spaces.

    Notes:
        - The answer must be a substring (contiguous), not a subsequence.
        - The character set is bounded, so space complexity is effectively
          O(min(n, m)) where m is the charset size.
    """

    def longest_substring_without_repeating_characters_brute_force(self, s: str) -> int:
        """
        Intuition:
            For each starting position i, expand outward as far as possible
            until we hit a repeating character. Track the maximum length seen.

        Algorithm:
            - Iterate i from 0 to n-1 as the start of the substring.
            - Initialize a set with s[i].
            - Iterate j from i+1 to n-1:
                - If s[j] is already in the set, break (duplicate found).
                - Otherwise, add s[j] to the set.
            - Update max_len with the size of the current set.

        Time:
            O(n^2) in the worst case. For each starting index i, the inner
            loop may scan up to n characters.

        Space:
            O(m), where m is the number of unique characters in the string.
            # (and m ≤ n is implied)
        """

        max_len = 0

        for i in range(len(s)):
            seen = set(s[i])

            for j in range(i + 1, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])

            max_len = max(max_len, len(seen))

        return max_len


    def longest_substring_without_repeating_characters_sliding_window(self, s: str) -> int:
        """
        Intuition:
            Maintain a window [left, right] that always contains unique
            characters. Expand right one step at a time. If the new character
            creates a duplicate, shrink the window from the left until the
            duplicate is removed.

        Algorithm:
            - Initialize left = 0 and an empty set.
            - Iterate right from 0 to n-1:
                - While s[right] is already in the set:
                    - Remove s[left] from the set.
                    - Increment left.
                - Add s[right] to the set.
                - Update max_len with window size (right - left + 1).

        Time:
            O(n). Each character is visited by right once and removed by
            left at most once. All set operations are O(1).

        Space:
            O(m), where m is the number of unique characters in the string.
            # (and m ≤ n is implied)
        """

        max_len = 0

        left = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


    def longest_substring_without_repeating_characters_sliding_window_optimal(self, s: str) -> int:
        """
        Intuition:
            Instead of shrinking the window one character at a time when a
            duplicate is found, use a hash map to remember the last index
            where each character appeared. When s[right] is a duplicate,
            jump left directly to max(left, last_index[s[right]] + 1) to
            exclude the previous occurrence. The max with left ensures we
            never move the window boundary backwards.

        Algorithm:
            - Initialize left = 0 and an empty hash map mp.
            - Iterate right from 0 to n-1:
                - If s[right] was seen before:
                    - left = max(left, mp[s[right]] + 1)
                - Update mp[s[right]] = right (store current index).
                - Update max_len with window size (right - left + 1).

        Time:
            O(n). Single pass through the string with O(1) hash map operations.

        Space:
            O(m), where m is the number of unique characters in the string.
            # (and m ≤ n is implied)
        """

        max_len = 0
        left = 0
        mp = dict()

        for right in range(len(s)):
            if s[right] in mp:
                # Move left to just after the previous occurrence of s[right].
                # The max ensures left never moves backwards, since the
                # previous occurrence might already be outside the window.
                left = max(left, mp[s[right]] + 1)
            mp[s[right]] = right # update the last seen index
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (s, expected)
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("abcdef", 6),
        ("abba", 2),  # Edge case for the optimal solution
    ]

    for s, expected in test_cases:
        result = solution.longest_substring_without_repeating_characters_sliding_window_optimal(s)

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