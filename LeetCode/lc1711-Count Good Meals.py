# time:O(22*n), space:O(n)
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        freq = defaultdict(int)
        result = 0

        for deli in deliciousness:
            for i in range(22):
                result += freq[2**i - deli]
            freq[deli] += 1

        return result % MOD
