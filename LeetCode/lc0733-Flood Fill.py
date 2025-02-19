# DFS recursion  - I solved my self on 02/19/2025

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(sr,sc):
            # base case - boundaries, color of pizel in image
            if sr<0 or sr>=rows or sc<0 or sc>=cols or image[sr][sc] == color:
                return
            
            # start processing if the curr color is accepted_color
            if image[sr][sc] == accepted_color:

                # change the  color of curr pixel
                image[sr][sc] = color

                # start exploring the neighbors of curr pizel
                for dr, dc in directions:
                    new_sr = sr+dr
                    new_sc = sc+dc

                    dfs(new_sr, new_sc)        

        
        if not image:
            return []
        
        rows = len(image)
        cols = len(image[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        accepted_color = image[sr][sc]
        
        dfs(sr,sc)
        return image

# DFS with stack
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        
        rows = len(image)
        cols = len(image[0])
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        starting_color = image[sr][sc]
        
        stack = [[sr,sc]]
        if starting_color!= color:
            while stack:
                row, col = stack.pop()
                # check for bounadries
                if row<0 or row>=rows or col<0 or col>=cols:
                    continue
                
                # check for current color == starting color
                if image[row][col] == starting_color:
                    
                    # change the color of current cell
                    image[row][col] = color
                    
                    # start exploring the neighbors
                    for dr, dc in directions:
                        new_row = row+dr 
                        new_col = col+dc
                        
                        stack.append([new_row, new_col])             
                    
        return image
        




###########################################################################################################

# dfs - time:O(m*n), space:O(m*n) for dfs call stack
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        curr_color = image[sr][sc]
        if color == curr_color:
            return image
        

        def dfs(r, c):
            # base cases
            if r <0 or r>=len(image) or c<0 or c>=len(image[0]):
                return 

            if image[r][c] == curr_color:
                image[r][c] = color
                dfs(r-1, c)
                dfs(r, c-1)
                dfs(r+1, c)
                dfs(r, c+1)

        dfs(sr, sc)
        return image




# bfs - time:O(m*n), space:O(m*n)
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        new_color = color
        curr_color = image[sr][sc]

        if curr_color != new_color:
            q = deque([(sr,sc)])
            while q:
                r, c = q.popleft()
                image[r][c] = new_color

                for x,y in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if 0<=x<rows and 0<=y<cols and image[x][y] == curr_color:
                        q.append((x,y))


        return image



# DFS using stack - time:O(m*n), space:O(m*n)+callstack
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        curr_color = image[sr][sc]
        new_color = color

        if curr_color != new_color:
            stack = [(sr, sc)]
            while stack:
                r,c = stack.pop()
                image[r][c] = new_color

                for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0<=x<rows and 0<=y<cols and image[x][y] == curr_color and image[x][y] != new_color:
                        stack.append((x,y))

        return image
