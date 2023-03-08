# https://leetcode.com/problems/missing-number


# space: O(1), time:O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)


# https://leetcode.com/problems/missing-number/solutions/2563887/eight-different-approaches-in-python3/?orderBy=most_votes