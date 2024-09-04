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

        
