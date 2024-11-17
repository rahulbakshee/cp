# time:O(s*p), space:O(1)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = [0] * len(spells)

        for i in range(len(spells)):
            for potion in potions:
                if spells[i] * potion >= success:
                    result[i] += 1

        return result




# sorting and binary search
# time:O(mlogm + nlogm) - n is len of spells, m is len potions
# space:O(1)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        result = [0] * len(spells)

        for i in range(len(spells)):
            left, right = 0, len(potions)-1
            index = len(potions)

            while left <= right:
                mid = (left + right)//2
                if spells[i] * potions[mid] >= success:
                    index = mid
                    right = mid-1
                else:
                    left = mid+1
                
            result[i] = len(potions)-index

        return result