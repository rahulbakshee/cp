class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_right = -1
        result = []

        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max_right:
                result.append(i)
            max_right = max(max_right, heights[i])

        return result[::-1]
