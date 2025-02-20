# time:O(mn), space:O(mn)

# BFS-queue
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
                
        rows = len(mat)
        cols = len(mat[0])
        
        result = [row[:] for row in mat]
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        q = deque()
        

        # add each cell with 0 to the queue
        for r in range(rows):
            for c in range(cols):
                if result[r][c] == 0:
                    q.append((r,c,0)) # (row,col,level) 
                    visited.add((r,c))
                    
                    
        
        # process each cell using BFS-queue
        while q:
            row, col, level = q.popleft()
            
            for dr,dc in directions:
                new_row = row+dr
                new_col = col+dc
                if not(new_row<0 or new_row>=rows or 
                       new_col<0 or new_col>=cols or 
                       (new_row,new_col) in visited):
                    
                    # update matrix
                    result[new_row][new_col] = level+1
                    
                    # add it to visited
                    visited.add((new_row,new_col))
            
                    # start adding it to q for exploration
                    q.append((new_row, new_col, level+1))
                    
                    
                
        return result
