https://leetcode.com/problems/meeting-rooms/
# https://www.lintcode.com/problem/920/


from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            before = intervals[i-1]
            after = intervals[i]

            if before > after.start:
                return False
        return True

# time:O(nlogn), space:O(1)
