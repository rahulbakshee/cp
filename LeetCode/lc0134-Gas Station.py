# bruteforce - time:O(n^2), space:O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        for start in range(len(gas)):
            total = 0
            completed = True
        

            for i in range(len(gas)):
                index = (start+i) % len(gas)

                total += gas[index] - cost[index]

                if total < 0:
                    completed = False
                    break

            if completed:
                return start

        return -1        



# greedy - time:O(n), space:O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i+1

        return start
