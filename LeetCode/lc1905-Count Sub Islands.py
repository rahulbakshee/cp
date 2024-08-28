# time:O(n*m), space:O(n*m)
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r, c):
            # base case
            if r<0 or c<0 or r>=rows or c>= cols or grid2[r][c] == 0 or (r,c) in visited:
                return True

            if grid1[r][c] == 0:
                return False

            visited.add((r,c))
            # recurse
            return dfs(r-1,c) & dfs(r+1,c) & dfs(r,c-1) & dfs(r,c+1) # usage of & instead of "and"
            # In python, x and y means if x if False, return x. otherwise, return y. 
            # So only if x is True then y can be executed. 
            # x or y: if x if True, return x. otherwise return y. That means if x is True, y will not be executed.
            # So in the dfs(). we can only use &. Cause it is the bit counting. 

    
        counter = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and (r, c) not in visited and dfs(r,c):
                    counter += 1

        return counter
