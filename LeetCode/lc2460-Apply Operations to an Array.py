# time:O(n), space:O(1)
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] *2
                nums[i+1] = 0

        # shift zeros to the end
        index = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        return nums



# solved myself in March 2025 monthly challange
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] = nums[left]*2
                nums[right] = 0
                left += 2
                right += 2
            else:
                left += 1
                right += 1


        result = [0] * len(nums)
        i = 0
        for num in nums:
            if num != 0:
                result[i] = num
                i += 1

        return result
