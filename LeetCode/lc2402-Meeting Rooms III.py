# two minHeaps
"""
available - for storing available room numbers
used - for storing [end_time, room_number]

iterarte over meetings, sorted by start time
For each meeting:
 - Free up rooms that have finished by the current meeting's start time
    - Pop from used and push room back to available.
 - If available is not empty:
     - Assign the room with the lowest number.
     - pop from available and Push to used.
 - If no room is free:
     - Wait for the earliest finishing room from used
     - Delay the meeting to that room’s end time, preserving duration.
     - Push the new (delayed_end_time, room_number) to used.
 - Track the count of meetings per room using a counter array.
 - return highest count room 
"""
# time:O(mlogm+mlogn), space:O(n+m) - m-meetings, n-rooms
# mlogm - meetings sorting, mlogn - heap operations
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # sort meetings by start time
        meetings.sort()

        available = [i for i in range(n)] # [0,1,2,,,,n-1]
        # actually not needed to heapify coz array is sorted
        heapq.heapify(available) 

        used = [] # [end_time, room_number]

        count = [0] * n # count[n] = meetings scheduled in room n

        # iterate over meetings
        for start, end in meetings:
            # finished meetings
            while used and used[0][0] <= start:
                e, room = heapq.heappop(used)

                # allocate the freshly freed room back to available rooms
                heapq.heappush(available, room)

            # if room available
            if available:
                # pop from available and add it to used
                room = heapq.heappop(available)
                heapq.heappush(used, [end, room])

            else:
                # pop from used, and increment its start and end
                e, room = heapq.heappop(used)
                heapq.heappush(used, [e+end-start, room])
                # update the room number used
            count[room] += 1 # REMEMBER
        return count.index(max(count))
