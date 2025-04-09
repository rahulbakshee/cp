

# # time:O(n!), space:O(n^2)
# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         # 1-  build the board
#         board = [["." for _ in range(n)] for _ in range(n)]


#         # 2 - storage for columns, pos, neg diags
#         cols = set()
#         posDiag = set()
#         negDiag = set()
#         result = []

#         def backtrack(r:int)->None:
#             # base case
#             if r == n:
#                 temp = ["".join(row) for row in board]
#                 result.append(temp)
#                 return


#             for c in range(n):
#                 if c in cols or (r+c) in posDiag or (r-c) in negDiag:
#                     continue

#                 cols.add(c)
#                 posDiag.add(r+c)
#                 negDiag.add(r-c)
#                 board[r][c] = "Q"

#                 backtrack(r+1)

#                 cols.remove(c)
#                 posDiag.remove(r+c)
#                 negDiag.remove(r-c)
#                 board[r][c] = "."


#         backtrack(0)
#         return len(result)






# time:O(n!), space:O(n)
class Solution:
    def totalNQueens(self, n: int) -> int:
        # 1-  build the board
        board = [["." for _ in range(n)] for _ in range(n)]


        # 2 - storage for columns, pos, neg diags
        cols = set()
        posDiag = set()
        negDiag = set()
        

        def backtrack(r:int)->None:
            # base case
            if r == n:
                return 1
            
            result = 0

            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                result += backtrack(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
            
            return result

        return backtrack(0)
