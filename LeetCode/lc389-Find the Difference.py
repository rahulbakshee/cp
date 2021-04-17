# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        
        count = 0
        for i in range(len(s)):
            if s[i] != t[i] :
                count = 1
                print(t[i])
                return t[i]
            
        if count == 0:
            return t[-1]
