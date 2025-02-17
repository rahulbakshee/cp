# https://leetcode.com/problems/valid-parentheses/
# time:O(n), space:O(n)
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




# i did by myself on Feb 17, 2025
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = dict()
        mapping["]"] = "["
        mapping[")"] = "("
        mapping["}"] = "{"
        
        stack = []
        for char in s:
            if char  in "[({":
                stack.append(char)
            else: # ")}]"
                if not stack or stack.pop() != mapping[char]:
                    return False
                
        return True if not stack else False
