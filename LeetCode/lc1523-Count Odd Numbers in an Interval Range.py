# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        nums = high - low + 1

        if low%2 !=0 and high%2 != 0:
            return nums//2 + 1
        else:
            return nums//2 