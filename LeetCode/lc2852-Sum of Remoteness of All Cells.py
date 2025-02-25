# using DFS-recursive
# time:O(n^2), space:O(n^2)
class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        
        # step 3 - define dfs recursive function
        def dfs(row, col, arr):
            # add current cell value to the arr
            arr[0] += grid[row][col]

            # add the increment tot he reachable connected components counter
            arr[1] += 1

            # mark the cell as visited
            grid[row][col] = -1

            # explore all directions
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for dx, dy in dirs:
                new_row = row+dx
                new_col = col+dy
                # check if this new coordinate in boundry/valid/unblocked
                if 0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and grid[new_row][new_col] != -1:
                    # call dfs giving it new cordinates
                    dfs(new_row, new_col, arr)
        
        
        # step1 - find total sum of all the unblocked cells
        total_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    total_sum += grid[i][j]
                    
        # step2 - calculate remoteness by starting from the unblocked cell
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    # arr[0] is sum of values, arr[1] is number of reachable connected cells
                    arr = [0,0] 
                    dfs(i,j, arr)
                    result += (total_sum-arr[0]) *arr[1]


        return result


# using BFS-iterative using a Queue
# time:O(n^2), space:O(n^2)
class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        # step3 - define the bfs
        def bfs(i,j,total_sum):
            comp_sum = grid[i][j]
            comp_size = 1
            grid[i][j] = -1

            q = deque([(i,j,)])
            while q:
                curr_row, curr_col = q.popleft()

                # explore all dirs
                dirs = [(0,-1), (0,1), (-1,0), (1,0)]
                for dx,dy in dirs:
                    new_row = curr_row + dx
                    new_col = curr_col + dy
                    # check if new coordinate is valid
                    if 0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and grid[new_row][new_col] != -1:
                        q.append((new_row, new_col))
                        comp_sum += grid[new_row][new_col]
                        comp_size += 1
                        grid[new_row][new_col] = -1

            return (total_sum - comp_sum) * comp_size


        # step1 - calculate total_sum of all the cells
        total_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    total_sum += grid[i][j]

        # step2 - calculate remoteness 
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    result += bfs(i,j,total_sum)

        return result
