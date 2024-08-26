# time:O(n), space:O(1)
# refer editorial and solution tab 
# https://leetcode.com/problems/next-permutation/solutions/14054/python-solution-with-comments/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # get the first number from right which is decreasing 
        i = j = len(nums)-1
        while i>0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # if that is the first element then given number is the last lexicograhical number
        if i <= 0:
            nums.reverse()
            return 

        # find the last ascending position
        k = i-1
        while nums[j] <= nums[k]:
            j -= 1
        # swap
        nums[k], nums[j] = nums[j], nums[k]

        # reverse the rest of numbers
        left, right = k+1, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -=1
