# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/


# time-O(n), space O(1)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        for i in nums:
            if i < k:
                counter += 1

        return counter


