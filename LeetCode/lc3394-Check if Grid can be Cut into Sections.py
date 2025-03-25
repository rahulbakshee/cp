class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(rectangles, dim):
            count = 0

            rectangles.sort(key=lambda rect:rect[dim])

            furthest_end = rectangles[0][dim+2]

            for i in range(1, len(rectangles)):
                rect = rectangles[i]

                if furthest_end <= rect[dim]:
                    count += 1
                
                furthest_end = max(furthest_end, rect[dim+2])

            return count >=2

        return check(rectangles, 0) or check(rectangles, 1)
