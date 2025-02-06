# time:O(n+m), space:O(max(n, m))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a, 2) + int(b, 2))[2:]

        x, y = int(a, 2), int(b, 2)

        while y:
            answer = x^y
            carry = (x&y) << 1
            x, y = answer, carry

        return bin(x)[2:]
