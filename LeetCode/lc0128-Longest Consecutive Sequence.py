# https://leetcode.com/problems/longest-consecutive-sequence/description/

# time-O(n), space-O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        
        for num in nums:
            if num-1 not in nums:
                # it is the starting point
                length = 0
                while (num+length) in nums:
                    length += 1
                max_len = max(max_len , length)

        return max_len
