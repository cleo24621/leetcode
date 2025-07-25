import math

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
        return max_profit
        