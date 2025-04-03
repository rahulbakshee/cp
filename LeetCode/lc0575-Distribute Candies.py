# time:O(nlogn), space:O(n)
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyType.sort()

        can_eat = len(candyType)//2
        available = 1
        for i in range(1, len(candyType)):
            if candyType[i] != candyType[i-1]:
                available += 1
        
        return min(can_eat, available)           


# time:O(n), space:O(n)
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        can_eat = len(candyType)//2
        available_types = len(set(candyType))

        if available_types >= can_eat:
            return can_eat
        else:
            return available_types
