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
