# recursion - time - O(2^(m+n)), space:O(m+n)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        directions = [(0,1), (1,0)]

        if obstacleGrid[ROWS-1][COLS-1]:
            return 0

        def get_paths(r, c):
            if r >= ROWS or c>= COLS:
                return 0
            
            if obstacleGrid[r][c]:
                return 0

            if (r, c) == (ROWS-1, COLS-1):
                return 1

            paths = 0
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                paths += get_paths(new_r, new_c)
            
            return paths

        return get_paths(0,0)      

# memoization
# timeO(mn), space:O(1)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[0][0] or obstacleGrid[ROWS-1][COLS-1]:
            return 0

        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = 1

        # first col
        for r in range(1, ROWS):
            if obstacleGrid[r][0]:
                dp[r][0] = 0
            else:
                dp[r][0] = dp[r-1][0]            
            
        # first row
        for c in range(1, COLS):
            if obstacleGrid[0][c]:
                dp[0][c] = 0
            else:
                dp[0][c] = dp[0][c-1]

        # fill the rest of the dp table
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # if curr cell = obstacle then assign 0
                # else assign sum of top + left
                if obstacleGrid[r][c]:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[ROWS-1][COLS-1]

            
