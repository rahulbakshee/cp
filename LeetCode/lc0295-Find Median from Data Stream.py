# sorting - time:O(m*nlogn)
"""
addNum - just append at the end of array - time:O(1)
findMedian - sort the array - O(nlogn) n elemnets in array
           - find the middle element(s)
           - overall O(m*nlogn) m is the number of times "findMedian" func is called
"""

class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num:int)->None:
        """adds the integer num from the data stream to the data structure."""
        self.arr.append(num)

    def findMedian(self)->float:
        """ returns the median of all elements so far"""
        self.arr.sort()
        n = len(self.arr)

        if n%2:
            return self.arr[n//2]
        else:
            return (self.arr[n//2-1] + self.arr[n//2]) * 0.5


class MedianFinder:

    def __init__(self):
        self.lo = [] # maxHeap storing lower number
        self.hi = [] # mnHeap storing higher number
        

    def addNum(self, num: int) -> None:
        # 1 add directly to lo
        heapq.heappush(self.lo, -num)

        # 2 - pop from lo and push to hi
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        
        # 3- check lens
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (-self.lo[0]+self.hi[0])/2

        return -self.lo[0]        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
