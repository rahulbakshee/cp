# time:O(mn), space:O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        row_zeros = set()
        col_zeros = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zeros.add(i)
                    col_zeros.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in row_zeros or j in col_zeros:
                    matrix[i][j] = 0

        



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        frz = False
        fcz = False

        for i in range(m):
            if matrix[i][0] == 0:
                fcz = True
                break
        
        for i in range(n):
            if matrix[0][i] == 0:
                frz = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:        
                    matrix[i][j] = 0

        if frz:
            for i in range(n):
                matrix[0][i] = 0

                            
        if fcz:
            for i in range(m):
                matrix[i][0] = 0
