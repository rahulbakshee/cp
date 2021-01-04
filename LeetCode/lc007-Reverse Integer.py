#  https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            new = str(0-x)
            new = 0 - int(new[::-1]) 
            if new > 2**31-1 or new < -2**31 : return 0
            else: return new
        if x > 0:
            new = str(x)
            new = int(new[::-1]) 
            if new > 2**31-1 or new < -2**31 : return 0
            else: return new
