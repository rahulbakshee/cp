# say that you are a traveler one a 2D grid. 
# You begin in the top-left corner and your goal is to 
# travel to the bottom-right corner. Your may only move 
# down or right.In how many ways can you trael to the 
# goal on a grid with dimensions m * n




# time:O(m*n), space:O(n)

def uniquePaths(m: int, n: int) -> int:
    dp = [1]*(n)
    
    for row in range(1, m):
        for col in range(1, n):
            dp[col] += dp[col-1]

    return dp[n-1]


print(uniquePaths(1,1)) # 1
print(uniquePaths(2,3)) # 3
print(uniquePaths(3,2)) # 3
print(uniquePaths(3,3)) # 6
print(uniquePaths(18,18)) # 2333606220
