# https://leetcode.com/problems/climbing-stairs/description/

# recursion - TLE - time limit exceeded
# time-O(2**n), space-O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i == 1:
                return 1

            if i == 2:
                return 2

            return dfs(i-1) + dfs(i-2)
        return dfs(n)


# memoization
# time-O(n), space-O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i in memo:
                return memo[i]
                
            memo[i] = dfs(i-1) + dfs(i-2)
            return memo[i]

        memo = {1:1, 2:2}
        return dfs(n)

# bottom up/Tabulation
# time-O(n), space-O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1 or n== 2:
            return n

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

# Space Optimization
# time-O(n), space-O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1 or n== 2:
            return n

        prev = 1
        curr = 2

        for i in range(2, n):
            prev, curr = curr, prev + curr

        return curr
