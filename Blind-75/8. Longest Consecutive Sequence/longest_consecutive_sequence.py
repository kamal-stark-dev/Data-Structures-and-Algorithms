from collections import defaultdict

class Solution:
    """
    Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

    A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

    NOTE: You must write an algorithm that runs in O(n) time. So, only the `hash_set` and `hash_map` solutions are valid.

    Constraints:
        0 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
    """

    def longest_consecutive_brute_force(self, nums: list[int]) -> int:
        """
        Find the longest consecutive sequence by treating every number as a
        potential starting point and repeatedly checking for the next number.

        This approach performs redundant work because the same sequences may be
        traversed multiple times.

        Time: O(n^2)
        Space: O(n) for `seen` set
        """

        longest = 0
        seen = set(nums)

        for num in nums:
            length = 0
            curr = num
            while curr in seen:
                curr += 1
                length += 1
            longest = max(length, longest)

        return longest


    def longest_consecutive_sorting(self, nums: list[int]) -> int:
        """
        Sort the array and scan it once to count consecutive runs.

        Duplicates are skipped since they do not extend a sequence.

        Time: O(n logn)
        Space: O(1) or O(n) depending on sorting algorithm
        """

        longest = 0
        sorted_nums = sorted(nums)

        length = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                length += 1
                longest = max(length, longest)
            elif sorted_nums[i] == sorted_nums[i - 1]:
                continue # skip duplicates
            else:
                length = 1

        return longest


    def longest_consecutive_hash_set(self, nums: list[int]) -> int:
        """
        Store all numbers in a hash set and only begin counting from numbers
        that are the start of a sequence (i.e., num - 1 is absent).

        Each sequence is traversed exactly once, giving linear time complexity.

        Time: O(n)
        Space: O(n)
        """

        longest = 0
        seen = set(nums)

        for num in seen:
            if (num - 1) not in seen:
                length = 1
                while (num + length) in seen:
                    length += 1
                longest = max(length, longest)

        return longest


    def longest_consecutive_hash_map(self, nums: list[int]) -> int:
        """
        Maintain the length of each consecutive sequence using a hash map.

        For each new number, merge the consecutive sequences on its left and
        right (if they exist), compute the new sequence length, and update only
        the sequence boundaries. Duplicate values are ignored.

        Time: O(n)
        Space: O(n)
        """

        longest = 0
        mp = defaultdict(int)

        for num in nums:
            if not mp[num]: # skip duplicates
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                # update left boundary
                mp[num - mp[num - 1]] = mp[num]
                # update right boundary
                mp[num + mp[num + 1]] = mp[num]

                longest = max(mp[num], longest)

        return longest



if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3)
    ]

    for nums, expected in test_cases:
        result = solution.longest_consecutive_hash_map(nums)

        assert result == expected

        print(
            f"nums = {nums}\n"
            f"got = {result}, expected = {expected}\n"
        )

    print("#######################\nAll test cases passed!!\n#######################")
