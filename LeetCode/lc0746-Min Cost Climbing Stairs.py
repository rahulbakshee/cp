# recursion
# time:O(2^n) breadth^depth, space:O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i == 0 or i == 1:
                return 0

            return min(cost[i-1] + dfs(i-1), cost[i-2] + dfs(i-2))

        n = len(cost)
        return dfs(n)



# recursion + memoization
# time:O(n) , space:O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i in memo:
                return memo[i]

            memo[i] = min(cost[i-1] + dfs(i-1), cost[i-2] + dfs(i-2))
            return memo[i]

        n = len(cost)
        memo = {0:0, 1:0}
        return dfs(n)


# bottom up DP- tabulation - iterative
# time:O(n), space:O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(cost[i-1] + dp[i-1], 
                        cost[i-2] + dp[i-2])

        return dp[-1]

# bottom up DP- space optimized - iterative
# time:O(n), space:O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev, curr = 0, 0

        for i in range(2, n+1):
            prev, curr = curr, min(cost[i-2] + prev, cost[i-1] + curr)

        return curr
