# using hashmap
# time:O(1), space:O(n)
class Logger:

    def __init__(self):
        self.hashmap = dict() # key=strmsg, val=int timestamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hashmap:
            self.hashmap[message] = timestamp + 10
            return True
        else:
            if timestamp >= self.hashmap[message]:
                self.hashmap[message] = timestamp + 10
                return True
            else:
                return False



# using QUEUE + SET
# time:O(n), space:O(n)
from collections import deque

class Logger:

    def __init__(self):
        self.hashset = set()
        self.q = deque()
        self.diff = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # clean up expired messages using sliding window of timestamps
        while self.q:
            msg, ts = self.q[0]
            if ts + self.diff <= timestamp:
                self.q.popleft()
                self.hashset.remove(msg)
            else:
                break

        # check for upcoming msg and timestamp
        if message not in self.hashset:
            self.hashset.add(message)
            self.q.append((message, timestamp))
            return True

        else:
            return False




# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
