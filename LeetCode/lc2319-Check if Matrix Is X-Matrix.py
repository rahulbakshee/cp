# time:O(n**2), space:O(1)
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                if i == j or j == n-i-1:
                    # diagonals
                    if grid[i][j] == 0:
                        return False
                else:
                    # other than diagonals
                    if grid[i][j] !=0:
                        return False
        return True
