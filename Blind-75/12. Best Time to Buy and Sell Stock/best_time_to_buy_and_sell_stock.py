class Solution:
    """
    Problem:
        Given an array where prices[i] represents the stock price on the ith day,
        determine the maximum profit that can be achieved by buying one stock
        on a single day and selling it on a later day.

        Only one transaction (one buy and one sell) is allowed.
        If no profit can be made, return 0.

    Approach:
        1. Brute Force:
           Compare every possible buy/sell pair and keep track of the maximum profit.
        2. Two Pointers:
           Maintain a left pointer for the best buying day and a right pointer
           that scans through future days looking for better selling opportunities.
        3. Dynamic Programming (Running Minimum):
           Keep track of the minimum stock price seen so far and compute the
           profit obtainable by selling on each day.

    Constraints:
        - 1 <= len(prices) <= 10^5
        - 0 <= prices[i] <= 10^4

    Notes:
        - Buying must occur before selling.
        - Only one transaction is permitted.
        - Return 0 if no profitable transaction exists.
    """

    def best_time_to_buy_and_sell_stock_brute_force(self, prices: list[int]) -> int:
        """
        Intuition:
            Check every possible buying day against every valid future selling
            day. Record the largest profit encountered.

        Algorithm:
            - Iterate through each day as the buying day.
            - For every buying day, iterate through all future days as
              potential selling days.
            - Compute each profit and update the maximum profit.

        Time:
            O(n²)

        Space:
            O(1)
        """

        max_profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                max_profit = max(max_profit, sell - buy)

        return max_profit


    def best_time_to_buy_and_sell_stock_two_pointers(self, prices: list[int]) -> int:
        """
         Intuition:
            Treat the left pointer as the current best buying day and move the
            right pointer through the array searching for profitable selling
            days. Whenever a lower price is found, update the buying day.

        Algorithm:
            - Initialize the left pointer at day 0 (buy).
            - Move the right pointer through the remaining days (sell).
            - If selling is profitable, update the maximum profit.
            - Otherwise, move the left pointer to the current lower price.
            - Continue until every day has been processed.

        Time:
            O(n)

        Space:
            O(1)
        """

        max_profit = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return max_profit



    def best_time_to_buy_and_sell_stock_dp(self, prices: list[int]) -> int:
        """
        Intuition:
            The maximum profit from selling on a given day depends only on the
            lowest stock price seen before that day. By continuously tracking
            this minimum price, we can determine the best profit in a single pass.

        Algorithm:
            - Initialize the minimum price as the first day's price.
            - Traverse the remaining prices.
            - For each day:
                * Calculate the profit if sold today.
                * Update the maximum profit if necessary.
                * Update the minimum price seen so far.
            - Return the maximum profit.

        Time:
            O(n)

        Space:
            O(1)
        """

        max_profit = 0
        min_so_far = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_so_far)
            min_so_far = min(min_so_far, prices[i])

        return max_profit

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (prices, expected)
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ]

    for prices, expected in test_cases:
        result = solution.best_time_to_buy_and_sell_stock_dp(prices)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"prices = {prices}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"prices = {prices}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!")
    print("#######################")