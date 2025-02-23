class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        if k == 0:
            return 0

        # sort each row of input grid in reverse ordder
        for row in grid:
            row.sort(reverse=True)

        # take the last elements from the sorted rows
        result = []
        for i in range(len(grid)):
            result.extend(grid[i][:limits[i]])

        # sort all the elemnts and take only first k
        result.sort(reverse=True)
        return sum(result[:k])
