from collections import deque

class Solution:
    """
    Problem:
        - Given a list of words sorted according to an unknown alien alphabet,
          determine a valid ordering of the unique characters.
        - If the given dictionary is inconsistent and no valid character ordering
          exists, return an empty string.
        - If multiple valid orderings exist, return any one of them.

    Approach:
        1. Build a directed graph by comparing every pair of adjacent words.
           The first position where two words differ gives an ordering constraint:
           word1[idx] -> word2[idx].
        2. Handle the invalid prefix case. If word1 is longer than word2 but
           word2 is a prefix of word1, the dictionary cannot be valid.
        3. Find a topological ordering of the graph. A cycle means that the
           character constraints are contradictory, so return an empty string.

    Constraints:
        - 1 <= words.length <= 100
        - 1 <= words[i].length <= 100
        - words[i] contains only lowercase English letters.
        - Since the alphabet contains only 26 lowercase English letters, the
          number of graph nodes is at most 26.

    Notes:
        - Only the first different character between two adjacent words provides
          useful ordering information.
        - Duplicate edges must not increase indegree more than once.
        - Multiple valid character orderings may exist.
    """

    def alien_dictionary_dfs(self, words: list[str]) -> str:
        """
        Intuition:
            - Treat each unique character as a node in a directed graph.
            - When comparing two adjacent words, the first different characters
              determine their relative ordering.
            - For example, if "abc" comes before "axy", then 'b' must come
              before 'x', giving the edge b -> x.
            - A DFS topological sort can then produce a valid character ordering.
            - During DFS, a character can have three states:
                1. Not present in visited: not visited yet.
                2. True: currently being explored.
                3. False: completely processed.
            - Encountering a character marked True means we found a cycle,
              which means no valid alphabet ordering exists.
            - Characters are added to the result after all their neighbors have
              been processed, so reversing the result gives the topological order.

        Algorithm:
            1. Create an adjacency set for every unique character.
            2. Compare every pair of adjacent words.
            3. Find the first position where the two words differ and add a
               directed edge from the character in the first word to the
               character in the second word.
            4. If the first word is longer and the second word is its prefix,
               return "" because the dictionary ordering is invalid.
            5. Run DFS from every character.
            6. If DFS encounters a character that is currently being visited,
               a cycle exists, so return "".
            7. Add each character to the result after processing all of its
               neighbors.
            8. Reverse the result and return it.

        Time:
            O(N * L), where:
                - N = number of words.
                - L = maximum length of a word.
              Building the graph requires comparing adjacent words and may
              inspect up to L characters for each pair.
              DFS takes O(V + E), which is O(1) for the fixed 26-letter alphabet.

        Space:
            O(1) auxiliary space because the alphabet contains only 26 letters.
            More generally, for an alphabet of size K, the graph and DFS state
            require O(K + E) space.
        """

        def dfs(ch: str) -> bool:
            if ch in visited:
                return visited[ch]

            visited[ch] = True

            for nei in adj[ch]:
                if dfs(nei):
                    return True

            visited[ch] = False
            res.append(ch)

            return False

        adj = {ch: set() for word in words for ch in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""

            for idx in range(minLen):
                if word1[idx] != word2[idx]:
                    adj[word1[idx]].add(word2[idx])
                    break

        visited = {}
        res = []

        for ch in adj:
            if dfs(ch):
                # cycle detected
                return ""

        res.reverse()
        return "".join(res)

    def alien_dictionary_topological_sort(self, words: list[str]) -> str:
        """
        Intuition:
            - Model the unknown alphabet as a directed graph.
            - Each character is a node.
            - If character 'a' must appear before character 'b', create an edge
              a -> b.
            - The first different character between two adjacent words gives
              exactly this ordering constraint.
            - Once all constraints are represented as a graph, the problem
              becomes finding a topological ordering.
            - Kahn's algorithm performs topological sorting using indegrees and
              a queue of characters that currently have no prerequisites.

        Algorithm:
            1. Create an adjacency set for every unique character and initialize
               the indegree of every character to 0.
            2. Compare every pair of adjacent words.
            3. Find the first position where the words differ.
            4. Add an edge from the character in the first word to the character
               in the second word and increase the second character's indegree.
            5. Do not add duplicate edges because each edge should contribute
               only once to the indegree.
            6. If the first word is longer and the second word is its prefix,
               return "" because the dictionary is invalid.
            7. Add every character with indegree 0 to the queue.
            8. Repeatedly remove a character from the queue, add it to the
               result, and decrease the indegree of all its neighbors.
            9. Whenever a neighbor's indegree becomes 0, add it to the queue.
            10. If every character was processed, return the resulting
                topological ordering. Otherwise, a cycle exists, so return "".

        Time:
            O(N * L), where:
                - N = number of words.
                - L = maximum length of a word.
              Building the graph takes O(N * L).
              Topological sorting takes O(V + E), which is O(1) for the
              fixed 26-letter English alphabet.

        Space:
            O(1) auxiliary space because there are at most 26 unique lowercase
            English characters.
            More generally, for an alphabet of size K, the graph requires
            O(K + E) space.
        """

        adj = {ch: set() for word in words for ch in word}
        indegree = {ch: 0 for ch in adj}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""

            for idx in range(minLen):
                ch1 = word1[idx]
                ch2 = word2[idx]

                if ch1 != ch2:
                    if ch2 in adj[ch1]: # ch1 already points to ch2
                        break
                    adj[ch1].add(ch2)
                    indegree[ch2] += 1

        queue = deque([char for char in indegree if indegree[char] == 0])
        res = []

        while queue:
            char = queue.popleft()
            res.append(char)

            for nei in adj[char]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        if len(res) != len(adj):
            return ""

        return "".join(res)


def is_valid_order(words: list[str], order: str) -> bool:
    # 1. Every character must appear exactly once
    unique_chars = {ch for word in words for ch in word}

    if len(order) != len(unique_chars):
        return False

    if set(order) != unique_chars:
        return False

    # Map character -> position in the alien alphabet
    position = {
        ch: i
        for i, ch in enumerate(order)
    }

    # 2. Check every adjacent pair of words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]

        minLen = min(len(word1), len(word2))

        # find first different character
        for idx in range(minLen):
            if word1[idx] != word2[idx]:
                # word1[idx] must come before word2[idx]
                if position[word2[idx]] < position[word1[idx]]:
                    return False

                # first difference determines the ordering
                break

        else:
            # No difference found in the common prefix.
            # Therefore the shorter word must come first.
            if len(word1) > len(word2):
                return False

    return True

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (words: list[str], expected: str)
        (
            ["z", "o"],
            "zo"
        ),
        (
            ["hrn", "hrf", "er", "enn", "rfnn"],
            "hernf"
        ),
        (
            ["abc", "ab"],
            ""
        ),
        (
            ['x', 'y', 'x'], # contains cycle
            ""
        ),
    ]

    for words, expected in test_cases:
        result = solution.alien_dictionary_topological_sort(words)

        if expected == "":
            assert result == "", (
                f"\nExpected invalid dictionary!"
                f"\nwords = {words}"
                f"\ngot = '{result}'"
            )
        else:
            assert result != "", (
                f"\nExpected a valid ordering!"
                f"\nwords = {words}"
                f"\ngot = '{result}'"
            )

            assert is_valid_order(words, result), (
                f"\n\nTest case failed!\n"
                f"words = {words}\n"
                f"expected = '{expected}'\n"
                f"got = '{result}'\n"
            )

        print(
            f"words = {words}\n"
            f"expected = '{expected}'\n"
            f"got = '{result}'\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")