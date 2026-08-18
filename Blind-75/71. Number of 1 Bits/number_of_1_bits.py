class Solution:
    """
    Problem:
        Given a positive integer `n`, return the number of set bits (1s)
        in its binary representation, also known as its *Hamming weight*.

    Approach:
        1. Iterate over the 32 possible bit positions and use a bit mask
           to check whether each bit is set.
        2. Repeatedly inspect the least significant bit and right-shift
           the number until no bits remain.
        3. Use Brian Kernighan's algorithm, where `num & (num - 1)`
           removes the rightmost set bit. This is the optimal bitwise
           approach because it iterates only once per set bit.
        4. Use Python's built-in `bin()` function to convert the number
           to its binary representation and count the occurrences of `1`.

    Constraints:
        - 1 <= n <= 2^31 - 1
        - The input is a positive 32-bit signed integer.

    Notes:
        - A set bit is a bit whose value is 1.
        - The number of set bits is also called the Hamming weight.
        - Brian Kernighan's algorithm is especially efficient when the
          number contains relatively few set bits.
        - If this function is called many times, a lookup table can be
          used to precompute the Hamming weight of smaller bit groups.
    """

    def number_of_1_bits_bit_mask_1(self, num: int) -> int:
        """
        Count set bits by checking every bit position with a bit mask.

        Intuition:
            - A bit mask with only the `i`-th bit set is created using
              `1 << i`.
            - ANDing this mask with `num` tells us whether the `i`-th bit
              of `num` is set.
            - Since the input is a 32-bit integer, we check all 32 positions.

        Algorithm:
            - Initialize a counter to 0.
            - For each bit position from 0 through 31:
                - Create a mask with only that bit set.
                - Use bitwise AND to check whether the corresponding bit
                  in `num` is 1.
                - Increment the counter if the bit is set.
            - Return the counter.

        Time:
            O(1), because exactly 32 bit positions are checked.

        Space:
            O(1), because only a constant amount of extra space is used.
        """

        cnt = 0
        for i in range(32):
            if (1 << i) & num:
                cnt += 1
        return cnt


    def number_of_1_bits_bit_mask_2(self, num: int) -> int:
        """
        Count set bits by repeatedly checking and removing the least
        significant bit.

        Intuition:
            - `num & 1` extracts the least significant bit.
            - If the result is 1, the current number has a set bit at
              that position.
            - Right-shifting by one moves the next bit into the least
              significant position.
            - Continue until all bits have been processed.

        Algorithm:
            - Initialize a counter to 0.
            - While `num` is not zero:
                - Add `num & 1` to the counter.
                - Right-shift `num` by one position.
            - Return the counter.

        Time:
            O(1), because each iteration processes one binary digit.
            And here there will be 32 binary digits. Otherwise it'll
            be O(log n).

        Space:
            O(1), because only a constant amount of extra space is used.
        """

        cnt = 0
        while num:
            cnt += num & 1
            num >>= 1
        return cnt


    def number_of_1_bits_optimal(self, num: int) -> int:
        """
        Count set bits using Brian Kernighan's algorithm.

        Intuition:
            - The operation `num & (num - 1)` removes the rightmost
              set bit from `num`.
            - Therefore, every iteration corresponds to exactly one
              set bit.
            - The loop terminates when all set bits have been removed.

        Algorithm:
            - Initialize a counter to 0.
            - While `num` is not zero:
                - Remove the rightmost set bit using
                  `num &= num - 1`.
                - Increment the counter.
            - Return the counter.

        Time:
            O(k), where `k` is the number of set bits in `num`.
            Since `num` is a 32-bit integer, this is O(1) in the
            context of the problem.

        Space:
            O(1), because only a constant amount of extra space is used.
        """

        cnt = 0
        while num:
            num &= (num - 1)  # removes the rightmost set bit
            cnt += 1
        return cnt


    def number_of_1_bits_builtin(self, num: int) -> int:
        """
        Count set bits using Python's built-in binary conversion.

        Intuition:
            - `bin(num)` returns the binary representation of `num`
              as a string prefixed with `0b`.
            - Counting the character `'1'` gives the number of set bits.

        Algorithm:
            - Convert `num` to its binary string representation using
              `bin()`.
            - Count the occurrences of `'1'`.
            - Return the count.

        Time:
            O(log n), because the binary representation contains
            O(log n) bits and the string must be traversed.

        Space:
            O(log n), because `bin(num)` creates a binary representation
            string.
        """

        return bin(num).count('1')


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (num: int, expected: int)
        (11, 3), # 11 -> 1011 -> 3 one bits
        (128, 1),
        (2147483645, 30),
    ]

    for num, expected in test_cases:
        result = solution.number_of_1_bits_bit_builtin(num)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"num = {num}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"num = {num}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")