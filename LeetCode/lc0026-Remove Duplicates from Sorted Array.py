# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# in-place sorting
# time:O(n logn), space:O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(sorted(set(nums)))
        return len(nums)

# two pointers
# time:O(n), space:O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        left, right = 0, 1
        while left < right and right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left +=1
                nums[left] = nums[right]
                right += 1

        return left+1
