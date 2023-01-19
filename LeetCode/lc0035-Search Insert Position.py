# https://leetcode.com/problems/search-insert-position/

# bruteforce
# space O(1), time O(n)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
            else:
                continue
        return len(nums)


# binary search, assuming no duplicates in nums
# space O(1), time O(logn)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] == target: # if duplicates in nums, remove this condition
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return left 

# binary search, assuming duplicates in nums
# space O(1), time O(logn)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left 
