# neetcode

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # init a RESULT matrix of size n^2
        # init 4 boundaries for top, left, right, bottom
        # start from top left and move towards right boundary
        # once boundary reached, adjust the boundary shorter.
        # keep going from top to bottom
        # ...
        result = [[0] *n  for _ in range(n)]
        
        top = 0
        left = 0
        right = n-1
        bottom = n-1

        num = 1

        while left<=right and top <= bottom:
            
            # from left to right
            for col in range(left, right+1):
                result[top][col] = num
                num +=1
            top += 1
            
            # from top to bottom
            for row in range(top, bottom+1):
                result[row][right] = num
                num += 1
            right -= 1

            # from right to left
            for col in range(right, left-1, -1):
                result[bottom][col] = num
                num += 1
            bottom -= 1

            # from bottom to top
            for row in range(bottom, top-1, -1):
                result[row][left] = num
                num += 1
            left += 1

        return result      


        # time:O(n^2), space:O(1)



        # Top - 1,2,3
        #           Right

        #       1,2,3
        # top -   R
            
