from collections import defaultdict

class Solution:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Solution should not contain any duplicate values.

    Constraints:
        3 <= nums.length <= 3000
        -10^5 <= nums[i] <= 10^5
    """

    def three_sum_brute_force(self, nums: list[int]) -> list[list[int]]:
        """
        Find all unique triplets whose sum is zero using brute force.

        This method checks every possible combination of three different
        indices in the array. Whenever a triplet sums to zero, it is sorted
        and stored in a set to avoid duplicate results.

        Time: O(n^3)
        Space: O(1) or O(m), where m is the number of triplets
        """

        res = set()

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                for k in range(len(nums)):
                    if i == k or j == k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return [list(item) for item in res]


    def three_sum_hash_map(self, nums: list[int]) -> list[list[int]]:
        """
        Find all unique triplets whose sum is zero using sorting and a
        frequency hash map.

        The array is first sorted so duplicate values can be skipped.
        A frequency map keeps track of how many occurrences of each number
        are still available. For every pair of numbers, the required third
        value is computed and looked up in the hash map.

        Duplicate first and second elements are skipped to ensure each
        triplet is returned only once.

        Time: O(n^2)
        Space: O(n) for the hash map
        """

        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip duplicate elements

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1

                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue

                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1

        return res


    def three_sum_two_pointers(self, nums: list[int]) -> list[list[int]]:
        """
        Find all unique triplets whose sum is zero using the two-pointer
        technique.

        After sorting the array, each element is treated as the first
        number of a potential triplet. Two pointers then search the
        remaining portion of the array for two numbers whose sum equals
        the negative of the currently selected elements.

        Duplicate values are skipped to prevent duplicate triplets from
        being added to the result.

        Time: O(n^2)
        Space: O(1) or O(n) depending on sorting algorithm and O(m) for output list where m is the number of triplets
        """

        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: # skip same numbers on the left
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: # skip same numbers on the right
                        right -= 1

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 0, 0, 2, 2], [[-2, 0, 2], [0, 0, 0]])
    ]

    for nums, expected in test_cases:
        result = solution.three_sum_hash_map(nums)
        print("result:", result)

        assert sorted(result) == sorted(expected)

        print(
            f"nums = {nums}\n"
            f"got = {result}, expected = {expected}\n"
        )

    print("#######################\nAll test cases passed!!\n#######################")