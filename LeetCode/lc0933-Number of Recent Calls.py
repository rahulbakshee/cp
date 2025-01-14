# time:O(1), space:O(1) - editorial
from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()
        
    def ping(self, t: int) -> int:
        # append the given timestamp
        self.queue.append(t)

        # remove the older timestamps
        while self.queue[0] + 3000 < t:
            self.queue.popleft()

        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
