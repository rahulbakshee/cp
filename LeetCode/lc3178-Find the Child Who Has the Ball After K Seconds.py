# time:O(1), space:O(1)
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        round = 0
        reminder = 0

        round = k//(n-1)
        reminder = k % (n-1)

        if round %2==0:
            return reminder
        else:
            return n-1-reminder
