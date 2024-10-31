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



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# implement a FindMedian class
    # def init
    # def add_num(num)-> None - adds the number to the list
    # def find_median()-> float



class MedianFinder:
    def __init__(self):
        self.small = [] # smaller eleemnts than middle
        self.large = [] # larger elements than middle


    def addNum(self, num:int)-> None:
        """adds the integer num from the data stream to the data structure."""
        # check if input num is largeer than min of largeHeap
        # if yes then add it to large , if not then add to smallerHeap
        if self.large and num>self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1*num)

        # check if len of small is 1 more than large
        # if not then pop from small and push to large
        if len(self.small) - len(self.large) >1:
            # pop from small
            val = -1 * heapq.heappop(self.small)
            # push to large
            heapq.heappush(self.large, val)


        # check if len of large is 1 more than small
        # if not then pop from large and push to small
        if len(self.large) - len(self.small) >1:
            # pop from large
            val = heapq.heappop(self.large)
            # push to small
            heapq.heappush(self.small, -1*val)
    
# 1, 2, 3, 4
# 2 small -2,-1
# 2 large  3, 4
       
    def findMedian(self)->float:
        """ returns the median of all elements so far"""
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1*self.small[0] + self.large[0])/2
        
