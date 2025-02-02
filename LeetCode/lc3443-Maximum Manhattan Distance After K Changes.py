# time:O(n), space:O(1)
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def manhat(x1,y1):
            return abs(x1) + abs(y1)
    
        x,y = 0,0
        max_manhat = 0
        moves = 1

        for direction in s:
            if direction == "N":
                y += 1
            elif direction == "S":
                y -= 1
            elif direction == "W":
                x += 1
            else:# E
                x -= 1

            curr_manhat = manhat(x,y)
            max_manhat = max(max_manhat, curr_manhat, min(moves, curr_manhat+(k*2)))

            moves += 1

        return max_manhat
