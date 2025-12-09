# recursion
# time:O(n^m), space:O(m), n-len of coins, m=amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(curr):
            if curr == 0:
                return 0

            if curr < 0:
                return amount+1

            required_coins = amount + 1
            for coin in coins:
                required_coins = min(required_coins, 1+dfs(curr - coin))

            return required_coins


        result = dfs(amount)
        return -1 if result == amount+1 else result




# recursion + memoization
# time:O(nm), space:O(m), n-len of coins, m=amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(curr):
            if curr in memo:
                return memo[curr]

            if curr < 0:
                return amount+1

            required_coins = amount + 1
            for coin in coins:
                required_coins = min(required_coins, 1+dfs(curr - coin))

            memo[curr] = required_coins
            return memo[curr]


        memo = {0:0}
        result = dfs(amount)
        return -1 if result == amount+1 else result



# tabulation
# time:O(nm), space:O(m) -n-len of coins, m=amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i] , 1+dp[i-coin])

        return dp[amount] if dp[amount] != amount+1 else -1
