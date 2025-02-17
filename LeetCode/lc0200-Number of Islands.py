#############################################################
# my solutions below

# DFS using recursion

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            # base case
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if (r,c) in visited:
                return
            if grid[r][c] == "0":
                return
            
            visited.add((r,c))
            for dr, dc in directions:
                new_row = r+dr
                new_col = c+dc
                dfs(new_row, new_col)  
        
        
        if not grid:
            return 0
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands
    

# BFS using QUEUE
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                row,col = q.popleft()
                visited.add((row,col))
                
                # explore neighbors
                for dr,dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    
                    # check for boundary
                    if new_row<0 or new_row==rows or new_col<0 or new_col==cols:
                        continue
                    
                    # check if not in visited
                    if (new_row, new_col) in visited:
                        continue
                    
                    # check if land vs. water
                    if grid[new_row][new_col] == "0":
                        continue
                        
                    # explore the neighbors by adding them to the stack
                    if (new_row,new_col) not in q:
                        q.append((new_row, new_col))
        
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
                    
        return islands




# DFS using STACK
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                row,col = q.pop()
                visited.add((row,col))
                
                # explore neighbors
                for dr,dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    
                    # check for boundary
                    if new_row<0 or new_row==rows or new_col<0 or new_col==cols:
                        continue
                    
                    # check if not in visited
                    if (new_row, new_col) in visited:
                        continue
                    
                    # check if land vs. water
                    if grid[new_row][new_col] == "0":
                        continue
                        
                    # explore the neighbors by adding them to the stack
                    if (new_row,new_col) not in q:
                        q.append((new_row, new_col))
        
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
                    
        return islands
