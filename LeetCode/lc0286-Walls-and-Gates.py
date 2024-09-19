#https://neetcode.io/problems/islands-and-treasure
# trick is to start from the gate(grid[i][j] == 0
# bfs - queue
import collections
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        q = collections.deque()

        # add all gates to the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        # def bfs
        def addRoom(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols
                or (r,c) in visited
                or grid[r][c] == -1):
                return 
            visited.add((r,c))
            q.append((r,c))
            

        # call bfs
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                addRoom(r+1,c)
                addRoom(r,c+1)
                addRoom(r-1,c)
                addRoom(r,c-1)


            distance += 1

        
