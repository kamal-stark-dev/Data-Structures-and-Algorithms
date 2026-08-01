from collections import Counter

class Solution:
    """
    Problem:
        Given two strings `s` and `t`, return the smallest substring of `s`
        that contains every character from `t`, including duplicate
        occurrences.

        If no such substring exists, return an empty string.

    Approach:
        1. Brute Force:
            - Generate every possible substring.
            - Count character frequencies.
            - Check whether the substring satisfies the character
              requirements of `t`.
            - Track the smallest valid substring.

        2. Sliding Window:
            - Maintain a variable-size window using two pointers.
            - Expand the window until it contains all required characters.
            - Shrink it while it remains valid to obtain the minimum window.
            - Repeat until the end of the string.

    Constraints:
        - 1 <= len(s), len(t) <= 10^5
        - s and t contain uppercase and lowercase English letters.

    Notes:
        - Characters may appear multiple times in `t`, and those duplicate
          frequencies must also be present in the window.
        - The problem guarantees a unique minimum window if one exists.
    """

    def minimum_window_substring_brute_force(self, s: str, t: str) -> str:
        """
        Intuition:
            Every possible substring could potentially be the answer.
            Generate each substring, count its characters, and determine
            whether it contains all required characters from `t`.
            Keep the shortest valid substring found.

        Algorithm:
            1. Count the frequency of every character in `t`.
            2. Iterate over every possible starting index.
            3. Expand the ending index one character at a time while
               maintaining the current character counts.
            4. Compare the current counts with the required counts.
            5. Update the answer whenever a smaller valid window is found.
            6. Return the smallest valid substring, or an empty string if
               none exists.

        Time:
            O(n^2)

        Space:
            O(n)
        """

        if t == "":
            return ""

        counter_t = Counter(t)

        res = s
        for i in range(len(s)):
            curr_counter = Counter()
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                curr_counter[s[j]] += 1

                if counter_t <= curr_counter and len(substr) < len(res):
                    res = substr

        return res if counter_t <= Counter(res) else ""


    def minimum_window_substring_sliding_window(self, s: str, t: str) -> str:
        """
        Intuition:
            Instead of checking every substring, maintain a sliding window
            that expands until it satisfies all character requirements.
            Once valid, shrink the window as much as possible while keeping
            it valid, ensuring the minimum window is found efficiently.

        Algorithm:
            1. Build a frequency map for the characters in `t`.
            2. Expand the right pointer, adding characters to the current
               window.
            3. Track how many required character frequencies have been met.
            4. When all requirements are satisfied:
                - Update the minimum window if the current one is smaller.
                - Move the left pointer to shrink the window.
                - Stop shrinking once the window is no longer valid.
            5. Continue until the right pointer reaches the end of `s`.
            6. Return the smallest recorded window, or an empty string if no
               valid window exists.

        Time:
            O(m + n), where m is the total number of unique characters in `t` and `s`

        Space:
            O(n)
        """

        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        left = 0
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        left, right = res
        return s[left: right + 1] if resLen != float("infinity") else ""



if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (s: str, t: str, expected)
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("b", "bb", ""),
        ("ab", "a", "a"),
    ]

    for s, t, expected in test_cases:
        result = solution.minimum_window_substring_sliding_window(s, t)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"s = '{s}'\n"
            f"t = '{t}'\n"
            f"expected = '{expected}'\n"
            f"got = '{result}'\n"
        )

        print(
            f"s = '{s}'\n"
            f"t = '{t}'\n"
            f"expected = '{expected}'\n"
            f"got = '{result}'\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")