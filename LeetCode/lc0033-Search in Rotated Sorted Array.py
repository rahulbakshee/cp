# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# linear
# time:O(n), space:O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


# binary search
# time:O(logn), space:O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right= 0, len(nums)-1

        while left <= right:
            mid= left + (right-left)//2

            if nums[mid] == target:
                return mid
            # check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid 
                else:
                    left = mid + 1
            else: # second half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return -1
