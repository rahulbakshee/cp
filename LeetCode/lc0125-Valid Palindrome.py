# https://leetcode.com/problems/valid-palindrome/description/

# time-O(n), space-O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isInRange(char):
            if ((ord("0") <= ord(char) <= ord("9")) or
                (ord("A") <= ord(char) <= ord("Z")) or
                (ord("a") <= ord(char) <= ord("z"))):
                return True
            else:
                return False
        
        news = ""
        for char in s:
            if isInRange(char): # alpha-numeric
                news += char.lower() 

        return news == news[::-1]


# time O(n), space: O(1)
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

