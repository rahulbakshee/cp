# time:O(n^2), space:O(n^2)
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        if not grid or rows == 0:
            return -1
        
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        visited = set()

        q = deque([(0,0,1)])
        while q:
            for _ in range(len(q)):
                r,c,length = q.popleft()

                if (r,c) == (rows-1,cols-1):
                    return length

                # explore children
                for dr,dc in directions:
                    new_r = r+dr
                    new_c = c+dc
                    
                    if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols:
                        continue

                    if grid[new_r][new_c]:
                        continue
                    
                    if (new_r,new_c) in visited:
                        continue
                    
                    visited.add((new_r,new_c))
                    q.append([new_r,new_c,length+1])

        
        return -1


####################################################################
# return all shortest paths - BFS - https://www.youtube.com/watch?v=kqwrHrxOpl0&ab_channel=CodingwithMinmer

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


# BELOW DFS CODE DOES NOT WORK FOR shortest path algo - 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return float("inf")

            if grid[r][c]:
                return float("inf")
            
            if (r,c) in visited:
                return float("inf")

            if (r,c) == (rows-1,cols-1):
                return 1

            visited.add((r,c))

            distance = float("inf")

            # explore children
            for dr,dc in directions:
                new_r = r+dr
                new_c = c+dc
                distance = min(distance, 1+dfs(new_r,new_c))

            return distance       

        rows = len(grid)
        cols = len(grid[0])
        
        if not grid or rows == 0:
            return -1
        
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        visited = set()

        result = dfs(0,0)
        return result if result != float("inf") else -1


