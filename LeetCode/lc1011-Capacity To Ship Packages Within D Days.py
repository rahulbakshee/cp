# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

# bruteforce linear search, Time Limit Exceeded
# space O(1), time O(n^2)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weight, max_weight = max(weights), sum(weights)
        print("min_weight, max_weight", min_weight, max_weight)
        
        for capacity in range(min_weight, max_weight+1):
            print("capacity", capacity)
            sum_w = 0
            sum_d = 1

            for weight in weights:
                sum_w += weight
                if sum_w > capacity:
                    sum_d += 1
                    sum_w = weight
            
            print("days required", sum_d)
            
            if sum_d <= days:
                return capacity
            
  

# binary search
# space O(1), time O(nlogn) --> not sure about this
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(capacity)-> bool: # whether it is feasible to ship all packages within days days 
            sum_w = 0
            sum_d = 1
            
            for weight in weights:
                sum_w += weight
                if sum_w > capacity:
                    sum_d += 1
                    sum_w = weight

                    if sum_d > days:
                        return False
            return True

        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right-left)//2 

            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
