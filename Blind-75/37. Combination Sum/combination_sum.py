class Solution:
    """
    Problem:
        Given an array of distinct positive integers `candidates` and a target
        integer `target`, return all unique combinations of candidates whose
        values sum to `target`.

        Each candidate may be chosen an unlimited number of times. A combination
        is considered unique when the frequency of at least one chosen number
        differs from another combination.

    Approach:
        1. Use backtracking to explore possible combinations of candidates.
        2. At each step, either include the current candidate or move to the
           next candidate.
        3. When the running sum equals `target`, add a copy of the current
           combination to the result.
        4. Stop exploring a path when the running sum exceeds `target` or when
           all candidates have been considered.

    Constraints:
        - 1 <= candidates.length <= 30
        - 2 <= candidates[i] <= 40
        - All elements of candidates are distinct.
        - 1 <= target <= 40
        - Each candidate may be used an unlimited number of times.
        - The number of valid unique combinations is less than 150.

    Notes:
        - Candidates contain only positive integers, so any path whose sum
          exceeds the target can be safely pruned.
        - Keeping the index the same allows the current candidate to be reused.
        - Moving to the next index ensures combinations are generated without
          considering different permutations as separate results.
    """

    def combination_sum_backtrack(self, candidates: list[int], target: int):
        """
        Find all unique combinations using binary decision backtracking.

        Intuition:
            For every candidate, we have two choices:
            1. Include the current candidate and remain at the same index,
               allowing it to be used again.
            2. Skip the current candidate and move to the next index.

            By only moving forward through the candidates when skipping, we
            avoid generating duplicate permutations such as [2, 3] and [3, 2].

        Algorithm:
            1. Start backtracking from index 0 with an empty combination and
               a total of 0.
            2. If the total equals the target, add a copy of the current
               combination to the result.
            3. If the total exceeds the target or all candidates have been
               processed, stop exploring the current path.
            4. Include candidates[i], recurse with the same index, then
               backtrack by removing it.
            5. Skip candidates[i] and recurse with the next index.

        Time:
            O(2^(t / m)), where t is the target and m is the minimum candidate
            value. The exact complexity depends on the number of valid and
            explored combinations.

        Space:
            O(t / m) auxiliary space for the recursion stack and current
            combination, excluding the output.
        """

        res = []

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])

            curr.pop()
            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)
        return res


    def combination_sum_backtrack_optimal(self, candidates: list[int], target: int):
        """
        Find all unique combinations using optimized backtracking with pruning.

        Intuition:
            Instead of making an explicit include-or-skip decision for every
            candidate, iterate through all candidates starting from the current
            index.

            The candidates are sorted first. This allows us to stop exploring
            as soon as adding a candidate would exceed the target, because every
            following candidate will be at least as large.

            Passing `j` instead of `j + 1` into the recursive call allows the
            same candidate to be selected multiple times. Starting each loop at
            index `i` ensures that candidates are chosen in non-decreasing
            order, preventing duplicate combinations.

        Algorithm:
            1. Sort the candidates to enable early pruning.
            2. Start backtracking with an empty combination and total 0.
            3. Iterate through candidates starting at index `i`.
            4. If adding candidates[j] exceeds the target, stop the loop because
               all remaining candidates are greater than or equal to it.
            5. Add candidates[j] to the current combination.
            6. Recurse starting from index `j` so the same candidate can be
               used again.
            7. Remove the candidate after returning to explore the next choice.
            8. When the total equals the target, store a copy of the current
               combination.

        Time:
            O(2^(t / m)), where t is the target and m is the minimum candidate
            value. Sorting adds O(n log n), but the backtracking search
            dominates the overall complexity.

        Space:
            O(t / m) auxiliary space for the recursion stack and current
            combination, excluding the output. The maximum depth occurs when
            the smallest candidate is repeatedly chosen.
        """

        res = []
        candidates.sort()

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break
                curr.append(candidates[j])
                backtrack(j, curr, total + candidates[j])
                curr.pop()

        backtrack(0, [], 0)
        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], target: int, expected: list[list[int]])
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
    ]

    for candidates, target, expected in test_cases:
        result = solution.combination_sum_backtrack_optimal(candidates, target)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"candidates = {candidates}\n"
            f"target = {target}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"candidates = {candidates}\n"
            f"target = {target}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")