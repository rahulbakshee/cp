# https://leetcode.com/problems/sqrtx/

# bruteforce
# space O(1), time O(sqrt(n))
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x

        for i in range(2, x+1):
            if i*i == x:
                return i
            elif i*i > x:
                return i-1



# binary search
# space O(1), time O(log n)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0,1]:
            return x
        
        left, right = 2, x

        while left < right:
            mid = left + (right-left)//2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid +1

        return left - 1
