# linear - time:O(n), space:O(1)
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        gap = 0

        for i in range(1, len(nums)):
            gap = nums[i] - nums[i-1] -1

            if gap >= k:
                return nums[i-1] + k

            k -= gap

        return nums[-1] + k 


# binary search time:O(logn), space:O(1)
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = right - (right-left)//2

            if nums[mid] - nums[0] - mid < k:
                left = mid
            else:
                right = mid-1

        return nums[0] + k + left
