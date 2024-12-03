# time:O(n), space:O(1)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        
        for i in range(len(candies)):
            result.append((max(max(candies), candies[i] + extraCandies) == candies[i] + extraCandies))

        return result
