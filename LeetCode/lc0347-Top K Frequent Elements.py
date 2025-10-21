# sorting - time:O(nlogn), space:O(n)
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # {num:freq...}

        num_freq = [[value, key] for key, value in counter.items()]

        num_freq.sort()
        
        result = []
        for i in range(len(num_freq)-1, -1, -1):
            _, key  = num_freq[i]
            result.append(key)

            if len(result) == k:
                return result



# minHeap - time:O(nlognk), space:O(k)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # {key : freq}

        minHeap = []
        # iterate over nums to puish into minHeap
        for key, freq in counter.items():
            heapq.heappush(minHeap, [freq, key])

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # iterate over minHeap to prepare result of length k
        result = []
        while minHeap:
            freq, key = heapq.heappop(minHeap)
            result.append(key)

        return result




# buckets sort - time:O(n), space:O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min_occurance = 1
        # max_occuranec = len(nums)

        # create a freq counter of nums
        counter = Counter(nums)
        # create a list of lists, where indexes are freq, value at index is num from nums
        buckets = [[] for i in range(len(nums)+1)]

        for key, value in counter.items():
            buckets[value].append(key)

        # iterate over bucktes to prepare result of len k
        result = []
        for i in range(len(buckets)-1, -1, -1):
            for val in buckets[i]:
                result.append(val)
                if len(result) == k:
                    return result
