# recursive dfs from netcode
# time:O(m*n), space:O(m*n) - visited set and call stack
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            # base cases
            # if already visited
            if (i,j) in visited:
                return 0

            # lower out of bounds
            if i < 0 or j < 0:
                return 1
            
            # upper out of bounds
            if i>=len(grid) or j>=len(grid[0]):
                return 1

            # if water
            if grid[i][j] == 0:
                return 1

            # recurse
            visited.add((i, j))

            perimeter = dfs(i, j-1) # left
            perimeter += dfs(i, j+1) # right
            perimeter += dfs(i-1, j) # up
            perimeter += dfs(i+1, j) # down
            
            #         (-1,0)
            # (0,-1) (0,0) (0,1)
            #         (1,0)

            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)




# iterative solution from solutions tab
# on the idea of adding 4(for the boundaries of the cell)
# and then removing 2 if that is a shared boundary
# time:O(n*m), space:O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if we are on land
                if grid[row][col] == 1:
                    perimeter += 4

                    # check the cell to the left
                    if col>0 and grid[row][col-1] == 1:
                        perimeter -= 2
                    # check the cell to the up
                    if row>0 and grid[row-1][col] == 1:
                        perimeter -= 2

                    
        return perimeter
