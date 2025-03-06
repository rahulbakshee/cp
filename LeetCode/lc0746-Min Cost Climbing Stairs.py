# recursion
# time:O(2^n) breadth^depth, space:O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(index):
            # base case
            if index >= len(cost):
                return 0
            
            return min(cost[index] + dp(index+1), cost[index] + dp(index+2))
        
        return min(dp(0),dp(1))




# recursion + memoization
# time:O(n) , space:O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(index, memo):
            # base case
            if index in memo:
                return memo[index]

            if index >= len(cost):
                return 0
            
            memo[index] = min(cost[index] + dp(index+1,memo), cost[index] + dp(index+2,memo))
            return memo[index]
        
        return min(dp(0,{}),dp(1,{}))




# bottom up DP- tabulation - iterative
# time:O(n), space:O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # edge case - if len of input less than 2
        if len(cost) < 2:
            return cost[0]

        # whne len of input is atleast 2 or more
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], 
                        dp[i-2]+cost[i-2])

        return dp[n]


# bottom up DP- space optimized - iterative
# time:O(n), space:O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # edge case - if len of input less than 2
        if len(cost) < 2:
            return cost[0]

        # whne len of input is atleast 2 or more
        n = len(cost)
        prev, curr = 0, 0

        for i in range(2, n+1):
            curr, prev = min(curr+cost[i-1], prev+cost[i-2]), curr

        return curr

