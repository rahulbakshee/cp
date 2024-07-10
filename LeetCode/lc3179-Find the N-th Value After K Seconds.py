# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

# using accumulate in python and looping over the k
# time:O(k)
from itertools import accumulate
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        a = [1] * n
        for _ in range(k):
            a = list(accumulate(a))
        return a[-1] % MOD
