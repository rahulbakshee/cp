# sliding window
# time:O(n), space:O(n)
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        intervals_len = len(startTime)
        gaps = [0] * (intervals_len+1)


        # calculate the first and last gap
        gaps[0] = startTime[0]
        gaps[-1] = eventTime - endTime[-1]

        # gap between meetings
        for i in range(1, intervals_len):
            gaps[i] = startTime[i] - endTime[i-1]

        # sliding window of size k+1
        curr_free_time = sum(gaps[:k+1])
        max_free_time = curr_free_time
        for i in range(k+1, intervals_len+1):
            curr_free_time += gaps[i] - gaps[i-(k+1)]
            max_free_time = max(max_free_time, curr_free_time)

        return max_free_time
