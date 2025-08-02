# time:O(n^2 logn^2)-> O(n^2logn) due to heap ops
# space:O(n^2) heap
# Dijkstra's algorithm to find minimum time to reach bottom-right corner in grid
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # All possible directions: right, down, left, up
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        visited = set()  # To record already visited cells
        # Min-heap to choose the next cell with minimal maximum height so far
        minHeap = [[grid[0][0],0,0]] # [current max height, row, col]
        visited.add((0,0))

        while minHeap:
            # Pop cell with smallest 'max height so far'
            h, r, c = heapq.heappop(minHeap)

            # If we've reached the bottom-right corner, return the result
            if (r,c) == (rows-1,cols-1):
                return h

            # Explore all valid neighboring cells
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                # Check bounds and whether it's unvisited
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                    # The 'max' is because you can't "arrive" at a cell before time = its value
                    # Push the new cell into the heap with updated max height so far
                    heapq.heappush(minHeap, [max(h, grid[new_r][new_c]), new_r, new_c]) 
                    visited.add((new_r, new_c))
