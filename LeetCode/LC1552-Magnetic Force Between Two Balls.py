# DID NOT UNDERSTAND THIS
# READ EDITORIAL
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def feasible(pos)->bool:
            prev_pos = position[0]
            balls_placed = 1

            for i in range(1, len(position)):
                curr_pos = position[i]

                if curr_pos - prev_pos >= pos:
                    balls_placed += 1
                    prev_pos = curr_pos
                
                if balls_placed == m:
                    return True
            return False
        
        
        position.sort()
        answer = 0
        left, right = 1, int(position[-1]/(m-1))+1
        while left < right:
            mid = left + (right-left)//2

            if feasible(mid):
                answer = mid
                left = mid+1

            else:
                right = mid

        return answer
