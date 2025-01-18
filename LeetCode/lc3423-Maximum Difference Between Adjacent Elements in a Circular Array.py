# time:O(n), space:O(1)
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_difference = abs(nums[1]-nums[0])
        for i in range(2, len(nums)):
            diff = abs(nums[i]-nums[i-1])
            max_difference = max(max_difference, diff)

        return max(max_difference, abs(nums[-1]-nums[0]))
