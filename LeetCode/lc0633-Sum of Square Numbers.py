# https://leetcode.com/problems/sum-of-square-numbers/description/

# # two for loops
# # time:O(n**2), space:O(1)

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(math.ceil(math.sqrt(c))+1):
            for j in range(i, math.ceil(math.sqrt(c))+1):
                if i**2 + j**2 == c:
                    return True
        return False
        

# two pointers
# time:O(n), space:O(1)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))+1

        while left <= right:
            s = left **2 + right **2 
            if s > c:
                right -= 1
            elif s < c:
                left += 1
            else:
                return True

        return False
