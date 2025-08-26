# https://leetcode.com/problems/4sum/description/

# taken from neetcode - need to revisit 
# time:O(n**3), space:O(n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(k, start, target):
            # base case
            if k == 2:
                left, right = start, len(nums)-1

                while left < right:
                    if nums[left] + nums[right] > target:
                        right -=1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        result.append(sol + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left -1]:
                            left += 1
                return

            # normal
            for i in range(start, len(nums)-k+1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                sol.append(nums[i])
                kSum(k-1, i+1, target-nums[i])
                sol.pop()

            
        nums.sort()
        result, sol = [], []
        kSum(4, 0, target)
        return result
