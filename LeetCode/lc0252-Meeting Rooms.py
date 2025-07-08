
# simple bruteforce
# time:O(n^2), space:O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        for i in range(n):
            A = intervals[i]
            for j in range(i + 1, n):
                B = intervals[j]
                if min(A.end, B.end) > max(A.start, B.start):
                    return False
        return True


# complex bruteforce
# time:O(n^2), space:O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if (
                    (intervals[i][0] <= intervals[j][0] and intervals[i][1] > intervals[j][0]) or
                    (intervals[j][0] <= intervals[i][0] and intervals[j][1] > intervals[i][0])
                   ):
                    return False

        return True


# sorting
# time:O(nlogn), space:O(sorting/n)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort the input intervals
        intervals.sort()

        # loop over intervals and check if overlapping
        if len(intervals) < 2:
            return True

        for i in range(len(intervals)-1):
            first = intervals[i]
            second = intervals[i+1]

            # check if second is starting before first ends
            if second[0] < first[1]:
                return False

        return True
