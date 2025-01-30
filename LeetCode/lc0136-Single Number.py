# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_set_nums = sum(set(nums)) *2
        
        return (sum_set_nums - sum_nums)


# bit manipukation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res

        return res
