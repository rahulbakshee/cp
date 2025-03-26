# sorting
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid = [col for row in grid for col in row]

        grid.sort()

        median = grid[len(grid)//2]

        ops = 0
        for i in range(len(grid)):
            if grid[i] % x != median % x:
                return -1

            ops += abs(median - grid[i]) // x 

        return ops
