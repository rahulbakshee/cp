# https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/2324351/python-explained/
# https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/1079154/python-o-m-n-solution-explained/
# time:O(m+n), space:O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        
        # start from the bottom left corner
        i, j = m-1, 0
        while i >= 0 and j < n:
            # move up
            if matrix[i][j] > target:
                i -= 1
            # move right
            elif matrix[i][j] < target:    
                j += 1
            else:
                return True

        return False
