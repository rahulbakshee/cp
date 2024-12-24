# sliding window
# time:O(n), space:O(1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k = k - 1 + nums[right]
            if k < 0:
                k = k + 1 - nums[left]
                left += 1

        return right-left + 1
