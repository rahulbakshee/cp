# time:O(n^2), space:O(n^2)
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        result = 0
        freq = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod = nums[i] * nums[j]
                result += 8*freq[prod]
                freq[prod] += 1
        return result
