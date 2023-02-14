# https://leetcode.com/problems/running-sum-of-1d-array/

# space: O(1), time:O(n)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        s = 0
        for num in nums:
            s += num
            result.append(s)
        return result