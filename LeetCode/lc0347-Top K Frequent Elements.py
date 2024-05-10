# https://leetcode.com/problems/top-k-frequent-elements/description/

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
