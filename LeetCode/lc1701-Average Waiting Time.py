# https://leetcode.com/problems/average-waiting-time/description/

# time:O(n), space:O(1)
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start = 0
        end = 0
        wait = 0
        for customer in customers: 
            a, t = customer 
            if start == 0 or a > end:
                start = a 
            if a <= end:
                start = end

            end = start + t
            wait += end-a
        return wait/len(customers)
