# djikstra time:O(mnlogmn), space:O(mn) - mn-heights
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        # min of something dict
        min_efforts = {(r,c):float("inf") for r in range(rows) for c in range(cols)}
        min_efforts[(0,0)] = 0

        # minHeap 
        minHeap = [[0,0,0,]] # [eff, r, c]
        while minHeap:
            eff, r, c = heapq.heappop(minHeap)

            if (r,c) == (rows-1,cols-1):
                return eff

            # explore neighbors
            for dr,dc in directions:
                new_r = r+dr
                new_c = c+dc

                if 0<=new_r<rows and 0<=new_c<cols:
                    mad = max(eff, abs(heights[r][c]- heights[new_r][new_c]))
                    if mad < min_efforts[(new_r,new_c)]:
                        min_efforts[(new_r,new_c)] = mad

                        heapq.heappush(minHeap, [mad, new_r, new_c])
