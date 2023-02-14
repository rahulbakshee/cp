# https://leetcode.com/problems/two-sum/

# bruteforce
# space O(1) time O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                   return [i, j]
        
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
# hashmap/dict
# space O(n) time O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            dif = target - num

            if dif in hashmap:
                return [hashmap[dif], index]
            hashmap[num] = index
