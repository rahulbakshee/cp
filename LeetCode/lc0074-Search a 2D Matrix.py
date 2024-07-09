# https://leetcode.com/problems/search-a-2d-matrix/description/

# time:O(logn + logm) = O(logm*n), space:O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m-1
        while left <= right:
            mid = left + (right-left)//2

            if target < matrix[mid][0]:
                right = mid-1
            elif target > matrix[mid][n-1]:
                left = mid+1
            else: # target is in the row
                break
        if left > right:
            return False

        l, r = 0, n-1
        while l <= r:
            c = l + (r-l) //2
            if matrix[mid][c] == target:
                return True
            elif target > matrix[mid][c]:
                l = c+1
            else:
                r = c-1
        return False
                    
            
# using single binary search
# time:O(log m*n)            
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1

        while left <= right:
            mid = left + (right - left) //2
            if matrix[mid//n][mid%n] > target:
                right = mid - 1
            elif matrix[mid//n][mid%n] < target:
                left = mid + 1
            else:
                return True
        return False
