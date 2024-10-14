# time:O(nlogn + klogn), space:O(n)
import heapq
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        maxHeap = []

        # add to heap
        for num in nums:
            heapq.heappush(maxHeap, -1*num)

        # take the element from heap and then apply operation K times
        for _ in range(k):
            popped = -1*heapq.heappop(maxHeap)
            score += popped
            operated = math.ceil(popped/3)
            heapq.heappush(maxHeap, -1*operated)

        return score
