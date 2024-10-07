# time:O(n), space:O(n)
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            stack.append(char)

            while len(stack) >=2 and str(stack[-1] + stack[-2]) in ["BA", "DC"]:
                stack.pop()
                stack.pop()
        
        return len(stack)
