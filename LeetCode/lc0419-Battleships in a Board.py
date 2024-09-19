# DFS - time:O(m*n), space:O(m*n)
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r,c):
            # base cases
            if (r<0 or r>=rows or
                c<0 or c>=cols or
                (r,c) in visited or
                board[r][c] !="X"):
                return

            visited.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            return


        ships = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X" and (i,j) not in visited:
                    dfs(i,j)
                    ships += 1

        return ships

# DFS - stack
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        stack = []
        ships = 0

        def dfs(r,c):
            stack.append((r,c))
            visited.add((r,c))
            while stack:
                row,col = stack.pop()
                for x,y in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
                    if 0<=x<rows and 0<=y<cols and (x,y) not in visited and board[x][y] == "X":
                        stack.append((x,y))
                        visited.add((x,y))


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X" and (i,j) not in visited:
                    dfs(i,j)
                    ships += 1

        return ships


# BFS - queue
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        stack = []
        ships = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col =q.popleft()
                for x,y in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
                    if 0<=x<rows and 0<=y<cols and (x,y) not in visited and board[x][y] == "X":
                        q.append((x,y))
                        visited.add((x,y))



        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X" and (i,j) not in visited:
                    bfs(i,j)
                    ships += 1

        return ships
