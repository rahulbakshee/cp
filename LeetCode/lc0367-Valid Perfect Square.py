# binary search
# time:O(logn), space:O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left, right = 2, num
        while left <= right:
            mid = left + (right-left)//2
            if mid * mid > num:
                right = mid-1
            elif mid*mid < num:
                left = mid+1
            else:
                return True

        return False
