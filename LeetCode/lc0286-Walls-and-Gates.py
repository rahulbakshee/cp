# https://leetcode.ca/2016-09-11-286-Walls-and-Gates/
# https://neetcode.io/problems/islands-and-treasure
# trick is to start from the gate(grid[i][j] == 0


# time:O(mn), space:O(mn)
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # 0 - measure the dimensions of the matrix
        rows = len(rooms)
        cols = len(rooms[0])
        q = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()

        # 1 - add all the gates to the queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        
        # 2 - BFS
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                # mark the distance
                rooms[r][c] = distance

                # explore neighbors
                for direction in directions:
                    dr, dc = direction
                    new_r = r + dr
                    new_c = c + dc

                    # check for boundry, not in visited, obstacle
                    if not (new_r<0 or new_r>=rows or
                            new_c<0 or new_c>=cols or
                            (new_r, new_c) in visited or
                            rooms[new_r][new_c] in [-1,0]):
                            
                            q.append((new_r, new_c))
                            visited.add((new_r, new_c))

            distance += 1
