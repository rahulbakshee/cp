# BFS
# time:O(nm), space:O(n+m)
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        # BFS
        from collections import deque
        visited = set(entrance)
        q = deque() # [entrance, steps]
        q.append([entrance[0], entrance[1], 0])


        while q:
            row, col, steps = q.popleft()

            # check for out of boundry
            if row<0 or row>=rows or col<0 or col>=cols:
                continue
            
            # check for wall
            if maze[row][col] == "+":
                continue

            # check for visited
            if (row,col) in visited:
                continue

            # success - check for exit
            if (row==0 or col==0 or row==rows-1 or col==cols-1) and [row,col] != entrance:
                return steps 

            # explore neighbors
            visited.add((row,col))

            for dr,dc in directions:
                new_row = row+dr
                new_col = col+dc
                q.append([new_row,new_col,steps+1])


        return -1 
