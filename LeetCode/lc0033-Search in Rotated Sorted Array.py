# brute force  - linear scan 
# time:O(N), space:O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i

        return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1

                else:
                    right = mid - 1

            else: # [6,7,0,1,2,3,4,5]
            #        l      m      r
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        
        return -1
