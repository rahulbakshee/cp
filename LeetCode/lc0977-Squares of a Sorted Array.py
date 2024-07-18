# https://leetcode.com/problems/squares-of-a-sorted-array/description/

# square and sort
# time:O(n) + O(nlogn) - > O(nlogn)
# space:O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])


# two pointers
# time:O(n), space:O(1)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        
        left, right = 0, len(nums)-1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[right-left] = nums[left] **2
                left += 1
            else:
                result[right-left] = nums[right]**2
                right -= 1
        return result
                
