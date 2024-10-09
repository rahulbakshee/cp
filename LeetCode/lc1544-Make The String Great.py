class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue
            
            prev = stack[-1]
            if ((ord(char) - ord("a") == ord(prev) - ord("A")) or
                (ord(prev) - ord("a") == ord(char) - ord("A"))):
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
