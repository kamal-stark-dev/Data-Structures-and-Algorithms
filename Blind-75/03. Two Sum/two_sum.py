class Solution:
    """
    This class contains various approaches to solve the two sum problem in which you need to return indices of numbers who's sum is equal to the given target.

    Inputs: arrray of integer `nums` and integer `target`
    Output: return indices of two numbers such that they add upto `target` (can't use the same index twice)
    """

    def two_sum_brute_force(self, nums: list[int], target: int) -> list[int]:
        """
        Brute force approach: iterating over nums and checking if (target - current_num) exists in the nums array.

        Time: O(n^2)
        Space: O(1)
        """

        for i in range(len(nums)):
            rem = target - nums[i]

            for j in range(i + 1, len(nums)):
                if rem == nums[j]:
                    return [i, j]

        return [-1, -1]


    def two_sum_sorting(self, nums: list[int], target: int) -> list[int]:
        """
        Sorting approach: sorting the nums array and then setting left as first index and right as last index then returning left and right if their sum is equal to target and increasing left if sum is less, decreasing right if sum is greater than target.

        Time: O(n logn)
        Space: O(n)
        """

        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            sum = A[left][0] + A[right][0]

            if sum == target:
                return [A[left][1], A[right][1]]
            elif sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]


    def two_sum_hash_map_two_pass(self, nums: list[int], target: int) -> list[int]:
        """
        Hash map approach: the logic is same as brute force approach but using a hash map for fast lookup, making it linear time complexity. First building the hash map and then looking for remaining (target - num) in the hash set.

        Time: O(n)
        Space: O(n)
        """

        seen = dict() # key: nums[idx], value: idx

        for i, num in enumerate(nums):
            seen[num] = i

        for i, num in enumerate(nums):
            rem = target - num

            if rem in seen and seen[rem] != i: # Note: we need `seem[rem] != i` for cases where (nums[i] * 2 == target)
                return [i, seen[rem]]

        return [-1, -1]


    def two_sum_hash_map(self, nums: list[int], target: int) -> list[int]:
        """
        Hash map approach: the logic is same as brute force approach but using a hash map for fast lookup, making it linear time complexity.

        Time: O(n)
        Space: O(n)
        """

        seen = dict() # key: nums[idx], value: idx

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in seen:
                return [i, seen[rem]]
            else:
                seen[nums[i]] = i

        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([2, 3, 1], 4, [1, 2])
    ]

    for nums, target, expected in test_cases:
        result = solution.two_sum_hash_map_two_pass(nums, target)
        print(result)

        # sorting cause the indices might be shuffled but may still be valid, sorting expected to make sure the expected output is also sorted
        assert sorted(result) == sorted(expected)

        print(
            f"nums = {nums}, target = {target}\n"
            f"got = {result}, expected = {expected}\n"
        )

    print("#######################\nAll test cases passed!!\n#######################")
