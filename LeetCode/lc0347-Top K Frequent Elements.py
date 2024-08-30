# good solutions at  - https://leetcode.com/problems/top-k-frequent-elements/solutions/1502514/c-python-2-solutions-maxheap-bucket-sort-clean-concise/


# using heap - 
# time:O(n) freq + O(n) heapify best OR O(nlogn) heapify worst case + O(klogn) heappop
# space:O(n) freq, + O(n) heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # freq: key:num, val:occurances {1:3, 2:5, 7:1}

        # maxHeap for storing the (occurances, num)

        maxHeap = [(-1*occur, key) for key, occur in freq.items()]
        heapify(maxHeap)


        result = []
        for _ in range(k):
            occur, key = heappop(maxHeap)
            result.append(key)

        return result




# bucket sort - 
# time-O(n), space-O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1

        freq = [[] for i in range(len(nums)+1)]
        for n, c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq)-1, 0, -1):
            result.extend(freq[i])
            if len(result) >=k:
                return result[:k]
