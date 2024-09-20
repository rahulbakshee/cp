# DFS - time:O(mn), space:O(mn)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] != "O":
                return

            board[r][c] = "T"  
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # 1 - DFS - capture unsurrounded regions (O->T)
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i in [0,rows-1] or j in [0, cols-1]):
                    dfs(i,j)


        # 2 - O->X
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # 3 - T-> X
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"

        
