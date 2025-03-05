class Solution:
    def coloredCells(self, n: int) -> int:
        result = 1
        while n:
            result = result + 4*(n-1)
            n -= 1


        return result


class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n*(n-1)*2


# time:O(1), space:O(1)
class Solution:
    def coloredCells(self, n: int) -> int:
        return n**2 + (n-1)**2
