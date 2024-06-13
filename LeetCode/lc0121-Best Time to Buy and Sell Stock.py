# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# brute forces
# time:O(n**2), space:O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for buy in range(len(prices)):
            for sell in range(buy+1, len(prices)):
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
        return max_profit


# two pointers
# time:O(n), space:O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1

        return max_profit

            
