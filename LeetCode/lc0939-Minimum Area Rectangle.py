# time:O(n**2), space:O(n)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        min_area = float("inf")

        for point in points:
            x1, y1 = point
            for seen_point in seen:
                x2, y2 = seen_point
                if (x1,y2) in seen and (x2, y1) in seen:
                    area = abs(x2-x1) * abs(y2-y1)
                    min_area = min(min_area, area)

            seen.add((x1,y1)) 

        return min_area if min_area !=float("inf") else 0
