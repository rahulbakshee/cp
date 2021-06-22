# https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums) 
        sum_set  = sum(set(nums)) * 3
        
        return (sum_set - sum_nums) // 2
