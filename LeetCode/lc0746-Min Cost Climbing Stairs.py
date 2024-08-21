# TLE - time:O(2**n), space:O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def recursion(n):
            # base case
            if n <2:
                return cost[n]
            
            return cost[n] + min(recursion(n-1), recursion(n-2))

        n = len(cost)
        return min(recursion(n-1), recursion(n-2))

# memo - top down - time:O(n), space:O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def memo(n):
            # base case
            if n in cache:
                return cache[n]
            
            cache[n] = cost[n] + min(memo(n-1), memo(n-2))
            return cache[n]
        
        cache = {0:cost[0], 1:cost[1]}
        n = len(cost)
        return min(memo(n-1), memo(n-2))
        

# bottom up - tabulation - time:O()
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])

        return min(dp[n-1], dp[n-2])
        


