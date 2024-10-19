# time:O(nlogn), space:O(n)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # sort the input
        points.sort(key=lambda x: x[1])

        arrows = 1
        prev_end = points[0][1]

        for point in points[1:]:
            if point[0] > prev_end:
                arrows += 1
                prev_end = point[1]

        return arrows
