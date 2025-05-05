class SmallestInfiniteSet:

    def __init__(self):
        self.added_numbers = set()
        self.minHeap = []
        self.curr = 1

    def popSmallest(self) -> int:
        if len(self.minHeap):
            result = heapq.heappop(self.minHeap)
            self.added_numbers.remove(result)

        else:
            result = self.curr
            self.curr += 1

        return result

    def addBack(self, num: int) -> None:
        if num in self.added_numbers:
            return

        if num >= self.curr:
            return

        heapq.heappush(self.minHeap, num)
        self.added_numbers.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
