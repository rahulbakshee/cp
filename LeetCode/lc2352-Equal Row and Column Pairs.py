# time:O(n^3), space:O(1)
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0

        for r in range(n):
            for c in range(n):
                match = True
                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        match = False
                        break

                count += int(match)

        return count


# time:O(n^2), space:O(n^2)
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)

        # row counter
        row_counter = collections.Counter(tuple(row) for row in grid)

        # column
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]

        return count
