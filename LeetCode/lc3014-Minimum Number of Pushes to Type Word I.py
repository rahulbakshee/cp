# time:O(n), space:O(1)
class Solution:
    def minimumPushes(self, word: str) -> int:
        result = 0
        n = len(word)
        div = n//8
        mod = n%8

        times = 1
        while times < div+1:
            result += (times) * 8
            times += 1
        
        result += mod*times

        return result
