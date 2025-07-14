class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # check for dimensions of the input grid
        # 

        # approaches to traverse and calculates the max area - 
        # m - rows, n - cols
        # DFS - recursion - time:O(mn), space:O(mn)
        # DFS - iterative - using stack - time:O(mn), space:O(mn)
        # bfs - using queue - time:O(mn), space:O(mn)
        # union find  - using disjoint set - time:O(mn), space:O(mn)

        # traverse from a land area and explore its neighbors
        # if neighbors are water ->ignore, if land ->traverse

        # keep a counter of area 
        # return the max_area


        # DFS - recursive approach

        def dfs(r,c):
            # base case - out of boundry
            if r<0 or r>=row or c<0 or c>=cols:
                return 0

            # base case - water
            if grid[r][c] == 0:
                return 0

            # base case - if already visited
            if (r,c) in visited:
                return 0
            
            # mark as visited
            visited.add((r,c))

            curr_area = 1
            # explore its neighbors
            for dr, dc in directions:
                new_r = r+dr
                new_c = c+dc
                curr_area += dfs(new_r, new_c)
            return curr_area

        row = len(grid)
        cols = len(grid[0])

        # if not grid or rows == 0 or cols == 0:
        # return 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        max_area = 0

        for i in range(row):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]:
                    area = dfs(i,j)
                    max_area = max(max_area, area)

        return max_area




# DFS iterative-using stack
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            """stack based DFS implementation"""
            stack = [[i,j]]
            area = 0

            while stack:
                r,c = stack.pop()
                # check for in boundry
                if r<0 or r>=rows or c<0 or c>=cols:
                    continue
                # check for water/land
                if grid[r][c] == 0:
                    continue
                # check if already visited
                if (r,c) in visited:
                    continue

                visited.add((r,c))
                # account for area
                area += 1
                
                # explore the neighbors
                for dr, dc in directions:
                    new_r = r+dr
                    new_c = c+dc
                    stack.append((new_r,new_c))       

            return area

        
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]:
                    max_area = max(max_area, dfs(i,j))
        return max_area




# BFS iterative-using queue
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i,j):
            """queue based BFS implementation"""
            q =  deque([[i,j]])
            area = 0

            while q:
                r,c = q.popleft()
                # check for in boundry
                if r<0 or r>=rows or c<0 or c>=cols:
                    continue
                # check for water/land
                if grid[r][c] == 0:
                    continue
                # check if already visited
                if (r,c) in visited:
                    continue

                visited.add((r,c))
                # account for area
                area += 1
                
                # explore the neighbors
                for dr, dc in directions:
                    new_r = r+dr
                    new_c = c+dc
                    q.append((new_r,new_c))       

            return area

        
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]:
                    max_area = max(max_area, bfs(i,j))
        return max_area





# union find approach
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        # size or rank
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        # union by size
        if self.size[px] >= self.size[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]


    def get_size(self, x):
        px = self.find(x)
        return self.size[px]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        uf = UnionFind(rows*cols)
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    # explore neighbors
                    for dr, dc in directions:
                        new_r = r+dr
                        new_c = c+dc

                        # check inbounds
                        if new_r<0 or new_r>=rows or new_c<0 or new_c>= cols:
                            continue
                        
                        # check water
                        if grid[new_r][new_c] == 0:
                            continue

                        # union them
                        x1 = r*cols + c
                        x2 = new_r*cols + new_c
                        uf.union(x1, x2)
                    
                    max_area = max(max_area, uf.get_size(r*cols + c))                

        return max_area
