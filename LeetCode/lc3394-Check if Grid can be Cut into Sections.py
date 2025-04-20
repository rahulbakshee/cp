# better way - neetcode as well

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        # 1 - separate x and y direction intervals
        # and sort them
        x = [[rect[0],rect[2]] for rect in rectangles]
        y = [[rect[1],rect[3]] for rect in rectangles]

        x.sort()
        y.sort()

        #2 - create a function to count non overlapping intervals
        def count_non_overlapping(intervals):
            count = 0
            prev_end = -1

            for start, end in intervals:
                if prev_end <= start:
                    count += 1
                prev_end = max(prev_end, end)

            return count

        # 3 - use this function on bothg directions
        return max(count_non_overlapping(x), count_non_overlapping(y)) >= 3

        




# IGNORE THIS ONE  -= THIS IS FROM EDITORIAL
# USE THE ABOVE ONE 

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



