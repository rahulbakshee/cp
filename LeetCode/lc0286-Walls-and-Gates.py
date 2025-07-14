"""Multi-Source BFS - time:O(mn), space:O(mn)
“I use multi-source BFS, starting from all gates at once. 
BFS ensures we find the minimum distance to the nearest gate,
layer by layer. We only update a room if it's still INF, 
ensuring we don't overwrite shorter paths.”

Instead of searching from an empty room to the gates, how about searching 
the other way round? In other words, we initiate breadth-first search (BFS) 
from all gates at the same time. Since BFS guarantees that we search all 
rooms of distance d before searching rooms of distance d + 1, the distance 
to an empty room must be the shortest.
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # 0 - measure the dimensions of the matrix
        rows = len(rooms) 
        cols = len(rooms[0])
        
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        # 1 - add all the gates to the queue
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0: # gate
                    visited.add((i,j))
                    q.append((i,j))

        distance = 0
        # 2 - bfs - starting from all the gates simultatneously
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                # mark distance
                rooms[r][c] = distance

                # explore neighbors
                for dr, dc in directions:
                    new_r = r+dr
                    new_c = c+dc

                    if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols:
                        continue
                    if rooms[new_r][new_c] in [-1,0]:
                        continue
                    if (new_r,new_c) in visited:
                        continue
                    q.append((new_r,new_c))
                    visited.add((new_r,new_c))

            distance += 1
