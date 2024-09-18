# REFER NEETCODE VIDEO EXPLANATION
# for both DFS and BFS

# bfs - with popleft and dfs with pop

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                for x, y in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                    if 0<=x<len(grid) and 0<=y<len(grid[0]) and (x,y) not in visited and grid[x][y] == "1":
                        q.append((x,y))
                        visited.add((x,y))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1

        return islands
