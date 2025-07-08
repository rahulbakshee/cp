"""using heapq and sorting
sort intervals and initiaize a minheap. iterate over sorted intervals.
we will add the meetings using END TIME to the minHeap - REMEBER
if minHeap empty-nothing to compare so add end Time of interval and continue
otherwise(minHeap non empty) check if minHeap's top(earlier stored end time) 
is less than /equal to upcoming start time. if yes, then free the room i.e. 
pop the earlier stored element.
insert the upcoming interval's end time in any case.
return the len of minHeap
"""
# pichle wale ka end time agle wale ka start time

# time:O(nlogn), space:O(n)
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort the intervals and init minHeap(list)
        intervals.sort()
        minHeap = []

        for i in range(len(intervals)):
            if not minHeap:
                heapq.heappush(minHeap, intervals[i][1])
                continue

            if minHeap[0] <= intervals[i][0]:
                heapq.heappop(minHeap)
            # but in both conditions insert upcoming interval's endTime
            heapq.heappush(minHeap, intervals[i][1])

        # return the len of minHeap
        return len(minHeap)

# sorting
""" create two separate arrays of start times and end times.
sort them.
use two pointers for these arrays, start and end pointer 
start poointer simply iterates over intervals, compare the start times 
and end times to see if room is booked i.e. start time is smaller than end time.
if yes, increase the counter and increment the start pointer. 
Otherwise, if start time is greater or equal to end time - the room is free. 
decrease the counter and move the end pointer.
keep track of max_counter in evry iteration
"""
# time:O(nlogn), space:O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends =   sorted([i[1] for i in intervals])

        count, max_count = 0,0
        s, e = 0,0
        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                count += 1
            # else also covers greater than and equal to condition
            else:
                e += 1
                count -= 1

            max_count = max(count, max_count)              

        return max_count
