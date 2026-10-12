class Solution:
    """
    Problem:
        Given two integers a and b, return their sum without using
        the addition (+) or subtraction (-) operators.

    Approach:
        1. Simulate binary addition bit by bit using XOR and carry.
        2. Alternatively, use XOR for the partial sum and AND with
           left shift to calculate the carry.
        3. Use a 32-bit mask to simulate fixed-width integer arithmetic
           and handle negative results in Python.

    Constraints:
        - -1000 <= a, b <= 1000

    Notes:
        - XOR (^) computes the sum of two bits without a carry.
        - AND (&) identifies positions that generate a carry.
        - Left shift (<< 1) moves the carry to the next bit position.
        - Python integers have arbitrary precision, so a 32-bit mask
          is needed to simulate 32-bit integer behavior.
    """

    def sum_of_two_integers_bit_manipulation(self, a: int, b: int) -> int:
        """
        Intuition:
            Simulate binary addition one bit at a time. XOR determines
            the current sum bit, and carry handles overflow to the
            next bit position.

        Algorithm:
            1. Initialize carry and result to zero.
            2. Iterate through all 32 bit positions.
            3. Extract the corresponding bits of a and b.
            4. Compute the current bit using XOR of both bits and carry.
            5. Update carry if at least two bits are set.
            6. Set the result bit if the current bit is 1.
            7. Convert the unsigned result to a signed 32-bit integer
               when the most significant bit is set.

        Time:
            O(1) - Exactly 32 iterations.

        Space:
            O(1) - Uses a constant number of variables.
        """

        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            curr_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) > 1

            if curr_bit:
                res |= (1 << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res

    def sum_of_two_integers_bit_manipulation_optimal(
        self, a: int, b: int
    ) -> int:
        """
        Intuition:
            XOR calculates the partial sum without carrying, while
            AND identifies carry-generating bit positions. Shifting
            the carry left by one aligns it with the next bit position.

        Algorithm:
            1. Initialize a 32-bit mask and the maximum signed
               32-bit integer.
            2. While b is nonzero:
                - Calculate carry using (a & b) << 1.
                - Calculate the partial sum using (a ^ b) & mask.
                - Update b with the carry, restricted to 32 bits.
            3. Convert the final result to a signed 32-bit integer
               if it exceeds the maximum signed integer.

        Time:
            O(1) - At most 32 iterations for fixed-width arithmetic.

        Space:
            O(1) - Uses a constant number of variables.
        """

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (a: int, b: int, expected: int)
        (1, 2, 3),
        (4, 6, 10),
        (3, -2, 1),
        (-10, 3, -7),
    ]

    for a, b, expected in test_cases:
        result = solution.sum_of_two_integers_bit_manipulation_optimal(
            a, b
        )

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"a = {a}\n"
            f"b = {b}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"a = {a}\n"
            f"b = {b}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")