# time:O(mn), space:O(mn)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        result = [[board[row][col] for col in range(cols)] for row in range(rows)]

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for r in range(rows):
            for c in range(cols):
                curr = result[r][c]
                
                # check for live neighbors
                neighbors = 0
                for dr, dc in directions:
                    new_r = r+dr
                    new_c = c+dc

                    if 0<=new_r<rows and 0<=new_c<cols:
                        neighbors += result[new_r][new_c]

                # if current cell is alive
                if curr:
                    if neighbors < 2 or neighbors >3:
                        board[r][c] = 0

                # if current cell is dead
                else: 
                    if neighbors == 3:
                        board[r][c] = 1




# time:O(mn), space:O(1)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        rows = len(board)
        cols = len(board[0])

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for r in range(rows):
            for c in range(cols):
                curr = board[r][c]
                
                # check for live neighbors
                neighbors = 0
                for dr, dc in directions:
                    new_r = r+dr
                    new_c = c+dc

                    if 0<=new_r<rows and 0<=new_c<cols and abs(board[new_r][new_c]) == 1:
                        neighbors += 1

                # if current cell is alive
                if curr == 1:
                    if neighbors < 2 or neighbors >3:
                        board[r][c] = -1

                # if current cell is dead
                elif curr == 0: 
                    if neighbors == 3:
                        board[r][c] = 2



        # correct the baord by replacing -1 and 2
        for r in range(rows):
            for c in range(cols):
                if board[r][c] >0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
