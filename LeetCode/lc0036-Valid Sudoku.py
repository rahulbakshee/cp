class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create three separate sets for storing numbers of sudoku cells
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in cols[c]:
                    return False
                if board[r][c] in squares[(r//3, c//3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True
