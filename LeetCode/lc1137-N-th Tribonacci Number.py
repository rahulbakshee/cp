# recursion 
# time:O(3^n), space:O(n) - 3 is because at every moment 3 options
class Solution:
    def tribonacci(self, n: int) -> int:

        def dp(n):
            # base case
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1

            return dp(n-1) + dp(n-2) + dp(n-3)
            
        return dp(n)


# recursion + memoization
# time:O(n), space:O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def dp(n):
            # base case
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1

            return dp(n-1) + dp(n-2) + dp(n-3)
            
        return dp(n)



# recursion + memoization
# time:O(n), space:O(n)
class Solution:
    def tribonacci(self, n: int) -> int:

        def dp(n,memo):
            if n in memo:
                return memo[n]
            # base case
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1

            memo[n] = dp(n-1,memo) + dp(n-2,memo) + dp(n-3,memo)
            return memo[n]
            
        return dp(n,{})


# iterative -DP- tabulation
# time:O(n), space:O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        # base case
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

        return dp[-1]


# iterative -DP- tabulation - space optimized
# time:O(n), space:O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        # base case
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        
        prevprev = 0
        prev = 1
        curr = 1

        for i in range(3, n+1):
            curr, prev, prevprev = curr+prev+prevprev, curr, prev

        return curr
