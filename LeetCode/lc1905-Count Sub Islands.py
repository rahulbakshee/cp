# DFS - recursion
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(row, col):
            # base case
            if (row<0 or row>=rows or
                col<0 or col>=cols or
                (row,col) in visited or
                grid2[row][col] == 0):
                return True


            # update visited set
            visited.add((row,col))

            # check in grid1 if it is land or water
            if grid1[row][col] == 0:
                result = False
            else:
                result = True

            # explore neighbors
            for dr, dc in directions:
                new_row = row+dr
                new_col = col+dc
                result = dfs(new_row, new_col) and result

            return result


        directions = [(0,1), (1,0), (-1, 0), (0,-1)]
        rows = len(grid1)
        cols = len(grid1[0])
        visited = set()
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and (r,c) not in visited:
                    count += dfs(r,c)    

        return count


# DFS - stack
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(r,c):
            stack = [(r, c)]
            visited.add((r,c))
            result = True

            while stack:
                row, col = stack.pop()

                if grid1[row][col] == 0:
                    result = False

                for dr, dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if not (new_row<0 or new_row>=rows or
                            new_col<0 or new_col>=cols or
                            (new_row,new_col) in visited or
                            grid2[new_row][new_col] == 0):
                        stack.append((new_row, new_col))
                        visited.add((new_row, new_col))

            return result


        directions = [(0,1), (1,0), (-1, 0), (0,-1)]
        rows = len(grid1)
        cols = len(grid1[0])
        visited = set()
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and (r,c) not in visited:
                    if dfs(r,c):
                        count += 1

        return count
