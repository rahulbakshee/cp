# time:O(nlogn), space:O(sorting/n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the input intervals based on start time
        intervals.sort()

        merged = []
        for i in range(len(intervals)):
            # if the list of merged intervals is empty or if curr 
            # interval does not overlap with the previous, simply append it
            if not merged or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                # merge the overlapping intervals
                merged[-1][1] = max(merged[-1][1], intervals[i][1])

        return merged
