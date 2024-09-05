# time:O(max(m, n)), space:O(1)
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_n = mean * (len(rolls) + n) - sum(rolls)

        # sum could never be less than n or greater than 6n
        if sum_n < 1*n  or sum_n > 6*n:
            return []

        # distribute the sum_n into n buckets
        mod = sum_n % n
        elements = [sum_n // n] * n
        for i in range(mod):
            elements[i] += 1

        return elements



        
