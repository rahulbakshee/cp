class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        index = 2
        i = 2
        while i < len(nums):
            if nums[index-2] != nums[i]:
                nums[index] = nums[i]
                index += 1
            i += 1
        return index
