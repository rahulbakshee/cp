# time:O(n^2), space:O(n)
class MyCalendar:
    def __init__(self):
        self.bookings = [] # [start, end]

    def book(self, start, end)-> bool:
        for booking in self.bookings:
            s, e = booking
            if s<end and start<e:
                return False
        self.bookings.append([start, end])
        return True        


# # initialize the array data structure
# # keep all the bookings in the array as they come
# # as a new booking comes, check with the earlier stored unsorted bookings
# # check for overlap, if overlap then return False, else add it to the array
# # overlap-> [s1, e1], [s2, e2] --> when s1<e2 and s2<e1



# using a sorted List
# time:O(nlogn), space:O(n)
from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.bookings = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.bookings.bisect_right((start, end))
        if ((idx>0 and self.bookings[idx-1][1] > start) or
            (idx < len(self.bookings) and self.bookings[idx][0] < end)):
            return False
        self.bookings.add((start, end))
        return True





# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
