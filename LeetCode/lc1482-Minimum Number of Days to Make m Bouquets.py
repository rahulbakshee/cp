# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

# time:O(n log max(bloomDay)), space:O(1)
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k :
            return -1

        def feasible(day:int)->bool:
            flowers = 0
            bouquet = 0
            for bloom in bloomDay:
                if bloom > day: # flower has not bloomed yet
                    flowers = 0 # this breaks the ajdacency
                else: # flower has bloomed
                    bouquet += (flowers + 1) // k
                    flowers  = (flowers + 1) % k
            return bouquet >=m

        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
