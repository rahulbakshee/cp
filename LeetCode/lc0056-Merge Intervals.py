# https://leetcode.com/problems/merge-intervals/description/

# time:O(nlogn), space:O(1)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the input
        intervals.sort(key= lambda i:i[0])

        # initialize the result output
        result = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]: # overlap
                result[-1][1] = max(result[-1][1], interval[1])
            else: #no overlap
                result.append(interval)
        return result
