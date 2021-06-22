# https://leetcode.com/problems/single-number-iii/


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
                
        result = []
        for key, value in d.items():
            if value == 1:
                result.append(key)
                
        return result
