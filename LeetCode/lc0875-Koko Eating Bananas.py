# https://leetcode.com/problems/koko-eating-bananas


# # bruteforce, linear, time limit exceeded
# # space O(1), time O(pn) -> p is number of piles and n is max(piles)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for k in range(min(piles), max(piles)+1):
            #print("k", k)

            curr_h = 0
            for pile in piles:
                #print("pile", pile, "curr_h", curr_h)
                rem_ba = pile

                while rem_ba >= 1:
                    #print("rem_ba", rem_ba)
                    if rem_ba <= k:
                        rem_ba = 0
                        curr_h += 1
                        break
                    if rem_ba > k:
                        rem_ba -= k
                        curr_h += 1

            #print("curr_h", curr_h)
            if curr_h <= h:
                return k




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
