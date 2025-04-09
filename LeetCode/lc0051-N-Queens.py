# time:O(n!), space:O(n^2)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 1 - build the empty board
        board = [["." for _ in range(n)] for _ in range(n)]
        # print(board)

        # 2 - start from 0th row till last row
        # explore the (row,col) to place the queen given the constraints
        cols = set()
        posDiag = set()
        negDiag = set()
        result = []


        def backtrack(r):
            # base case - row has reached boundry
            if r == n:
                temp = ["".join(row) for row in board]
                result.append(temp)
                return


            # iterate over columns
            for c in range(n):
                if c in cols or (r-c) in negDiag or (r+c) in posDiag:
                    continue

                # place my queen
                board[r][c] = "Q"
                # add column to the sets
                cols.add(c)
                # add diag values to the diagonal sets
                posDiag.add(r+c)
                negDiag.add(r-c)

                # do something
                backtrack(r+1)

                # undo something
                # unplace my queen
                board[r][c] = "."
                # remove column to the sets
                cols.remove(c)
                # remove diag values to the diagonal sets
                posDiag.remove(r+c)
                negDiag.remove(r-c)

        

        backtrack(0)
        return result
