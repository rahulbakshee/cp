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



   
# union find  - time:O(mn), space:O(mn)
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # initially parent of itself
        self.rank = [1] * n                 # initially rank 1 for all

    def find(self, x)->int:
        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # find parent
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        # union by rank
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dsu = DSU(rows*cols)

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    # explore neighbors
                    for dr, dc in directions:
                        new_r = r+dr
                        new_c = c+dc
                        if (new_r<0 or new_r>=rows or 
                            new_c<0 or new_c>=cols or  
                            grid[new_r][new_c] == "0"):
                            continue
                        # find the index of the cell as we have a 2D grid
                        # pass those indexes to union
                        x = r*cols + c
                        y = new_r*cols + new_c
                        if dsu.union(x,y):
                            islands -= 1

        return islands
