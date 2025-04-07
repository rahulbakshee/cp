class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0

        def find_min(nums):
            minn = float("inf")
            index = len(nums)+1
            
            for i in range(1, len(nums)):
                if minn > nums[i]+nums[i-1]:
                    minn = nums[i]+nums[i-1]
                    index = i-1

            if index+2 < len(nums):
                return nums[:index] + [nums[index]+nums[index+1]] + nums[index+2:]
            else:
                return nums[:index] + [nums[index]+nums[index+1]]
 
        result = 0
        while len(nums) > 0 and nums != sorted(nums):
            nums = find_min(nums)
            result += 1

        return result
    
            
