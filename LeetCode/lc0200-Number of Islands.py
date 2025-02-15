# REFER NEETCODE VIDEO EXPLANATION
# for both DFS and BFS

# bfs - with popleft and dfs with pop

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        # 0 - dimensions
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        result = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        
        # 2 - define BFS
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                r,c= q.pop()
                for dr, dc in directions:
                    new_r = r+dr
                    new_c = c+dc
                    # check for boundary
                    if not (new_r<0 or new_r>=rows or new_c<0 or new_c>=cols or
                            (new_r,new_c) in visited or 
                            grid[new_r][new_c] == "0"):
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
            

        # 1 - call BFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # call bfs on that cell
                    bfs(r,c)
                    result += 1
                    
        return result




# simple DFS - 
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0


        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or (r,c) in visited or grid[r][c] !="1":
                return
            
            visited.add((r,c))

            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
            return 


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands += 1

        return islands
