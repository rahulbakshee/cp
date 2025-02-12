# time:O(r^2), space:O(r)
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured]

        for row in range(1, query_row+1):
            curr_row = [0] * (row+1)

            for i in range(row):
                extra = prev_row[i] - 1
                if extra > 0:
                    curr_row[i] += 0.5 * extra
                    curr_row[i+1] += 0.5 * extra

            prev_row = curr_row
        return min(1, prev_row[query_glass])
                    
