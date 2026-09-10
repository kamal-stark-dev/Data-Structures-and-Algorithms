class TrieNode:
    """
    Represents a single node in a Trie data structure.

    Attributes:
        children (dict): Maps each character to its corresponding TrieNode.
        endOfWord (bool): Indicates whether this node marks the end of a
            complete word.
    """

    def __init__(self) -> None:
        """Initialize an empty Trie node."""
        self.children = dict()
        self.endOfWord = False


class Trie:
    """
    Implements a Trie (Prefix Tree) for storing and searching strings.

    A Trie stores words character by character, allowing efficient
    whole-word searches and prefix searches.

    Operations:
        insert(word): Inserts a word into the Trie.
        search(word): Checks whether a complete word exists in the Trie.
        startsWith(prefix): Checks whether any word starts with a prefix.
    """

    def __init__(self) -> None:
        """Initialize an empty Trie with a root node."""
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Each character is stored as a node in the Trie. If a character
        does not already exist, a new TrieNode is created.

        Args:
            word: The string to insert into the Trie.

        Time:
            O(L), where L is the length of the word.

        Space:
            O(L) in the worst case for newly created nodes.
        """
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.endOfWord = True


    def search(self, word: str) -> bool:
        """
        Check whether a complete word exists in the Trie.

        The method traverses the Trie character by character. The word
        exists only if every character is found and the final node is
        marked as the end of a word.

        Args:
            word: The string to search for.

        Returns:
            True if the complete word exists, otherwise False.

        Time:
            O(L), where L is the length of the word.

        Space:
            O(1) auxiliary space.
        """
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]

        return curr.endOfWord


    def startsWith(self, prefix: str) -> bool:
        """
        Check whether any word in the Trie starts with a given prefix.

        The method only needs to successfully traverse all characters
        of the prefix. The final node does not need to mark the end of
        a complete word.

        Args:
            prefix: The prefix to search for.

        Returns:
            True if at least one word starts with the prefix,
            otherwise False.

        Time:
            O(P), where P is the length of the prefix.

        Space:
            O(1) auxiliary space.
        """
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]

        return True

class Solution:
    """
    Provides a wrapper for executing a sequence of Trie operations.

    Problem:
        Implement a Trie that supports insertion, whole-word search,
        and prefix search.

    Approach:
        1. Initialize an empty Trie.
        2. Process each operation in the given order.
        3. Execute insert, search, or startsWith accordingly and store
           the result of each operation.

    Constraints:
        Each operation processes a string character by character.
        The implementation supports arbitrary strings accepted by
        Python's dictionary keys.

    Notes:
        The "insert" operation returns None, while "search" and
        "startsWith" return boolean values.
    """

    def implement_trie(
        self,
        calls: list[str],
        inputs: list[list[str]]
    ) -> list[bool | None]:
        """
        Execute a sequence of Trie operations.

        Intuition:
            The input describes a sequence of operations to perform on
            a single Trie instance. We maintain one Trie and process
            each operation in order, collecting its output.

        Algorithm:
            1. Create an empty Trie.
            2. Iterate through `calls` and `inputs` simultaneously.
            3. For "insert", add the given word to the Trie.
            4. For "search", check whether the given word exists.
            5. For "startsWith", check whether the given prefix exists.
            6. Append the operation's result to the result list.

        Args:
            calls: A list containing operation names such as "insert",
                "search", and "startsWith".
            inputs: A list of argument lists corresponding to each
                operation in `calls`.

        Returns:
            A list containing None for insert operations and boolean
            results for search and startsWith operations.

        Time:
            O(sum of the lengths of all input strings).

        Space:
            O(N), where N is the total number of characters stored in
            the Trie, excluding the output list.
        """

        res: list[bool | None] = []
        trie = Trie()

        for call, input in zip(calls, inputs):
            output = None

            if call == "insert":
                trie.insert(input[0])
            elif call == "search":
                output = trie.search(input[0])
            elif call == "startsWith":
                output = trie.startsWith(input[0])

            res.append(output)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (calls: lst[str], inputs: list[list[str]], expected: list[bool | None])
        (
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True]
        ),
    ]

    for calls, inputs, expected in test_cases:
        result = solution.implement_trie(calls, inputs)

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