# time:O(n), space:O(n)
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            # if number, then pop from stack
            if ord("0") <= ord(char) <= ord("9"):
                if stack:
                    stack.pop()

            else:
                stack.append(char)

        return "".join(stack)
                
