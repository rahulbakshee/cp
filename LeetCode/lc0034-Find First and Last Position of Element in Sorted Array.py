class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # we can do binary search two time each for finding first and last position
        def first_bin_search(nums, target):
            i = -1
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    i = mid
                    right = mid-1
            return i

        def last_bin_search(nums, target):
            i = -1
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    i = mid
                    left = mid+1
            return i


        left = first_bin_search(nums, target)
        right = last_bin_search(nums, target)

        if left <= right:
            return [left,right]
        else:
            return [-1,-1]
