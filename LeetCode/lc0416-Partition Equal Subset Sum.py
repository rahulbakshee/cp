class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dp(i, left, right):
            if left > half or right > half:
                return False
            if i >= len(nums):
                return left == right == half
            
            return dp(i+1, left+nums[i], right) or dp(i+1, left, right+nums[i])
        
        half = sum(nums)//2
        return dp(0,0,0)
