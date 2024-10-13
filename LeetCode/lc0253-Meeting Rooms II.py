# https://leetcode.com/problems/meeting-rooms-ii/description/
# https://www.lintcode.com/problem/919/description

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
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        counter, max_counter = 0, 0
        s, e = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                counter += 1
                s += 1
            else:
                counter -= 1
                e += 1
            max_counter = max(max_counter , counter)

        return max_counter

# time:O(nlogn), space:O(n)
