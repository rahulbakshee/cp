# top down DP - memoization
# time:O(n^2d), space:O(nd)
#  - len of job difficulty , d - days
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        @cache
        def dp(index,days, curr_max):
            # base cases
            if index == len(jobDifficulty) and days == 0:
                return 0
            
            if index == len(jobDifficulty) or days == 0:
                return float("inf")
            
            
            curr_max = max(curr_max, jobDifficulty[index])
            
            ending_the_day_here = curr_max + dp(index+1, days-1, -1)
            
            keep_appending_to_same_day = dp(index+1, days, curr_max)
            
            return min(ending_the_day_here, keep_appending_to_same_day)
        
        return dp(0, d, -1)
