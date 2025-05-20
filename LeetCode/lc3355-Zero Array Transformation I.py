# time:O(n+q)
# space:O(n)
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        delta = [0] * (len(nums)+1)

        for l,r in queries:
            delta[l] += 1
            delta[r+1] -= 1

        # prefix sum
        prefix = [0] * len(delta)
        prefix[0] = delta[0]
        for i in range(1, len(nums)):
            prefix[i] = delta[i] + prefix[i-1]
        
        print(delta)
        print(prefix)

        # check if any number from prefix is smaller than any num from nums
        for i, num in enumerate(nums):
            if num > prefix[i]:
                return False

        return True
