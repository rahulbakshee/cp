# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/

# sort and two pointer
# time:O(nlogn), space:O(sorting)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0

        left, right = 0, len(nums)-1
        while left < right:
            curr_sum = nums[left] + nums[right]
            max_sum = max(max_sum , curr_sum)
            left += 1
            right -= 1
        return max_sum
