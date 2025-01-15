# time:O(m*n), space:O(m*n)
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # possible directions
        dirs = [(0,1), (0,-1), (-1,0), (1,0)]
        rows, cols = len(grid), len(grid[0])

        # find starting position
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    start = (r,c)
                    break

        
        # BFS
        from collections import deque
        queue = deque([start])
        away = 1

        while queue:
            # process all cells at current level
            for _ in range(len(queue)):
                row, col = queue.popleft()

                # try all directions
                for dx, dy in dirs:
                    new_row = row+dx
                    new_col = col+dy

                    # check if the new position is not obstacle
                    if ((0<=new_row<rows) and (0<=new_col<cols) and (grid[new_row][new_col] != "X")):
                        # check for food
                        if grid[new_row][new_col] == "#":
                            return away

                        # mark this cell as visited and add to queue
                        grid[new_row][new_col] = "X"
                        queue.append((new_row, new_col))
            # add to steps
            away += 1
        # no path found
        return -1
