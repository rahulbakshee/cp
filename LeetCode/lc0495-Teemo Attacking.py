# time:O(n), space:O(1)
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        for i in range(1, len(timeSeries)):
            result += min(timeSeries[i]-timeSeries[i-1], duration)
        return result + duration
