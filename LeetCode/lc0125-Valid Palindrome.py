# https://leetcode.com/problems/valid-palindrome/description/

# space: O(1), time O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                 left = left +1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].upper() == s[right].upper():
                left += 1
                right -= 1
            else:
                return False
        return True

