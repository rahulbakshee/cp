# recursion - exponential - TLE
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(curr, prev):
            if curr >= len(nums):
                return 0

            # not take
            result = dfs(curr+1, prev)

            # take
            if prev == -1 or nums[curr] > nums[prev]:
                result = max(result, 1+dfs(curr+1, curr))

            return result
        
        return dfs(0,-1) # curr_index, prev_index



# DP - top down
# time:O(n^2), space:O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = [-1 for _ in range(n)]

        def dfs(i):
            if memo[i] != -1:
                return memo[i]


            LIS = 1

            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1+dfs(j))

            memo[i] = LIS
            return memo[i]

        return max(dfs(i) for i in range(n))



# DP - bottom up - tabulation
# time:O(n^2), space:O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])

        return max(dp)



# DP + binary search
# time:O(nlogn), space:O(n)
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]: 
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i] 

        return LIS
