# time:O(n^2), space:O(n^2)
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1

        
        n = len(grid)
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
        
        queue = deque([(0,0,1)]) # row, col, length
        visited.add((0,0))

        while queue:
            row,col,distance = queue.popleft()
            # check if this is the target position
            if row == n-1 and col == n-1:
                return distance

            # explore its neighbors/children
            for dr,dc in directions:
                new_row = row+dr
                new_col = col+dc

                # check for index out of bounds
                if new_row<0 or new_row>=n or new_col<0 or new_col>=n:
                    continue

                # check if value = 1, then continue
                if grid[new_row][new_col]:
                    continue

                # check if not in visited:
                if (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, distance+1))
                    visited.add((new_row, new_col))

        return -1


####################################################################
# return all shortest paths - BFS

# time:O(n^2), space:O(n^2)

from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]):
        if not grid or grid[0][0] or grid[len(grid)-1][len(grid)-1]:
            return [-1, []]

        
        n = len(grid)
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
        
        queue = deque([(0,0,1,[(0,0)])]) # row, col, length, path
        visited.add((0,0))

        while queue:
            row,col,distance,path = queue.popleft()
            print(path)
            # check if this is the target position
            if row == n-1 and col == n-1:
                return [distance, path]

            # explore its neighbors/children
            for dr,dc in directions:
                new_row = row+dr
                new_col = col+dc

                # check for index out of bounds
                if new_row<0 or new_row>=n or new_col<0 or new_col>=n:
                    continue

                # check if value = 1, then continue
                if grid[new_row][new_col]:
                    continue

                # check if not in visited:
                if (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, distance+1,path+[(new_row, new_col)]))
                    visited.add((new_row, new_col))

        return [-1, []]

                
grid = [[0,0,0],[1,1,0],[1,1,0]]
solution = Solution()
print(solution.shortestPathBinaryMatrix(grid))






######################################################################


# return any one of the paths - DFS


