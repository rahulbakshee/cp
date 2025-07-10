# using hashmap and minHeap
# time:O(nlogn), space:O(n)
""" - Count the frequency of each card using collections.Counter.
 - Use a min-heap to always pick the smallest available card to start 
 forming a group.
 - For each group of groupSize starting from the smallest card, reduce the count 
 for each consecutive number. If any required card is missing → return False.
"""

class Solution:
    def isPossibleDivide(self, hand: List[int], groupSize: int) -> bool:
        # check if group can be divided into groupsize
        if len(hand) % groupSize != 0:
            return False

        # init a counter dict for counting freq of nums
        counter = {}
        for num in hand:
            counter[num] = 1+counter.get(num, 0)

        # init a minHeap to store counter keys in increasing fashion
        minHeap = list(counter.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first+groupSize):
                # check if this key is there in counter
                if i not in counter:
                    return False
                
                # decrement the counter
                counter[i] -= 1
                # remove from minHeap if counter[key] reaches 0
                if counter[i] == 0:
                    heapq.heappop(minHeap)
        return True
