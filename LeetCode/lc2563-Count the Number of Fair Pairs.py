# time:O(n^2), space:O(1)
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            for j in range(i+1, n):
                if lower <= nums[i] + nums[j] <= upper:
                    result += 1

        return result





class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def lower_bound(low, high, element):
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] >= element:
                    high = mid-1
                else:
                    low = mid+1

            return low        
        
        
        nums.sort()
        result = 0

        for i in range(len(nums)):
            low = lower_bound(i+1, len(nums)-1, lower-nums[i])

            high = lower_bound(i+1, len(nums)-1, upper-nums[i]+1)

            result += high-low

        return result
