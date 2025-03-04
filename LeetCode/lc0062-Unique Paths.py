# recursion - TLE - time:O(2^(m+n)), space:O(m+n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # base cases
        # if out of boundry - 
        # 0Xm or nX0 - only 0 ways 
        if m == 0 or n == 0:
            return 0
        
        # 1X1 grid - only one way
        if m == n == 1:
            return 1
        
        # traverse next coordinate
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)   




# recursion with memoization - top down DP
# time:O(mn), space:O(m+n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def paths(m,n,memo):
            # base cases
            # if out of boundry - 
            # 0Xm or nX0 - only 0 ways 
            if m == 0 or n == 0:
                return 0
            
            # 1X1 grid - only one way
            if m == n == 1:
                return 1

            # if in memo
            if (m,n) in memo:
                return memo[(m,n)]
            
            # traverse next coordinate
            memo[(m,n)] = paths(m-1, n,memo) + paths(m, n-1,memo)   
            return memo[(m,n)]
        
        return paths(m,n,dict())


# tabulation - bottom up DP
# time:O(mn), space:O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[m-1][n-1]
