# solving it similar to
# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75
# time:O(n), space:O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        k = 1
        for right in range(len(nums)):
            k = k - 1 + nums[right]
            if k < 0:
                k = k + 1 - nums[left]
                left += 1

        return right-left+1


