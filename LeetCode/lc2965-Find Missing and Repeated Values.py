# time:O(n^2), space:O(n^2)
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        total = []
        for row in grid:
            total.extend(row)
        
        total = Counter(total)
        for i in range(1, len(grid)**2+1):
            if i not in total:
                missing = i
            if total[i] == 2:
                repeating = i

        return [repeating, missing]
