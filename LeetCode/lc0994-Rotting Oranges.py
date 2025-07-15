"""Multi-Source BFS - time:O(mn), space:O(mn)
Initialize:
    - Traverse the grid to:
        - Count the number of fresh oranges.
        - Add positions of all rotten oranges to a queue — 
        these are the starting points for BFS.
BFS Traversal:
    - Use a queue to perform BFS level by level, representing 
    each minute that passes.
    - For each rotten orange in the queue, rot all adjacent 
    fresh oranges (up/down/left/right) and add them to the queue.
    - After each BFS level (minute), increment the time counter.
Final Check:
    - If all fresh oranges are rotted during BFS, return the total 
    time (BFS depth).
    - If any fresh oranges remain unrotted (i.e., unreachable), 
    return -1.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get dimensions of input grid
        rows = len(grid)
        cols = len(grid[0])

        # add fresh oranges to the fresh variable 
        # add rotten to the queue for BFS
        fresh = 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))


        # start multi source BFS
        time = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        while q and fresh>0:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    new_r = r+dr
                    new_c = c+dc
                    if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols:
                        continue
                    if grid[new_r][new_c] in [0,2]: # REMEMBER
                        continue
                    # mark rotten and add to q
                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c))

                    fresh -= 1
                    
            time += 1

        if fresh == 0:
            return time
        else:
            return -1
