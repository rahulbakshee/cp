# adding/inserting element to heap : time -O(log n )
# accessing the min/max element: time -O(1)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums

        # add to heap
        heapq.heapify(self.minHeap)


        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
