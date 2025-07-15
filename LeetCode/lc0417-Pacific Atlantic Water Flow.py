"""DFS from Ocean Borders to inner cells - time:O(mn), space:O(mn)
💡 Key Idea: Instead of checking if each cell can reach both oceans, we 
start DFS from the oceans' edges and see which cells can flow into them.
WE REVERSE THE FLOW: water can only go from lower or equal height to higher 
or equal height, so we traverse "uphill" from the oceans.
- Initialize two visited sets:
    - pacific: cells that can flow to the Pacific Ocean (top and left borders).
    - atl: cells that can flow to the Atlantic Ocean (bottom and right borders).
- Run DFS from each ocean's border:
    - For Pacific: top row and left column.
    - For Atlantic: bottom row and right column.
    - In DFS, only move to neighbors with height ≥ current, since water can only
     flow from higher to lower in the reverse DFS.
 - Intersection:The result is the list of cells that exist in both pac and atl."""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        # visited set for both types
        pacific, atlantic = set(), set()
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        # visited set would be different for different oceans
        def dfs(r,c,visited,prevHeight):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            if (r,c) in visited:
                return

            if heights[r][c] < prevHeight:
                return

            visited.add((r,c))
            for dr, dc in directions:
                new_r = r+dr
                new_c = c+dc
                dfs(new_r, new_c, visited, heights[r][c])

        
        # call dfs on two different oceans borders
        # left and right borders
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])


        # top and bottom borders
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    result.append((r,c))

        return result



# BFS - time:O(mn), space:O(mn)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        # visited set for both types
        pacific, atlantic = set(), set()
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        # create two queues for each ocean appending all border cells
        atlantic_q = deque()
        pacific_q = deque()

        for r in range(rows):
            atlantic_q.append((r, cols-1))
            pacific_q.append((r,0))
        
        for c in range(cols):
            atlantic_q.append((rows-1,c))
            pacific_q.append((0,c))
            
        def bfs(queue):
            visited = set()
            while queue:
                r,c = queue.popleft()
                visited.add((r,c))

                for dr, dc in directions:
                    new_r = r+dr
                    new_c = c+dc
                    if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols:
                        continue
                    if (new_r,new_c) in visited:
                        continue
                    if heights[new_r][new_c] < heights[r][c]:
                        continue

                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))            
            
            return visited


        atlantic_reachable = bfs(atlantic_q)
        pacific_reachable = bfs(pacific_q)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic_reachable and (r,c) in pacific_reachable:
                    result.append((r,c))

        return result

