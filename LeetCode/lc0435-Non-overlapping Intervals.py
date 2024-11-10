# time:O(nlogn), space:O(n)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the input
        intervals.sort()
        
        result = 0
        prevStart, prevEnd = intervals[0]
        
        for start, end in intervals[1:]:
            # overlapping
            if start < prevEnd:
                result += 1
                prevEnd = min(prevEnd, end)
            # non overlapping
            else:
                prevEnd = end
                

        return result
