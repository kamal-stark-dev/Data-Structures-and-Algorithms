class Solution:
    """
    Encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

    Encode: converting a list of strings into an encoded string
    Decode: an encoded string is decoded back to it's original form

    Constraints:
        0 <= strs.length < 100
        0 <= strs[i].length < 200
        strs[i] contains any characters from 256 valid ASCII characters
    """

    def encode_my_approach(self, strs: list[str]) -> str:
        """
        Encoding a list of strings into an encoded string using a special delimiter
        character ('∏') that is assumed to never appear in the input strings (as given in constraints).

        Example:
            ["Hello", "World", ""]

        becomes:

            "Hello∏World∏∏"

        Note:
            This approach is only valid if the delimiter character is guaranteed
            to never appear in any input string.

        Time: O(L + n)
        Space: O(L + n)

        where:
            n = number of strings
            L = total number of characters across all strings
        """

        encoded = []

        for s in strs:
            encoded.append(s) # Note: using encoded += s repeatedly creates new strings, making worst-case O(L^2), that's why we used lists instead
            encoded.append("∏")

        return "".join(encoded)


    def decode_my_approach(self, s: str) -> list[str]:
        """
        Decoding an encoded string by splitting it whenever the special delimiter
        character ('∏') is encountered, reconstructing the original list of
        strings.

        Example:
            "Hello∏World∏∏"

        becomes:

            ["Hello", "World", ""]

        Note:
            This approach assumes the delimiter character never appears inside any
            original string.

        Time: O(L + n)
        Space: O(L + n)

        where:
            n = number of decoded strings
            L = total number of characters across all strings
        """

        decoded = []

        word = []
        for ch in s:
            if ch == "∏":
                decoded.append("".join(word))
                word = []
            else:
                word.append(ch) # Note: using word += ch repeatedly creates new strings, making worst-case O(L^2), that's why we used lists instead

        return decoded


    def encode_using_size(self, strs: list[str]) -> str:
        """
        Encoding a list of strings by first storing the length of every string,
        separated by commas, followed by a '#' delimiter, and finally concatenating
        all strings together.

        Example:
            ["cat", "dog", ""]

        becomes:

            "3,3,0,#catdog"

        Time: O(L + n)
        Space: O(L + n)

        where:
            n = number of strings
            L = total number of characters across all strings
        """

        if not strs:
            return ""

        encoded = []

        for s in strs:
            encoded.append(str(len(s)) + ",")
        encoded.append("#")

        for s in strs:
            encoded.append(s)

        return "".join(encoded)


    def decode_using_size(self, s: str) -> list[str]:
        """
        Decoding an encoded string by first reading the comma-separated list of
        string lengths until the '#' delimiter is reached, then reconstructing
        each original string using its stored length.

        Time: O(L + n)
        Space: O(L + n)

        where:
            n = number of decoded strings
            L = total number of characters across all strings
        """

        if not s:
            return []

        sizes = []

        i = 0
        while s[i] != "#":
            curr = ""
            while s[i] != ",":
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            i += 1
        i += 1 # skip the # character

        decoded = []
        for size in sizes:
            decoded.append(s[i: i + size])
            i += size

        return decoded


    def encode_optimal(self, strs: list[str]) -> str:
        """
        Encoding a list of strings by prefixing each string with its length,
        followed by a '#' delimiter.

        Example:
            ["cat", "dog", ""]

        becomes:

            "3#cat3#dog0#"

        This approach stores each string's length immediately before the string,
        allowing decoding in a single pass without separately storing all lengths.

        Time: O(L + n)
        Space: O(L + n)

        where:
            n = number of strings
            L = total number of characters across all strings
        """

        encoded = []

        for s in strs:
            encoded.append(str(len(s)) + "#" + s)

        return "".join(encoded)


    def decode_optimal(self, s: str) -> list[str]:
        """
        Decoding an encoded string by reading the length prefix until the '#'
        delimiter, then extracting exactly that many characters as the next
        original string. This process repeats until the end of the encoded string.

        Time: O(L + n)
        Space: O(L + n)

        where:
            n = number of decoded strings
            L = total number of characters across all strings
        """

        decoded = []

        i = 0
        while i < len(s):
            curr = ""
            while s[i] != '#':
                curr += s[i]
                i += 1
            size = int(curr)

            i += 1
            j = i + size
            decoded.append(s[i: j])
            i = j

        return decoded


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["Hello", "World"], ["Hello", "World"]),
        ([""], [""]),
        (["Encode", "and", "decode", "strings"], ["Encode", "and", "decode", "strings"]),
        (["Bye", "World", ""], ["Bye", "World", ""])
    ]

    for strs, expected in test_cases:
        encoded = solution.encode_optimal(strs)

        result = solution.decode_optimal(encoded)

        print(
            f"Encoded = {encoded}\n"
            f"Decoded = {result}\n"
        )

        assert result == expected

        print(
            f"strs = {strs}\n"
            f"got = {result}, expected = {expected}\n"
        )

    print("#######################\nAll test cases passed!!\n#######################")