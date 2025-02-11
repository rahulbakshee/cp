# time:O(n^2/m), space:O(n)
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            parti = s.find(part)

            s = s[:parti] + s[parti+len(part):]

        return s



# time:O(n*m), space:O(n+m)
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for char in s:
            stack.append(char)

            if len(stack) >= part_len and "".join(stack[-part_len:]) == part:
                for _ in range(part_len):
                    stack.pop()

        return "".join(stack)
