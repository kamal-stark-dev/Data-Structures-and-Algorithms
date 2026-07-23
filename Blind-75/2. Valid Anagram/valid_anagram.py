class Solution:
    """Different approaches to find if given strings are anagrams or not."""

    def is_anagram_brute_force(self, s: str, t: str) -> bool:
        """
        Return True if the given strings are anagrams.

        Time: O(n^2)
        Space: O(1)

        Constraints:
            1 <= s.length, t.length <= 5 * 104
            s and t consist of lowercase English letters.
        """

        if len(s) != len(t):
            return False

        # Strings are immutable in Python, so convert to a list for in-place marking.
        t = list(t)


        for ch in s:
            char_found = False

            for i in range(len(t)):
                if ch == t[i]:
                    char_found = True
                    t[i] = '$' # using '$' as the input only contains lowercase English letters
                    break

            if not char_found:
                return False

        return True


    def is_anagram_sorting(self, s: str, t: str) -> bool:
        """
        Return True if s and t are anagrams using sorting approach.

        Time: O(n logn)
        Space: O(n) # due to sorted() creating new lists
        """

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


    def is_anagram_hash_map(self, s: str, t: str) -> bool:
        """
        Return True if s and t are anagrams using a hash map.

        Time: O(n)
        Space: O(n)
        """

        if len(s) != len(t):
            return False

        s_map, t_map = dict(), dict()

        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)

        return s_map == t_map


    def is_anagram_array(self, s: str, t: str) -> bool:
        """
        Return True if s and t are anagrams using an array to count frequencies.

        Time: O(n)
        Space: O(1)
        """

        if len(s) != len(t):
            return False

        freq = [0] * 26

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False

        return True

        # you can also use this one-liner for checking if each element is 0 or not
        return all(count == 0 for count in freq)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("bat", "tab", True),
        ("anagram", "nagaram", True),
        ("racecar", "basecar", False),
    ]

    for s, t, expected_output in test_cases:
        result = solution.is_anagram_array(s, t)

        assert result == expected_output

        print(
            f"Input: s = {s}, t = {t}\n"
            f"Expected: {expected_output}, Got: {result}\n"
        )

    print("All test cases passed!!")


