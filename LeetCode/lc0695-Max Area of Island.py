# DFS - time:O(m*n), space:O(m*n) + recusrive callstack
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0


        def dfs(r,c):
            if r<0 or c<0 or r>= rows or c>=cols or (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r,c))
            return 1+ dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    curr_area = dfs(i, j)
                    max_area = max(max_area, curr_area)

        return max_area



# bfs - queue - time:O(m*n), space:O(m*n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            area = 0

            while q:
                row,col = q.popleft()
                area += 1
                for x,y in [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]:
                    if 0<=x<rows and 0<=y<cols and (x,y) not in visited and grid[x][y]==1:
                        q.append((x,y))
                        visited.add((x,y))
            return area

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    curr_area = bfs(i,j)
                    max_area = max(max_area, curr_area)





# dfs - stack
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0


        def dfs(r,c):
            stack = []
            stack.append((r,c))
            visited.add((r,c))
            area = 0

            while stack:
                row, col = stack.pop()
                area += 1

                for x,y in [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]:
                    if 0<=x<rows and 0<=y<cols and (x,y) not in visited and grid[x][y]:
                        stack.append((x,y))
                        visited.add((x,y))

            return area


        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == 1:
                    curr_area = dfs(i,j)
                    max_area = max(max_area, curr_area)
        return max_area


        return max_area

