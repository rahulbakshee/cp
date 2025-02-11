# editorial
# time:O(n*m), space:O(1)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        if not mat or not mat[0]:
            return []

        n = len(mat)
        m = len(mat[0])

        result = []

        row, col = 0,0
        direction = 1

        while row < n and col < m:
            result.append(mat[row][col])

            if direction:
                new_row = row - 1
                new_col = col + 1
            else:
                new_row = row + 1
                new_col = col - 1

            if new_row <0 or new_row >= n or new_col<0 or new_col >= m:
                if direction:
                    row += (col == m - 1)
                    col += (col<m - 1)
                else:
                    col += (row==n - 1)
                    row += (row<n - 1)
                # flip the direction
                direction = 1- direction

            else:
                row = new_row
                col = new_col


        





        
        return result
