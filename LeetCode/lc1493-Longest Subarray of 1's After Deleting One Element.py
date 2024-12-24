# similar to https://leetcode.com/problems/max-consecutive-ones-iii/description/
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        k = 1
        for right in range(len(nums)):
            k = k -1 + nums[right]
            if k < 0:
                k = k + 1 - nums[left]
                left += 1

        return right-left
