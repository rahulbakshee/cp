class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float("-inf")] + nums + [float("-inf")]

        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i-1

        

# time:O(logn), space:O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            # left neighbor greater
            if mid>0 and nums[mid] < nums[mid-1]:
                right = mid-1 
            # right neighbor greater
            elif mid<len(nums)-1 and nums[mid] < nums[mid+1]:
                left = mid+1
            # mid is peak
            else:
                return mid

