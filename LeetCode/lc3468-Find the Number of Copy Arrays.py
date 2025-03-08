class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        left, right = bounds[0]

        for i in range(1, len(original)):
            diff = original[i] - original[i-1]

            left = max(left+diff, bounds[i][0])
            right = min(right+diff, bounds[i][1])

            if left > right:
                return 0

        return right-left+1         
