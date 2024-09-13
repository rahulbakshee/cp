# time:O(1), space:O(1)
class Solution:
    def coloredCells(self, n: int) -> int:
        return n**2 + (n-1)**2
