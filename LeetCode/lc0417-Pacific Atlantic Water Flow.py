# DFS - time:O(mn), space:O(mn)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,visited, prevH):
            # base case
            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited or heights[r][c] < prevH):
                return

            visited.add((r,c))

            dfs(r+1,c, visited, heights[r][c])
            dfs(r,c+1, visited, heights[r][c])
            dfs(r-1,c, visited, heights[r][c])
            dfs(r,c-1, visited, heights[r][c])

            

        for c in range(cols):
            dfs(0,c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r,0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        result = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in atl:
                    result.append([i,j])

        return result     
