import re

class Solution:
    """
    Given a string s, return true if it is a palindrome, or false otherwise.

    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Constraints:
        1 <= s.length <= 2 * 105
        s consists only of printable ASCII characters.
    """

    def valid_palindrome_reverse_string(self, s: str) -> bool:
        """
        Check whether a string is a palindrome by creating a cleaned copy.

        This approach:
            1. Converts every character to lowercase.
            2. Removes all non-alphanumeric characters.
            3. Compares the cleaned string with its reverse.

        Since a palindrome reads the same forwards and backwards,
        the cleaned string should be identical to its reversed version.

        Time: O(n)
        Space: O(n) for storing t and reverse of t
        """

        t = []
        for ch in s.lower():
            if ch.isalnum():
                t.append(ch)
        t = "".join(t)

        return t == t[::-1]


    def valid_palindrome_two_pointers(self, s: str) -> bool:
        """
        Check whether a string is a palindrome using the two-pointer technique.

        Two pointers are placed at the beginning and end of the string.
        The pointers move toward each other while skipping any
        non-alphanumeric characters.

        At each step:
            1. Ignore any non-alphanumeric character.
            2. Compare the lowercase versions of the characters.
            3. If a mismatch is found, the string is not a palindrome.
            4. Otherwise, continue until the pointers meet.

        This approach avoids creating an extra cleaned string,
        making it more memory-efficient.

        Time: O(n)
        Space: O(1)
        """

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


    def valid_palindrome_re(self, s: str) -> bool:
        """
        Check whether a string is a palindrome using regular expressions.

        This approach:
            1. Uses a regular expression to remove every character that
            is not a letter or digit.
            2. Converts the remaining characters to lowercase.
            3. Compares the cleaned string with its reverse.

        The regular expression: r'[^a-zA-Z0-9]'

        matches every character that is NOT:
            - a-z
            - A-Z
            - 0-9

        Those matched characters are replaced with an empty string.

        Time: O(n)
        Space: O(n) for substituted string and lowercasing it and reversing it
        """

        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True)
    ]

    for s, expected in test_cases:
        result = solution.valid_palindrome_two_pointers(s)

        assert result == expected

        print(
            f"s = `{s}`\n"
            f"got = {result}, expected = {expected}\n"
        )

    print("#######################\nAll test cases passed!!\n#######################")
