# say that you are a traveler one a 2D grid. 
# You begin in the top-left corner and your goal is to 
# travel to the bottom-right corner. Your may only move 
# down or right.In how many ways can you trael to the 
# goal on a grid with dimensions m * n



# time:O(m*n), space:O(m+n)

def uniquePaths(m: int, n: int, memo = {}) -> int:
    # base cases

    # check memo
    if (m,n) in memo:
        return memo[(m,n)]

    # if out of boundry - 
    # 0Xm or nX0 - only 0 ways 
    if m == 0 or n == 0:
        return 0
    
    # 1X1 grid - only one way
    if m == n == 1:
        return 1
    
    # traverse next coordinate
    memo[(m,n)] = uniquePaths(m-1, n, memo) + uniquePaths(m, n-1, memo)   
    return memo[(m,n)]



print(uniquePaths(1,1)) # 1
print(uniquePaths(2,3)) # 3
print(uniquePaths(3,2)) # 3
print(uniquePaths(3,3)) # 6
print(uniquePaths(18,18)) # 2333606220
