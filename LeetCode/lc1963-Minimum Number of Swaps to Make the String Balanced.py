# time:O(n), space:O(1)
class Solution:
    def minSwaps(self, s: str) -> int:
        if not s:
            return True

        close, max_close = 0,0
        for char in s:
            if char == "[":
                close -=1
            else:
                close += 1

            max_close = max(max_close, close)

        return math.ceil(max_close/2)
