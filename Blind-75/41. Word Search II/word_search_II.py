class TrieNode:
    """
    Represents a single node in a Trie.

    Each node stores:
        - children: Mapping from a character to the next TrieNode.
        - endOfWord: True if a complete word ends at this node.
    """

    def __init__(self):
        self.children = dict()
        self.endOfWord = False


class Trie:
    """
    Trie data structure used to store all words.

    A Trie allows the backtracking search to determine in O(1) average
    time whether the current sequence of characters can be a prefix of
    any word we are looking for.
    """

    def __init__(self):
        self.root = TrieNode()

    def addWords(self, words: list[str]) -> None:
        """
        Inserts every word into the Trie.

        Each character represents one edge in the Trie. Once all
        characters of a word have been inserted, the final node is
        marked as the end of a complete word.

        Args:
            words: List of words to insert into the Trie.

        Time:
            O(S), where S is the total number of characters across
            all words.

        Space:
            O(S) in the worst case, for the Trie nodes.
        """

        for word in words:
            curr = self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.endOfWord = True


class Solution:
    """
    Problem:
        Given an m x n board of lowercase English characters and a list
        of words, return all words that can be constructed from the board.

        A word is constructed using horizontally or vertically adjacent
        cells. The same cell cannot be used more than once for the same
        word.

    Approach:
        1. Brute force:
           Search for every word independently using DFS/backtracking.

        2. Trie + backtracking:
           Insert all words into a Trie and perform DFS from every board
           cell. The Trie allows us to stop exploring as soon as the
           current character sequence is not a prefix of any word.

        3. During Trie-based backtracking, mark visited board cells
           temporarily and restore them after exploring the current path.

    Constraints:
        - 1 <= m, n <= 12
        - 1 <= len(words) <= 3 * 10^4
        - 1 <= len(words[i]) <= 10
        - All board characters and word characters are lowercase English
          letters.
        - All words are unique.

    Notes:
        - Trie significantly reduces unnecessary DFS exploration because
          paths that cannot form a prefix of any word are immediately
          discarded.
        - Once a complete word is found, endOfWord is set to False so the
          same word is not added to the result multiple times.
    """

    def word_search_II_brute(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Finds all words using DFS/backtracking independently for each word.

        Intuition:
            For each word, try starting the search from every cell that
            contains the first character of the word. From that cell,
            recursively explore the four possible directions.

            A cell cannot be reused within the same path, so the current
            cell is temporarily marked as visited during DFS and restored
            afterward.

        Algorithm:
            1. Iterate through every word.
            2. For each word, scan every cell in the board.
            3. If the cell matches the first character, start a DFS.
            4. During DFS:
               - Stop if the position is outside the board.
               - Stop if the cell does not match the required character.
               - Mark the current cell as visited.
               - Recursively search in all four directions.
               - Restore the cell before returning.
            5. If a complete word is found, add it to the result.
            6. Return all words that were found.

        Time:
            O(W * M * N * 4^L), where:
                - W = number of words,
                - M = number of rows,
                - N = number of columns,
                - L = maximum word length.

            For every word, we may start a DFS from every board cell.
            Each DFS can explore up to four directions at each level.

        Space:
            O(L) auxiliary space for the DFS recursion stack, where L is
            the maximum length of a word.

            The board is modified in-place for visited tracking and then
            restored.
        """

        n, m = len(board), len(board[0])
        res = []

        def backtrack(i, j, idx, word):
            if idx == len(word):
                return True

            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != word[idx]:
                return False

            board[i][j] = "$"

            res = (
                backtrack(i + 1, j, idx + 1, word) or
                backtrack(i, j + 1, idx + 1, word) or
                backtrack(i - 1, j, idx + 1, word) or
                backtrack(i, j - 1, idx + 1, word)
            )

            board[i][j] = word[idx]
            return res

        for word in words:
            flag = False

            for i in range(n):
                for j in range(m):
                    if board[i][j] != word[0]:
                        continue
                    if backtrack(i, j, 0, word):
                        res.append(word)
                        flag = True
                        break
                if flag:
                    break

        return res

    def word_search_II_trie_and_backtracking(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Finds all words using a Trie combined with DFS/backtracking.

        Intuition:
            Searching every word independently wastes work because many
            words can share the same prefixes.

            For example, if the words are ["oath", "oak", "oar"], the
            prefixes "o", "oa", and "oa..." are shared. A Trie stores these
            prefixes once, allowing the board search to explore a path only
            while that path is a valid prefix of at least one word.

            This combines the Trie prefix search with DFS/backtracking over
            the board.

        Algorithm:
            1. Insert every word into a Trie.
            2. Start DFS/backtracking from every cell in the board.
            3. At each cell:
               - Stop if the cell is outside the board.
               - Stop if the cell has already been visited.
               - Stop if the current character does not exist as a child
                 of the current Trie node.
            4. Move to the corresponding Trie child and append the
               character to the current word.
            5. If the Trie node represents the end of a word, add that
               word to the result.
            6. Set endOfWord to False after finding a word so duplicate
               paths do not add the same word multiple times.
            7. Temporarily mark the current board cell as visited.
            8. Recursively explore all four neighboring cells.
            9. Restore the board cell after exploring all directions.
            10. Return the collected words.

        Time:
            Let S be the total number of characters across all words and
            L be the maximum word length.

            Building the Trie takes O(S).

            The board traversal is bounded by the number of possible
            backtracking paths, but Trie prefix pruning eliminates paths
            that cannot correspond to any word.

            A commonly used upper-bound description is
            O(M * N * 4^L), with additional pruning from the Trie.

        Space:
            O(S + L), where:
                - O(S) is used by the Trie,
                - O(L) is used by the recursion stack.

            The board is modified in-place to mark visited cells.
        """

        def backtrack(i: int, j: int, curr: str, trieNode: TrieNode, board: list[list[str]], res: list[str]) -> None:
            n, m = len(board), len(board[0])
            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] == "$" or board[i][j] not in trieNode.children:
                return

            ch = board[i][j]
            curr += ch
            trieNode = trieNode.children[ch]

            if trieNode.endOfWord:
                res.append(curr)
                trieNode.endOfWord = False # so that the same word isn't visited again

            board[i][j] = "$"

            backtrack(i + 1, j, curr, trieNode, board, res)
            backtrack(i, j + 1, curr, trieNode, board, res)
            backtrack(i - 1, j, curr, trieNode, board, res)
            backtrack(i, j - 1, curr, trieNode, board, res)

            board[i][j] = ch

        trie = Trie()
        trie.addWords(words)

        res = []
        n, m = len(board), len(board[0])

        for i in range(n):
            for j in range(m):
                backtrack(i, j, "", trie.root, board, res)

                if len(res) == len(words):
                    return res

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (board: list[list[str]], words: list[str], expected: list[str])
        (
            [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
            ["oath","pea","eat","rain"],
            ["eat","oath"]
        ),
        (
            [["a","b"],["c","d"]],
            ["abcb"],
            []
        ),
    ]

    for board, words, expected in test_cases:
        result = solution.word_search_II_trie_and_backtracking(board, words)

        assert sorted(result) == sorted(expected), (
            f"\n\nTest case failed!\n"
            f"board = {board}\n"
            f"words = {words}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"board = {board}\n"
            f"words = {words}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")