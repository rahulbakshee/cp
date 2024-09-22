# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# # bruteforce -not utilizing sortedness
# # space O(1), time O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i+1, j+1]


# still not utilizing sortedness
# space O(n), time O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
               return [hashmap[diff]+1, index+1]
            hashmap[num] = index


# Your solution must use only constant extra space.
# time to uitlize the sortedness of given array
# two pointer solution
# space O(1), time O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else: # nums[left] + nums[right] == target
                return [left+1, right+1]
            
