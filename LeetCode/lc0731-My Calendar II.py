########## EDITORIAL
# line sweep
# time:O(n^2), space:O(n)
from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        # number of bookings at each point
        self.booking_count = SortedDict() 

        # max overlapped bookings allowed
        self.k = 2   

    def book(self, start: int, end: int) -> bool:
        # increase and decrease the booking count at start and end
        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1

        overlapped = 0

        # prefix sum of bookings
        for count in self.booking_count.values():
            overlapped += count

            if overlapped > self.k:
                self.booking_count[start] -=1
                self.booking_count[end] +=  1

                # remove entries if their count becomes zero
                if self.booking_count[start] == 0:
                    del self.booking_count[start]
                return False

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
