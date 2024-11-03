# time:O(rlogk) - r is len of ranks, k is max of ranks
# space:O(1)
import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # time[i] = rank[i] * num_car**2
        def feasible(time:int)->bool:
            # returns True if all the cars can be repaired in "time" time 
            # else False
            total_repaired = 0
            for rank in ranks:
                total_repaired += int(math.sqrt(time/rank))

            return total_repaired >= cars            


        # init the left and right boundaries
        left = 0
        right = max(ranks) * cars **2
        result = 0
        while left <= right:
            mid = left + (right-left)//2
            if feasible(mid):
                result = mid
                right = mid-1
            else:
                left = mid+1
        
        return result
