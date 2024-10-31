# time:O(n+nlogn), space:O(n)
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we need to create a maxHeap so negate all the weights
        stones = [-1*stone for stone in stones]

        # craete maxHeap of stones
        heapq.heapify(stones)

        while len(stones)>=2:

            # keep popping from the heap and process the two stones
            x = -1*heapq.heappop(stones)
            y = -1*heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -1*(abs(x-y)))

        return -1*heapq.heappop(stones) if stones else 0
