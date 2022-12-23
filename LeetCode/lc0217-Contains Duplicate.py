# https://leetcode.com/problems/contains-duplicate/

# bruteforce
# space O(1),  time O(n^2)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# sorting
# space O(1),  time O(nlogn)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False        
        

# most optimal
# space O(n) , time O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        
        for num in nums:
            if num in d:
                return True
            else:
                d.add(num)
        return False
        
