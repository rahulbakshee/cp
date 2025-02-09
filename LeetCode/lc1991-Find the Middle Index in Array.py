# https://leetcode.com/problems/find-the-middle-index-in-array

# time:O(n^2), space: O(1)
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1


# time:O(n), space:O(1)
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1
