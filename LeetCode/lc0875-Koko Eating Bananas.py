# https://leetcode.com/problems/koko-eating-bananas


# # bruteforce, linear, time limit exceeded
# time:O(p*m) - where p is the number of piles and m is the max length of piles
# space:O(1)
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for cap in range(1, max(piles)+1):
            sum_h = 0

            for pile in piles:
                sum_h += int(math.ceil(pile/cap))

            if sum_h == h:
                return cap
        return cap



# binary search
# time:O(p log m) - p is the number of piles, m is the max length of piles
# space:O(1)
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(capacity)-> bool:
            sum_h = 0
            for pile in piles:
                sum_h += math.ceil(pile/capacity)
            if sum_h <= h:
                return True
            else:
                return False

        left , right = 1, max(piles)

        while left < right:
            mid = left + (right-left)//2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left



