# cracking faang
# time:O(n), space:O(n)
class Solution:
    def calculate(self, s: str) -> int:
        curr, result = 0, 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)

            elif char in ["+", "-"]:
                result += sign * curr
                sign = 1 if char == "+" else -1
                curr = 0

            elif char == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0

            elif char == ")":
                result += sign * curr
                result *= stack.pop()
                result += stack.pop()
                curr = 0

        return result + sign * curr
