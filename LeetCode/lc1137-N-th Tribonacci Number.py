# recursion 
# time:O(3^n), space:O(n) - 3 is because at every moment 3 options
class Solution:
    def tribonacci(self, n: int) -> int:
        def dfs(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1

            return dfs(i-1) + dfs(i-2) + dfs(i-3)


        return dfs(n)



# recursion + memoization
# time:O(n), space:O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        def dfs(i):
            if i in memo:
                return memo[i]

            memo[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
            return memo[i]

        memo = {0:0, 1:1, 2:1}
        return dfs(n)



# iterative -DP- tabulation
# time:O(n), space:O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[-1]

# iterative -DP- tabulation - space optimized
# time:O(n), space:O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        prev = 0
        mid = 1
        curr = 1

        for i in range(3, n+1):
            prev, mid, curr = mid, curr, prev+mid+curr

        return curr
