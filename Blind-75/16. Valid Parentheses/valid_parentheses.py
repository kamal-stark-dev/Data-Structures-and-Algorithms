class Solution:
    """
    Problem:
        Given a string consisting only of the characters '(', ')', '{', '}',
        '[' and ']', determine whether the string represents a valid sequence
        of parentheses.

        A string is valid if:
            - Every opening bracket is closed by the same type of bracket.
            - Brackets are closed in the correct order.
            - Every closing bracket has a corresponding unmatched opening
              bracket.

    Approach:
        1. Implement a brute-force solution by repeatedly removing valid
           adjacent bracket pairs until no more can be removed.
        2. Implement an optimal stack-based solution that tracks unmatched
           opening brackets.
        3. Whenever a closing bracket is encountered, verify that it matches
           the most recent opening bracket.

    Constraints:
        - 1 <= s.length <= 10^4
        - s consists only of the characters '()[]{}'

    Notes:
        - The brute-force approach is simple but inefficient because repeated
          string replacements require multiple passes.
        - The stack approach is the standard optimal solution with linear time.
    """


    def valid_parentheses_brute_force(self, s: str) -> bool:
        """
        Intuition:
            A valid pair of brackets can always be removed without affecting
            the validity of the remaining string. Repeatedly eliminate the
            pairs '()', '{}', and '[]'. If the entire string disappears, the
            parentheses were valid; otherwise, unmatched or incorrectly ordered
            brackets remain.

        Algorithm:
            1. While the string contains any valid adjacent bracket pair:
                - Remove every occurrence of "()".
                - Remove every occurrence of "{}".
                - Remove every occurrence of "[]".
            2. After no more removals are possible, return whether the string
               is empty.

        Time:
            O(n^2)

        Space:
            O(n)
        """

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')

        return s == ''


    def valid_parentheses_stack(self, s: str) -> bool:
        """
        Intuition:
            The most recently opened bracket must be the first one to close,
            making this problem naturally suited for a stack (Last-In,
            First-Out).

        Algorithm:
            1. Maintain a stack to store opening brackets.
            2. Traverse the string one character at a time.
            3. If the current character is an opening bracket, push it onto
               the stack.
            4. If it is a closing bracket:
                - Ensure the stack is not empty.
                - Verify that the top of the stack is the matching opening
                  bracket.
                - If it matches, pop it; otherwise, return False.
            5. After processing all characters, return True only if the stack
               is empty.

        Time:
            O(n)

        Space:
            O(n)
        """

        st = []
        brackets = {'}': '{', ']': '[', ')': '('}

        for ch in s:
            if ch in brackets:
                if st and st[-1] == brackets[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)

        return True if not st else False



if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (s: str, expected)
        ("()", True),
        ("()[]{}", True),
        ("(])", False),
        ("([])", True),
        ("([)]", False),
        ("[", False),
        (")", False),
    ]

    for s, expected in test_cases:
        result = solution.valid_parentheses_stack(s)

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