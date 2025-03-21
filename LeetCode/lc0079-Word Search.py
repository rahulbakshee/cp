# time:O(n.3^l) - n -number of cells, l-max len of word to be matched
# space:O(l)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, suffix):
            # base case
            if len(suffix) == 0:
                return True
            
            # check for boundry
            if row<0 or row>= len(board) or col<0 or col>=len(board[0]) or board[row][col]!=suffix[0]:
                return False

            # first step of backtrack - mark the current state with #
            board[row][col] = "#"

            # explore the neighboring directions
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                new_row = row+dr
                new_col = col+dc
                if backtrack(new_row, new_col, suffix[1:]):
                    return True

            # second step of backtrack - unmark "#" and assign the char as is to the grid
            board[row][col] = suffix[0]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,word):
                    return True
        
        return False

# below one is done by me - 
# time:O(N*3^L), space:O(L)
# where N is the number of cells in the board and L is the length of the word to be matched.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, index):
            # base case
            # check for word index out of bound
            if index >= len(word):
                return True
            
            # check for board index out of bound
            if row<0 or row>=rows or col<0 or col>=cols:
                return False

            # check for current character matching
            if board[row][col] != word[index]:
                return False


            # mark the current cell as visited
            board[row][col] = "#"

            # explore its neighbors
            for dr, dc in directions:
                new_row = row+dr
                new_col = col+dc
                
                # do something
                if backtrack(new_row, new_col, index+1):
                    return True

            # undo something
            board[row][col] = word[index]
            return False

        
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True

        return False
