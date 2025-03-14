# recursion - TLE
# time:O(nm^nm), space:O(nm)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def dp(i,j):
            # base case
            if i <0 or i >= n or 
               j <0 or j >= m or 
               matrix[i][j] == "0":
                return 0
        
            return 1 + min(dp(i+1,j), 
                           dp(i+1, j+1), 
                           dp(i,j+1))

        # run the recursion from each cell which is 1
        n = len(matrix)
        m = len(matrix[0])
        largestSide = 0

        for row in range(n):
            for col in range(m):
                if matrix[row][col] == "1":
                    largestSide = max(largestSide, dp(row,col))

        return largestSide**2


# recursion + memoization - top down
# time:O(nm), space:O(nm)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def dp(i,j,memo):
            if (i,j) in memo:
                return memo[(i,j)]

            # base case
            if i <0 or i >= n or j <0 or j >= m or matrix[i][j] == "0":
                return 0
        
            memo[(i,j)] = 1 + min(dp(i+1,j,memo), 
                                dp(i+1, j+1,memo), 
                                dp(i,j+1,memo))
            return memo[(i,j)]
        # run the recursion from each cell which is 1
        n = len(matrix)
        m = len(matrix[0])
        largestSide = 0
        memo = {}
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == "1":
                    largestSide = max(largestSide, dp(row,col,memo))

        return largestSide**2


# bottom up tabulation
# time:O(mn), space:O(mn)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*(cols+1) for _ in range(rows+1)]
        largestSide = 0

        for row in range(1, rows+1):
            for col in range(1, cols+1):
                if matrix[row-1][col-1] == "1":
                    dp[row][col] = 1 + min(dp[row-1][col],
                                           dp[row][col-1],
                                           dp[row-1][col-1])

                    largestSide = max(largestSide, dp[row][col])


        return largestSide**2





# bottom up space optimized
# time:O(mn), space:O(n)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [0]*(cols+1)
        largestSide = 0
        prev = 0

        for row in range(1, rows+1):
            for col in range(1, cols+1):
                
                temp = dp[col]
                
                if matrix[row-1][col-1] == "1":
                    dp[col] = min(min(dp[col - 1], prev), dp[col]) + 1
                    largestSide = max(largestSide, dp[col])
                else:
                    dp[col] = 0

                prev = temp

        return largestSide**2

