# time:O(m*n), space:O(m*n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        time = 0


        # add all the rotten and fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1

                elif grid[i][j] == 2:
                    q.append((i,j))



        while q and fresh >0:
            for qi in range(len(q)):
                r,c = q.popleft()
                for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    # check for boundary conditions
                    if (x<0 or x>=rows or 
                        y<0 or y>=cols or 
                        grid[x][y] != 1):
                        continue

                    # make them rotten
                    grid[x][y] = 2
                    q.append((x,y))
                    fresh -= 1

            time += 1

        if fresh >0:
            return -1
        else:
            return time
