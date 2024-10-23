###### EDITORIAL
# line sweep
# time:O(n^2), space:O(n)
from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.diff[startTime] = self.diff.get(startTime, 0) + 1
        self.diff[endTime] = self.diff.get(endTime, 0) - 1

        curr = res = 0
        for delta in self.diff.values():
            curr += delta
            res = max(curr, res)

        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
