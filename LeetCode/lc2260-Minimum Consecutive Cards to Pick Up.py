# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/

# time:O(n), space:O(1)
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        distance = 0
        min_distance = 100001 # somehow float('inf') did not work on leetcode for me

        for i in range(len(cards)):
            if cards[i] in seen:
                distance = i - seen[cards[i]]
                min_distance = min(min_distance, distance)
                
            seen[cards[i]] = i 
            # print("seen", seen, "distance", distance, "min_distance", min_distance)
        if min_distance == 100001:
            return -1
        else:
            return min_distance+1
