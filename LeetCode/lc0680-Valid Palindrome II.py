# time:O(n), space:O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                    with_s_left = s[left:right]
                    without_s_left = s[left+1: right+1]
                    return with_s_left == with_s_left[::-1] or without_s_left == without_s_left[::-1]
                    
            left += 1
            right -=1
        return True
