class TrieNode:
    """
    A node in the Trie.

    Each node stores:
        - children: Mapping from a character to the next TrieNode.
        - endOfWord: True if a complete word ends at this node.
    """

    def __init__(self):
        self.children = dict()
        self.endOfWord = False


class WordDictionary:
    """
    Trie-based data structure that supports adding words and searching
    for words containing '.' as a wildcard character.
    """

    def __init__(self):
        """
        Intuition:
            - A Trie stores words character-by-character, allowing us to
              efficiently traverse a word one character at a time.
            - Each node marks whether a complete word ends at that node.

        Algorithm:
            - Create an empty TrieNode and use it as the root of the Trie.

        Time:
            O(1)

        Space:
            O(1)
        """

        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Intuition:
            - Insert the word into the Trie one character at a time.
            - If a character does not have a corresponding child node,
              create one.
            - Mark the final node as the end of a complete word.

        Algorithm:
            1. Start at the root of the Trie.
            2. For every character in the word:
               - Create a child node if the character does not exist.
               - Move to the corresponding child node.
            3. After processing all characters, mark the current node
               as the end of a word.

        Time:
            O(L), where L is the length of the word.

        Space:
            O(L) in the worst case for newly created Trie nodes.
        """

        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

    def _search_helper(self, idx: int, node: TrieNode, word: str) -> bool:
        """
        Intuition:
            - Normal characters have exactly one possible path in the Trie.
            - A '.' can represent any lowercase letter, so we must try every
              child of the current node.
            - This creates multiple possible paths, so use DFS/backtracking.
            - If any path successfully matches the remaining characters,
              the search succeeds.

        Algorithm:
            1. Start from the given Trie node at index `idx` in `word`.
            2. For each character:
               - If it is a normal character:
                   * Follow the corresponding child.
                   * If the child does not exist, return False.
               - If it is '.':
                   * Try recursively searching through every child.
                   * Return True as soon as one path succeeds.
                   * If no child produces a match, return False.
            3. After processing the entire word, return whether the current
               Trie node represents the end of a previously added word.

        Time:
            O(26^D * L), where:
                - L is the length of the search word.
                - D is the number of '.' characters.
              Each '.' may branch to at most 26 children.

        Space:
            O(L) for the recursion stack in the worst case.
        """

        curr = node

        for i in range(idx, len(word)):
            c = word[i]

            if c == '.':
                for ch in curr.children:
                    if self._search_helper(i + 1, curr.children[ch], word):
                        return True
                return False

            if c not in curr.children:
                return False

            curr = curr.children[c]

        return curr.endOfWord

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.

        A '.' character acts as a wildcard and can match any single letter.

        Time:
            O(26^D * L), where L is the word length and D is the number
            of wildcard characters.

        Space:
            O(L) for the recursion stack.
        """

        return self._search_helper(0, self.root, word)


class Solution:
    """
    Problem:
        Design a data structure that supports adding words and searching
        for previously added words. During search, '.' can represent any
        single lowercase English letter.

    Approach:
        1. Use a Trie to store all words character-by-character.
        2. For addWord, traverse/create Trie nodes for each character and
           mark the final node as the end of the word.
        3. For search, traverse normally for alphabetic characters.
           When '.' is encountered, perform DFS over all possible child
           nodes and return True if any path forms a complete matching word.

    Constraints:
        - 1 <= word.length <= 25
        - Words contain lowercase English letters when added.
        - Search words contain lowercase English letters or '.'.
        - A search word contains at most 2 dots.
        - At most 10^4 addWord/search calls are made.

    Notes:
        - The Trie avoids scanning every previously added word during search.
        - The wildcard '.' is the only part that requires branching.
        - Since there are at most 2 dots, the branching factor is limited
          to at most 26^2 possible wildcard combinations.
    """

    def design_add_and_search_words(
        self,
        calls: list[str],
        inputs: list[list[str]]
    ) -> list[bool | None]:
        """
        Simulate the WordDictionary API using the provided sequence of calls.

        Intuition:
            - The input describes a sequence of operations that would normally
              be performed directly on a WordDictionary object.
            - Create one WordDictionary and execute each operation in order.
            - addWord does not return a value, so append None.
            - search returns a boolean, which is appended to the result list.

        Algorithm:
            1. Create an empty WordDictionary.
            2. Iterate through `calls` and `inputs` simultaneously.
            3. For "addWord":
               - Add the provided word to the Trie.
               - Append None to the result.
            4. For "search":
               - Search for the provided word.
               - Append the returned boolean to the result.
            5. Return the results in the same order as the input calls.

        Time:
            O(sum(L_add) + sum(26^D * L_search)), where:
                - L_add is the length of each word added.
                - L_search is the length of each searched word.
                - D is the number of '.' characters in a search word.

        Space:
            O(N * L) in the worst case for the Trie, where:
                - N is the number of words added.
                - L is the maximum word length.
              The result list additionally requires O(C) space, where C is
              the number of operations.
        """

        res: list[bool | None] = []
        trie = WordDictionary()

        for call, input in zip(calls, inputs):
            ouptut = None

            if call == "addWord":
                trie.addWord(input[0])
            elif call == "search":
                ouptut = trie.search(input[0])

            res.append(ouptut)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (calls: list[str], inputs: list[list[str]], expected: list[bool | None])
        (
            ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
            [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
            [None, None, None, None, False, True, True, True]
        ),
    ]

    for calls, inputs, expected in test_cases:
        result = solution.design_add_and_search_words(calls, inputs)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"calls = {calls}\n"
            f"inputs = {inputs}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"calls = {calls}\n"
            f"inputs = {inputs}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")