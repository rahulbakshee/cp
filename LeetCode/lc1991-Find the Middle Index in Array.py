# https://leetcode.com/problems/find-the-middle-index-in-array

# space: O(1), time: O(n)
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
