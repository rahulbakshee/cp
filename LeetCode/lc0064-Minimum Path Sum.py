# recursion -  exponential - 2^n
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def recursion(r,c):
            # base cases - out of bounds
            if r>=m or c>=n:
                return float("inf")

            if (r,c) == (m-1,n-1):
                return grid[r][c]

            right = recursion(r,c+1)
            down = recursion(r+1,c)
            
            return grid[r][c] + min(right, down)            


        m = len(grid)
        n = len(grid[0])
        return recursion(0,0)


# recursion + memoization - top down DP
# time:O(mn), space:O(mn)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def recursion(r,c):
            # base cases - out of bounds
            if r>=m or c>=n:
                return float("inf")

            if (r,c) == (m-1,n-1):
                return grid[r][c]

            if (r,c) in memo:
                return memo[(r,c)]

            right = recursion(r,c+1)
            down = recursion(r+1,c)
            
            memo[(r,c)] =  grid[r][c] + min(right, down) 
            return memo[(r,c)]           

        memo = {}
        m = len(grid)
        n = len(grid[0])
        return recursion(0,0)


# tabulation - bottom up 2D DP
# time:O(mn), space:O(mn)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = grid[m-1][n-1]
        

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r+1==m and c+1 == n:
                    dp[r][c] = dp[r][c]
                elif r+1 == m:
                    dp[r][c] = grid[r][c] + dp[r][c+1]
                elif c+1 == n: 
                    dp[r][c] = grid[r][c] + dp[r+1][c]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])


        return dp[0][0]




# tabulation - bottom up 1D DP
# time:O(mn), space:O(n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [0 for _ in range(n)]       

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r+1==m and c+1 == n:
                    dp[c] = grid[r][c]
                elif r+1 == m:
                    dp[c] = grid[r][c] + dp[c+1]
                elif c+1 == n: 
                    dp[c] = grid[r][c] + dp[c]
                else:
                    dp[c] = grid[r][c] + min(dp[c], dp[c+1])


        return dp[0]



# without extra space
# tabulation - bottom up 2D DP
# time:O(mn), space:O(1) - IMPORTANT
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r==m-1 and c==n-1:
                    continue
                if r+1 == m:
                    grid[r][c] = grid[r][c] + grid[r][c+1]
                elif c+1 == n: 
                    grid[r][c] = grid[r][c] + grid[r+1][c]
                else:
                    grid[r][c] = grid[r][c] + min(grid[r+1][c], grid[r][c+1])


        return grid[0][0]





        
