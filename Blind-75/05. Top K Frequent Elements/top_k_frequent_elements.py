import heapq
from collections import Counter

class Solution:
    """
    Given an integer array nums and an integer k, return the k most frequent elements.

    Input: list[int], int
    Output: list[int]

    Constraints
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.
    """


    def topKFrequent_sorting(self, nums: list[int], k: int) -> list[int]:
        """
        Return top k most frequent elements by building a frequency array, sorting it in descending order and return the first k elements.

        Time: O(n logn)
        Space: O(n), for freq and res (output)
        """
        freq = dict()

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        res = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in res[:k]]


    def topKFrequent_min_heap(self, nums: list[int], k: int) -> list[int]:
        """
        Return the top k elements by creating a min-heap of len `k`, we push frequencies to it and if the len goes beyond k then popping out of the heap so that k most frequent elements are evaluated.

        Time: O(n logk), k in worst case can be equal to n
        Space: O(n + k), n for counter and k for heap
        """

        heap = []
        counter = Counter(nums) # you can use a Counter or build your own counter like we did above

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [h[1] for h in heap]


    def topKFrequent_bucked_sort(self, nums: list[int], k: int) -> list[int]:
        """
        Return the top k elements by creating a count arary which store the list of nums that occurs i (index) times in the nums array and then traversing it backwards are returning the first k elements encountered.

        Time: O(n)
        Space: O(n), for count, freq and topK (result)
        """

        count = [[] for _ in range(len(nums) + 1)]

        freq = Counter(nums)

        for num, cnt in freq.items():
            count[cnt].append(num)

        topK = []
        for i in range(len(nums), 0, -1):
            for item in count[i]:
                topK.append(item)
                if len(topK) == k:
                    return topK


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,1,1,2,2,3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1,2,1,2,1,2,3,1,3,2], 2, [1, 2]),
    ]

    for nums, k, expected in test_cases:
        result = solution.topKFrequent_bucked_sort(nums, k)

        assert sorted(result) == sorted(expected)

        print(
            f"nums = {nums}, k = {k}\n"
            f"got = {result}, expected = {expected}\n"
        )

    print("#######################\nAll test cases passed!!\n#######################")