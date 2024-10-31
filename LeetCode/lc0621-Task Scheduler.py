# time:O(nlog26) = O(n)
# space:O(26) for heap and q = O(1)
from collections import Counter
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a counter dict of key:val pairs where key is A/B/C and val is freq
        counter = Counter(tasks)

        # create a maxHeap
        maxHeap = [-1*val for key, val in counter.items()]
        heapq.heapify(maxHeap)

        # queue
        q = deque() # (-val, availTime)

        time = 0
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1+ heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])

            
            if q and q[0][1] <= time:
                popped = q.popleft()[0]
                heapq.heappush(maxHeap, popped)

        return time

