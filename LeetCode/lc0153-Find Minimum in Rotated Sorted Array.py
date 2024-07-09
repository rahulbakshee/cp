# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# sorting entire array
# time:O(nlogn), space:O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return sorted(nums)[0]        




# linear traversal
# time:O(n), space:O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = float("inf")
        for num in nums:
            min_value = min(min_value, num)
        return min_value




# time:O(logn), space:O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid
        return nums[left]
