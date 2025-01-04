#EDITORIAL


# time:O(n+l), space:O(l), n-shift, l-string shift operation
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left,right = 0, 0
        for direction, amount in shift:
            # left
            if direction == 0:
                left += amount
            # right
            else:
                right += amount

        left = left % len(s)
        right = right % len(s) 
        
        # check which is higher and perform shift
        if left > right:
            k = left-right
            s = s[k:] + s[:k]
        elif right > left:
            k = right-left
            s = s[-k:] + s[:-k]
        return s
