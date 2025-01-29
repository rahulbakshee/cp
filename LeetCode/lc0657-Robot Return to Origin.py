# time:O(n), space:O(1)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up = 0
        left = 0
        for move in moves:
            if move == "U":
                up += 1
            elif move == "D":
                up -= 1
            elif move == "L":
                left += 1
            else:
                left -= 1
            
        return up == 0 and left == 0
