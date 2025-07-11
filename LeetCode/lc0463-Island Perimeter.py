# simple counting - time:O(mn), space:O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                # land
                if grid[r][c]:
                    result += 4

                    if r > 0 and grid[r-1][c] == 1: # check top
                        result -= 2

                    if c > 0 and grid[r][c-1] == 1: # check left
                        result -= 2

        return result        


# DFS - time:O(nm), space:O(nm)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # define DFS function to go over the island from a starting point
        def dfs(r,c):
            # boundary check
            if r<0 or c<0 or r>=rows or c>=cols:
                return 1
            
            # check if water
            if grid[r][c] == 0:
                return 1    
            
            # check if cell already visited
            if (r,c) in visited:
                return 0

            # add it to visted set
            visited.add((r,c))

            peremeter = 0

            # explore its neighbors
            for dr, dc in directions:
                new_r = r + dr
                new_c = c+ dc

                peremeter += dfs(new_r, new_c)

            return peremeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i,j)


# DFS - iterative stack - time:O(mn), space:O(mn)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # define DFS function to go over the island from a starting point
        def dfs(i,j):
            nonlocal peremeter

            stack = [(i,j)]
            while stack:
                r,c = stack.pop()

                # boundary check
                if r<0 or c<0 or r>=rows or c>=cols:
                    peremeter += 1
                    continue
                
                # check if water
                if grid[r][c] == 0:
                    peremeter += 1    
                    continue
                
                # check if cell already visited
                if (r,c) in visited:
                    peremeter += 0
                    continue

                # add it to visted set
                visited.add((r,c))

                # explore its neighbors
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c+ dc

                    stack.append((new_r, new_c))

        
        peremeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    dfs(i,j)

        return peremeter



# BFS - iterative queue - time:O(mn), space:O(mn)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # define DFS function to go over the island from a starting point
        def bfs(i,j):
            nonlocal peremeter

            q = deque([(i,j)])
            while q:
                r,c = q.popleft()

                # boundary check
                if r<0 or c<0 or r>=rows or c>=cols:
                    peremeter += 1
                    continue
                
                # check if water
                if grid[r][c] == 0:
                    peremeter += 1    
                    continue
                
                # check if cell already visited
                if (r,c) in visited:
                    peremeter += 0
                    continue

                # add it to visted set
                visited.add((r,c))

                # explore its neighbors
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c+ dc

                    q.append((new_r, new_c))

        
        peremeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    bfs(i,j)

        return peremeter
