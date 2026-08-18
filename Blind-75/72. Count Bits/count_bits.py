class Solution:
    """
    Problem:
        Given an integer n, return an array of length n + 1 where the value at
        index i is the number of set bits (1s) in the binary representation
        of i.

        Example:
            n = 5
            Output = [0, 1, 1, 2, 1, 2]

    Approach:
        1. Use Brian Kernighan's bit manipulation technique to count the set
           bits of every number independently.
        2. Use dynamic programming with the most significant power of two
           as an offset to derive the count for each number.
        3. Use the recurrence:
               bits[i] = bits[i >> 1] + (i & 1)
           which removes the least significant bit and adds it to the count.

    Constraints:
        - 0 <= n <= 10^5

    Notes:
        - The result must be computed without using built-in popcount functions.
        - The first approach runs in O(n log n) time.
        - The dynamic programming approaches run in O(n) time.
        - All approaches use O(n) additional space for the result array.
    """

    def count_bits_bit_manipulation(self, n):
        """
        Count set bits using Brian Kernighan's bit manipulation technique.

        Intuition:
            - For any positive integer `num`, the operation
                  num &= (num - 1)
              removes the lowest set bit (the rightmost `1`) from `num`.
            - Therefore, the number of times this operation can be performed
              before `num` becomes zero is exactly the number of set bits.
            - Apply this independently to every number from 0 through n.

        Algorithm:
            - Initialize an array `counts` of size n + 1.
            - For each number `i` from 0 to n:
                1. Copy `i` into `num`.
                2. Repeatedly remove its lowest set bit using
                   `num &= (num - 1)`.
                3. Count how many times the operation is performed.
                4. Store that count at `counts[i]`.
            - Return `counts`.

        Time:
            O(n log n) in the worst case, since each number can require
            O(log n) bit-removal operations.

        Space:
            O(n) for the output array.
        """

        counts = [0] * (n + 1)

        for i in range(n + 1):
            num = i
            while num:
                num &= (num - 1)
                counts[i] += 1

        return counts


    def count_bits_bit_manipulation_dp(self, n):
        """
        Count set bits using dynamic programming based on powers of two.

        Intuition:
            - Every number can be represented as a power of two plus a
              smaller remainder.
            - If `offset` is the largest power of two less than or equal to
              `num`, then:
                  num = offset + (num - offset)
            - Since a power of two contains exactly one set bit:
                  bits[num] = 1 + bits[num - offset]
            - As we iterate through the numbers, update `offset` whenever
              we reach the next power of two.

        Algorithm:
            - Initialize `dp[0] = 0`.
            - Start `offset` at 1, representing the current power of two.
            - For each number `num` from 1 to n:
                1. If `num` is the next power of two, update `offset`.
                2. Compute the number of set bits using:
                       dp[num] = 1 + dp[num - offset]
                3. Store the result in `dp[num]`.
            - Return `dp`.

        Time:
            O(n), because every number is processed exactly once.

        Space:
            O(n) for the dynamic programming array.
        """

        dp = [-1] * (n + 1)
        dp[0] = 0

        offset = 1
        for num in range(1, n + 1):
            if num == offset * 2:
                offset = num
            dp[num] = 1 + dp[num - offset]

        return dp


    def count_bits_bit_manipulation_dp_optimal(self, n):
        """
        Count set bits using a one-pass dynamic programming recurrence.

        Intuition:
            - Right-shifting a number by one removes its least significant
              bit:
                  num >> 1
            - The removed bit is exactly the least significant bit, which can
              be obtained with:
                  num & 1
            - Therefore, the number of set bits in `num` is:
                  bits[num] = bits[num >> 1] + (num & 1)
            - Since `num >> 1` is always smaller than `num`, its result has
              already been computed when processing `num`.

        Algorithm:
            - Initialize `dp[0] = 0`.
            - For every number `num` from 1 through n:
                1. Compute `num >> 1` to remove the least significant bit.
                2. Use `dp[num >> 1]` as the number of set bits in the
                   remaining higher bits.
                3. Add `(num & 1)` to account for the removed bit.
                4. Store the result in `dp[num]`.
            - Return `dp`.

        Time:
            O(n), because each number requires constant-time bit operations
            and is processed exactly once.

        Space:
            O(n) for the dynamic programming array.

        Notes:
            - This is the most concise of the three approaches.
            - It performs the computation in a single forward pass.
            - For example:
                  5 = 101
                  5 >> 1 = 10
                  5 & 1 = 1

              Therefore:
                  bits[5] = bits[2] + 1
                         = 1 + 1
                         = 2
        """

        dp = [-1] * (n + 1)
        dp[0] = 0

        for num in range(1, n + 1):
            dp[num] = dp[num >> 1] + (num & 1)
            # you can also write it as this if it makes more sense
            # dp[num] = dp[num // 2] + (num % 2)

        return dp


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (n: int, expected: list[int])
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (16, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1])
    ]

    for n, expected in test_cases:
        result = solution.count_bits_bit_manipulation_dp_optimal(n)
        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"n = {n}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"n = {n}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")