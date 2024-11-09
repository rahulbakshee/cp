# time:O(n), space:O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        # gas =  [1,2, 3, 4, 5]
        # cost = [3,4, 5, 1, 2]
        # remain=[-2,-2,-2,3,3]
 
        total_gain = 0
        curr_gain = 0
        index = 0

        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            # if it is a valley
            if curr_gain < 0:
                curr_gain = 0
                index = i+1

        return index if total_gain >=0 else -1
