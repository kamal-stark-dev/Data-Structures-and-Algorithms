class Solution:
    """
    Problem:
        Reverse the bits of a given 32-bit unsigned/signed integer.

        Given a 32-bit integer n, reverse the order of its 32 binary bits
        and return the resulting integer.

        For example:
            n = 00000010100101000001111010011100
        becomes:
            00111001011110000010100101000000

    Approach:
        1. Brute Force:
            - Build the 32-bit binary representation as a string.
            - Reverse the string.
            - Convert the reversed representation back into an integer.

        2. Bit Manipulation:
            - Process one bit at a time from right to left.
            - Extract the least significant bit using n & 1.
            - Shift the result left and append the extracted bit.
            - Repeat exactly 32 times.

        3. Optimal Bit Manipulation:
            - Reverse groups of bits using masks and shifts.
            - Swap the upper and lower 16 bits.
            - Swap adjacent groups of 8, 4, 2, and 1 bits.
            - This reverses all 32 bits without processing them individually.

    Constraints:
        - 0 <= n <= 2^31 - 2
        - n is even
        - The input is treated as a 32-bit integer.

    Notes:
        - The reversal must always consider exactly 32 bits, including leading
          zeroes.
        - The optimal approach is useful when the function is called many times,
          because it performs a fixed number of bitwise operations.
    """

    def reverse_bits_brute_force(self, n: int) -> int:
        """
        Reverse the 32 bits using a binary string representation.

        Intuition:
            - First construct the complete 32-bit representation of n.
            - Since leading zeroes matter when reversing bits, we explicitly
              process all 32 positions.
            - Reverse the resulting binary string.
            - Convert the reversed bits back into an integer using bitwise OR.

        Algorithm:
            1. Iterate through bit positions 0 through 31.
            2. Check whether each bit is set using:
                   n & (1 << i)
            3. Build a 32-character binary string from those bits.
            4. Reverse the string.
            5. Iterate through the reversed string.
            6. For every '1' bit at position i, set that bit in the result.
            7. Return the resulting integer.

        Time:
            O(32) = O(1)

        Space:
            O(32) = O(1)

        Notes:
            - Although the complexity is technically O(1) because the input
              size is fixed at 32 bits, this approach uses additional memory
              and string operations compared with the bit-manipulation
              approaches.
        """

        binary = ""
        for i in range(32):
            if n & (1 << i):
                binary += "1"
            else:
                binary += "0"

        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= (1 << i)

        return res


    def reverse_bits_bit_manipulation(self, n: int) -> int:
        """
        Reverse the 32 bits using repeated bit extraction and shifting.

        Intuition:
            - The least significant bit of n becomes the most significant bit
              of the reversed number.
            - We can extract the least significant bit using n & 1.
            - Shift the result left to make room for the next bit.
            - Shift n right to move the next bit into the least significant
              position.
            - Repeating this process 32 times reverses all bits.

        Algorithm:
            1. Initialize rev = 0.
            2. Repeat exactly 32 times:
                - Extract the current least significant bit of n using n & 1.
                - Shift rev left by one position.
                - Append the extracted bit using bitwise OR.
                - Shift n right by one position.
            3. Return rev.

        Example:
            Suppose the next bit of n is 1:

                rev = 101
                n   = ...1

            Then:

                rev << 1     -> 1010
                n & 1         -> 1
                (rev << 1)|1  -> 1011

            This effectively appends the extracted bit to the reversed result.

        Time:
            O(32) = O(1)

        Space:
            O(1)
        """

        rev = 0
        for i in range(32):
            rev = (rev << 1) | (n & 1)
            n >>= 1

        return rev


    def reverse_bits_bit_manipulation_optimal(self, n: int) -> int:
        """
        Reverse the 32 bits using parallel bit swapping.

        Intuition:
            - Instead of processing one bit at a time, reverse multiple groups
              of bits simultaneously.
            - We progressively swap increasingly smaller groups:
                1. Swap the two 16-bit halves.
                2. Swap 8-bit groups.
                3. Swap 4-bit groups.
                4. Swap 2-bit groups.
                5. Swap individual bits.
            - After all swaps, every bit has moved to its reversed position.

        Algorithm:
            1. Swap the upper and lower 16 bits.
            2. Swap every pair of 8-bit groups using an 8-bit mask.
            3. Swap every pair of 4-bit groups using a 4-bit mask.
            4. Swap every pair of 2-bit groups using a 2-bit mask.
            5. Swap adjacent individual bits using a 1-bit mask.
            6. Return the reversed 32-bit integer.

        Why the masks work:
            - Each mask selects alternating groups of bits.
            - The selected bits are shifted in one direction while the
              complementary groups are shifted in the opposite direction.
            - Combining them with bitwise OR swaps the groups.

            For example, the 16-bit swap:

                rev >> 16 | rev << 16

            exchanges the upper and lower halves of the 32-bit integer.

            The subsequent masks perform the same idea at smaller group sizes.

        Time:
            O(1)

            The algorithm always performs the same fixed number of bitwise
            operations regardless of the input value.

        Space:
            O(1)

        Notes:
            - This approach is particularly useful for the follow-up where
              the function may be called many times.
            - It avoids loops and string operations.
            - The implementation relies on the input being a 32-bit integer.
        """

        rev = n

        rev = (rev >> 16 | rev << 16)
        rev = (
              (rev & 0b11111111000000001111111100000000) >> 8
            | (rev & 0b00000000111111110000000011111111) << 8
        )
        rev = (
              (rev & 0b11110000111100001111000011110000) >> 4
            | (rev & 0b00001111000011110000111100001111) << 4
        )
        rev = (
              (rev & 0b11001100110011001100110011001100) >> 2
            | (rev & 0b00110011001100110011001100110011) << 2
        )
        rev = (
              (rev & 0b10101010101010101010101010101010) >> 1
            | (rev & 0b01010101010101010101010101010101) << 1
        )

        return rev


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (n: int, expected: int)
        (43261596, 964176192),
        (2147483644, 1073741822),
        (2147483646, 2147483646),
    ]

    for nums, expected in test_cases:
        result = solution.reverse_bits_bit_manipulation_optimal(nums)

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