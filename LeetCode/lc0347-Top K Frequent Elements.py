# time:O(nlogK)
# space:O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create num:freq mapping
        counter = Counter(nums)

        # craete minHeap
        minHeap = []
        for key, val in counter.items():
            heapq.heappush(minHeap, (val, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        result = []
        for val, key in minHeap:
            result.append(key)

        return result

        

# bucket sort - 
# time-O(n), space-O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        freq = [[] for i in range(len(nums)+1)]
        for n, c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq)-1, 0, -1):
            result.extend(freq[i])
            if len(result) >=k:
                return result[:k]
