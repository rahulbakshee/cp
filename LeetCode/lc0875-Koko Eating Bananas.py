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
# space O(1), time O(plogn) -> where p is number of piles and n is max(piles)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(capacity) -> bool:
            hour = 0
            for pile in piles:
                if pile %capacity ==0: 
                    hour += (pile // capacity)
                else:
                    hour += (pile // capacity) + 1

            if hour <= h:
                return True
            else:
                return False


        left, right = 1, max(piles)
        while left < right:
            mid = left + (right-left)//2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left
