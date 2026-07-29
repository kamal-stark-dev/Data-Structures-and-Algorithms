from collections import defaultdict

class Solution:
    """
    Given an array of `strs`, group the anagrams together and return that.

    Input: list[str]
    Output: list[list[str]]

    Constraints:
        1 <= strs.length <= 10^4
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters
    """

    def group_anagrams_sorting(self, strs: list[str]) -> list[list[str]]:
        """
        Given an array of `strs`, group the anagrams together by sorting each string and using that as a key to append that string to the map and return the values.

        Time: O(m * n logn)
        Space: O(m * n)

        m = number of strings
        n = length of the longest string
        """

        res = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            res[sorted_s].append(s)

        return list(res.values())


    def group_anagrams_hash_set(self, strs: list[str]) -> list[list[str]]:
        """
        Given an array of `strs`, group the anagrams together by creating a count array (of size 26 as only lowercase English letters are there) and use the tuple(count) as the key to build a map.

        Time: O(m * n)
        Space: O(m) auxilary space excluding the output, O(m * n) total space

        m = number of strings
        n = length of the longest string
        """

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ]

    for strs, expected in test_cases:
        result = solution.group_anagrams_hash_set(strs)

        normalized_result = sorted([sorted(group) for group in result])
        expected_result = sorted([sorted(group) for group in expected])

        assert normalized_result == expected_result

        print(
            f"strs = {strs}\n"
            f"got = {result}, expected = {expected}\n"
        )

    print("#######################\nAll test cases passed!!\n#######################")
