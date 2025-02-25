class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in blocks[r//3, c//3]):
                        return False
                    
                    # if current number is not there in any of the sets
                    # then update those sets with this number
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    blocks[r//3, c//3].add(board[r][c])
        return True
                    









class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create three separate sets for storing numbers of sudoku cells
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # iterate over each cell
        for r in range(9):
            for c in range(9):
                # if it is not a number then continue
                if board[r][c] == ".":
                    continue

                # if it is a number, check if we have seen it in above sets
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False

                # if not seen anywhere, then add it to the above sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True
