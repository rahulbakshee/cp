"""as the input is already sorted and non-overlapping. three cases-
1-newInterval ends before the curr interval starts
 - append newInterval to result.return the result + rest of the intervals[i:]
2-newInterval starts after the curr interval ends
 - append newIntervals to the result. donot return yet
3-newInterval has overlap with curr interval
 - update the newInterval by taking the min of start and max of end

REMEMBER to append newIterval to the result outside the loop
return result"""

# we modify newInterval
# linear time:O(n), space:O(1)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # case1-new interval comes befor the curr interval
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            # case 2-new interval comes after the curr interval
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # case 3-overlap. newInterval has overlap with curr interval
            else:
                # update the upcoming interval by merging it with curr interval
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        result.append(newInterval) # REMEMBER
        return result
