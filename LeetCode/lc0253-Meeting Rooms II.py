import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = []

        for interval in intervals:
            if not minHeap:
                heapq.heappush(minHeap, interval[1])
                continue
            if minHeap[0] <= interval[0]:
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap, interval[1])
            
        return len(minHeap)


# time:O(nlogn), space:O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        s, e = 0, 0
        rooms = 0
        max_rooms = 0

        while s < len(starts):
            if starts[s] < ends[e]:
                rooms += 1
                s += 1
            else: # starts[s] >= ends[e]
                rooms -= 1
                e += 1
            max_rooms = max(max_rooms, rooms)

        return max_rooms
                
