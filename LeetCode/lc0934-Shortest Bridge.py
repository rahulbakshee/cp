class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # input - 
            # grid - n X n
            # 1 - land, 0 - water, only 0 and 1 in input
            # grid - empty - no
            # num islnds - 2
            # size - n - 100

        # output - 
            # num of 0 to flip toi connect two islands
            # atleast 1 

        # approach - start DFS on first island
        # then BFS from first island to second island

        self.n = len(grid)
        self.grid = grid
        self.visited = set()
        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]

        # dfs
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    self.dfs(i, j)
                    return self.bfs()


    def dfs(self, r, c):
        if r<0 or r>=self.n or c<0 or c>=self.n:
            return
        if self.grid[r][c] == 0:
            return
        if (r,c) in self.visited:
            return 

        self.visited.add((r, c))

        for dr, dc in self.directions:
            new_r, new_c = r+dr, c+dc
            self.dfs(new_r, new_c)


    def bfs(self):
        level = 0
        queue = deque(self.visited)
        while queue:

            for _ in range(len(queue)):
                r, c = queue.popleft()
            
                for dr, dc in self.directions:
                    new_r, new_c = r+dr, c+dc
                    if (0<=new_r<self.n and 
                        0<=new_c<self.n and 
                        (new_r, new_c) not in self.visited):
                        if self.grid[new_r][new_c] == 1:
                            return level
                        queue.append((new_r, new_c))
                        self.visited.add((new_r, new_c))

            level += 1

        return -1
