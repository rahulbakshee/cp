# using 2 queues
# time:O(n), space:O(n)
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = deque(), deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                R.append(i)
            else:
                D.append(i)

        # voting session
        while R and D:
            senate_R = R.popleft()
            senate_D = D.popleft()

            if senate_D < senate_R:
                D.append(senate_D + len(senate))
            else:
                R.append(senate_R + len(senate))

            
        return "Radiant" if R else "Dire"
