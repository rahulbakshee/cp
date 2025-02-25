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





class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        if rows == 1 and cols == 1:
            return board[0][0] == word

        def backtrack(r, c, index):
            # 1 base case - index out of bounds
            if r <0 or c <0:
                return False
            # 2 base case - index out of bounds
            if r>= rows or c >=cols:
                return False
            # 3 base case - index out of bounds(index should go from 0 to len(words)-1)
            if index == len(word):
                return True
            # 4 base case - if current letter is not what we are looking for
            if board[r][c] != word[index]:
                return False
            # 5 base case - if current position is already visited
            if (r, c) in visited:
                return False

            # now that we have found the letter, add it to visited set
            visited.add((r,c))
            # start exploring the neighbors
            result = (backtrack(r-1, c, index+1) or # up
                        backtrack(r+1, c, index+1) or # down
                        backtrack(r, c-1, index+1) or # left
                        backtrack(r, c+1, index+1)) # rigth
                
            # remove the added visted node from visited list
            visited.remove((r, c))
            # return Found or not found - True/False
            return result

            #        (-1,0)
            # (0,-1) (0, 0) (0, 1)
            #        (1,0)
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
