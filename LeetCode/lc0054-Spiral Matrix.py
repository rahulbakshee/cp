# time:O(m*n), space:O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # original [row, col]
        # right - [row, col+1]
        # bottom - [row+1, col]
        # left - [row-1, col]
        # up - [row, col-1]

        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        result = []
        while left < right and top < bottom:
            # left to right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            # from top to bottom
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            # from right to left
            for i in range(right-1, left-1, -1):
                result.append(matrix[bottom-1][i])
            bottom -= 1

            # from bottom to top
            for i in range(bottom-1, top-1, -1):
                result.append(matrix[i][left])
            left += 1

        return result
