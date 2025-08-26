class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0    
        prd = 1

        for right in range(len(nums)):
            prd *= nums[right]

            while left <= right and prd >= k:
                prd = prd // nums[left]
                left += 1

            result += right - left + 1

        return result
