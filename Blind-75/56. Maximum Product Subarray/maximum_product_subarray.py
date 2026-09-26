class Solution:
    """
    Problem:
        Given an integer array nums, find a contiguous subarray that has
        the largest product and return that product.

    Approach:
        1. Brute Force:
            Enumerate every possible subarray and calculate its product.

        2. Sliding Window:
            Split the array around zeroes. For each zero-free segment,
            maintain a window with an even number of negative values so
            that the product is positive whenever possible.

        3. Kadane's Algorithm:
            Track both the maximum and minimum product ending at the
            current position because a negative number can turn the
            minimum product into the maximum.

        4. Prefix/Suffix:
            Maintain products while scanning from both the left and right.
            This handles negative values and zeroes without explicitly
            maintaining a window.

    Constraints:
        - 1 <= nums.length <= 2 * 10^4
        - -10 <= nums[i] <= 10
        - The product of every subarray fits in a 32-bit signed integer.

    Notes:
        - A subarray must be contiguous.
        - A single element can be the answer.
        - Zero separates independent portions of the array.
        - An even number of negative values produces a positive product.
    """

    def maximum_product_subarray_brute(self, nums: list[int]) -> int:
        """
        Intuition:
            Generate every possible contiguous subarray and keep track
            of its product. Instead of recalculating the product from
            scratch, extend each subarray one element at a time.

        Algorithm:
            1. Choose every possible starting index i.
            2. Initialize the product to 1.
            3. Extend the subarray from i to every possible ending index j.
            4. Multiply the current element into the running product.
            5. Update the maximum product.

        Time:
            O(n^2)

        Space:
            O(1)
        """

        res = nums[0]

        for i in range(len(nums)):
            prod = 1

            for j in range(i, len(nums)):
                prod *= nums[j]
                res = max(res, prod)

        return res

    def maximum_product_subarray_sliding_window(self, nums: list[int]) -> int:
        """
        Intuition:
            Zero splits the array into independent segments because any
            subarray containing zero has product zero.

            For a zero-free segment, a positive product requires an even
            number of negative values. Therefore, determine the largest
            valid even number of negatives and use a sliding window to
            maintain that condition.

        Algorithm:
            1. Split nums into zero-free subarrays.
            2. For each subarray, count the total number of negative values.
            3. Determine the largest even number of negatives allowed.
            4. Expand the window from left to right while maintaining
               its product.
            5. If the window contains too many negative values, remove
               elements from the left until it becomes valid.
            6. Update the maximum product for every non-empty window.
            7. Keep zero as a possible answer because it may be larger
               than every negative product.

        Time:
            O(n)

        Space:
            O(n)
        """

        arr = []
        curr = []
        res = float("-inf")

        for num in nums:
            res = max(res, num)

            if num == 0:
                if curr:
                    arr.append(curr)
                curr = []
            else:
                curr.append(num)

        if curr:
            arr.append(curr)

        for sub in arr:
            negs = sum(1 for num in sub if num < 0)
            need = negs if negs % 2 == 0 else negs - 1 # need even number of negs to make a positive product

            prod = 1
            negs = 0
            left = 0

            for right in range(len(sub)):
                prod *= sub[right]

                if sub[right] < 0:
                    negs += 1

                    while negs > need:
                        prod //= sub[left] # removing the left element
                        if sub[left] < 0:
                            negs -= 1
                        left += 1

                if left <= right:
                    res = max(res, prod)

        return res


    def maximum_product_subarray_kadanes(self, nums: list[int]) -> int:
        """
        Intuition:
            Similar to Kadane's algorithm, maintain the best product
            ending at the current position. However, unlike the maximum
            sum problem, we also need the minimum product.

            This is because multiplying a negative number by a negative
            product can produce a large positive product.

        Algorithm:
            1. Initialize max_prod and min_prod with the first element.
            2. For each remaining number, consider:
                   - Starting a new subarray with the current number.
                   - Extending the previous maximum product.
                   - Extending the previous minimum product.
            3. Store the maximum and minimum of these three possibilities.
            4. Update the global result using the current maximum product.

        Time:
            O(n)

        Space:
            O(1)
        """

        min_prod = nums[0]
        max_prod = nums[0]
        res = nums[0]

        for num in nums[1:]:
            temp_max = max(num, num * max_prod, num * min_prod)
            temp_min = min(num, num * max_prod, num * min_prod)

            max_prod = temp_max
            min_prod = temp_min

            res = max(res, max_prod)

        return res

    def maximum_product_subarray_prefix_suffix(self, nums: list[int]) -> int:
        """
        Intuition:
            For a zero-free segment, if there are an even number of
            negative values, the entire segment can be used. If there
            are an odd number of negatives, the maximum product can be
            obtained by removing either a prefix through the first
            negative or a suffix through the last negative.

            By scanning from both directions, we can consider both
            possibilities simultaneously.

        Algorithm:
            1. Maintain a running prefix product from the left.
            2. Maintain a running suffix product from the right.
            3. When either product becomes zero, reset it to 1 so that
               the next segment can be processed.
            4. After each position, update the maximum result using
               both prefix and suffix products.

        Time:
            O(n)

        Space:
            O(1)
        """

        n, res = len(nums), nums[0]
        prefix, suffix = 1, 1

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[~i] * (suffix or 1)

            res = max(res, prefix, suffix)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (nums: list[int], expected: int)
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2, -5], 10),
        ([3], 3),
        ([0, -2, -3], 6),
    ]

    for nums, expected in test_cases:
        result = solution.maximum_product_subarray_prefix_suffix(nums)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")