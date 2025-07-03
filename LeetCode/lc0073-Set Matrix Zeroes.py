# bruteforce
# make a copy of original matrix and set cells to zeros
# time:O(mn), space:O(mn)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        matrix_copy = [[matrix[i][j] for j in range(cols)] for i in range(rows)]
        

        # check for zeros
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    for r in range(rows):
                        matrix_copy[r][col] = 0

                    for c in range(cols):
                        matrix_copy[row][c] = 0

        # copy back the values of matrix_copy to original matrix
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = matrix_copy[i][j]


# using hashsets for storing indexes with zero values
# time:O(mn), spoace:O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # add the indexes to respective sets
                    row_set.add(r)
                    col_set.add(c)

        # iterate over the matrix once again to mark the cells as zero if indexes in either of sets
        for r in range(rows):
            for c in range(cols):
                if r in row_set or c in col_set:
                    matrix[r][c] = 0


# OPTIMAL - constant space 
# time:O(mn), space:O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = False
        rows = len(matrix)
        cols = len(matrix[0])

        # determine which rows/cols need to be zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # mark the first row as zero
                    matrix[0][c] = 0
                    # for marking col as zero
                    if r>0:
                        matrix[r][0] = 0
                    else:
                        first_row_zero = True


        # iterate over matrix once again to mark the cells zeros
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # first col
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # first row 
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
