# https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/description/

# time:O(n), space:O(n)
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n==k:
            return 0
        if n &k != k:
            return -1
        
        result = 0
        return sum(map(int, bin(n)[2:])) - sum(map(int, bin(k)[2:]))
