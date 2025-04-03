# recursion
# time:O(n^m), space:O(m), n-len of coins, m=amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(curr_amount):
            if curr_amount  == 0:
                return 0
            if curr_amount < 0:
                return -1

            required = float("inf")
            for coin in coins:
                remaining = curr_amount - coin
                coins_used = dp(remaining)
                if coins_used != -1:
                    required = min(required, coins_used + 1)


            return required

        result = dp(amount)
        return result if result != float("inf") else -1



# recursion + memoization
# time:O(nm), space:O(m), n-len of coins, m=amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(curr_amount):
            if curr_amount  == 0:
                return 0
            if curr_amount < 0:
                return -1

            required = float("inf")
            for coin in coins:
                remaining = curr_amount - coin
                coins_used = dp(remaining)
                if coins_used != -1:
                    required = min(required, coins_used + 1)


            return required

        result = dp(amount)
        return result if result != float("inf") else -1


# tabulation
# time:O(nm), space:O(m) -n-len of coins, m=amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i], 1+dp[i-coin])

        return dp[-1] if dp[-1] != float("inf") else -1
