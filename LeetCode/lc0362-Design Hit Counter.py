# https://leetcode.com/problems/design-hit-counter/solutions/83511/python-solution-with-detailed-explanation/
from collections import deque
class HitCounter:

    def __init__(self):
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.q and self.q[0] + 300 <= timestamp:
            self.q.popleft()
        return len(self.q)

# OPTIMAL
