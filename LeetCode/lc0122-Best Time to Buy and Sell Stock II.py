# time:O(n), space:O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        total_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
                right += 1
            else:
                while right+1 < len(prices) and prices[right+1] > prices[right]:
                    right += 1
                total_profit += prices[right] - prices[left]
                left = right
                right += 1

        return total_profit
