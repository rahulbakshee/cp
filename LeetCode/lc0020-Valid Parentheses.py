# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(', ']':'[', '}':'{'}
        
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if stack == [] or d[i] != stack.pop():
                    return False
                
            else:
                return False
        if stack == []: return True
        else: return False
