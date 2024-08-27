# using additional space
# time:O(n), space:O(n)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        result = []
        count_zeros = 0
        for num in nums:
            if num == 0:
                count_zeros +=1
            else:
                result.append(num)

        for _ in range(count_zeros):
            result.append(0)

        nums[:] = result       
                

# two pointers
# time:O(n), space:O(1) 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        # left-zero
        # right-non zero
        while right < len(nums):
            if  nums[left] == 0 and nums[right] != 0:
                # swap
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] != 0:
                left += 1
            right += 1

        print(left, right)
"""

0,1,0,3,12
L
R

"""
