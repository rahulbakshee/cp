# recursion
# time:O(2^m), space:O(m) - m-len of multipliers
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        def dp(index, curr_score, nums):
            # base case
            if index >= len(multipliers):
                return curr_score

            # take the first
            first = nums[0] * multipliers[index]

            # take the last
            last = nums[-1] * multipliers[index]

            return max(dp(index+1, curr_score+first, nums[1:]), 
                       dp(index+1, curr_score+last, nums[:-1]))
            
        return dp(0, 0, nums)



# recursion + memoization - TOP DOWN
# time:O(m^2), space:O(m^2)
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        def dp(index, curr_score, nums, memo):
            # base case
            if (index, curr_score) in memo:
                return memo[(index, curr_score)]
            
            if index >= len(multipliers):
                return curr_score

            # take the first
            first = nums[0] * multipliers[index]

            # take the last
            last = nums[-1] * multipliers[index]

            memo[(index, curr_score)] = max(dp(index+1, curr_score+first, nums[1:], memo), 
                                            dp(index+1, curr_score+last, nums[:-1], memo))
            return memo[(index, curr_score)]
            
        return dp(0, 0, nums, {})


# iterative - BOTTOM UP
# time:O(m^2), space:O(m^2)
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        # dp[index for m][index for n]
        dp = [[0] * (m+1) for _ in range(m+1)]

        # print(m+1, m+1, dp)

        for mi in range(m-1, -1, -1):
            for ni in range(mi, -1, -1):
                # print(mi, ni, n-1-mi+ni)

                dp[mi][ni] = max(multipliers[mi] * nums[ni]          + dp[mi+1][ni+1], 
                                 multipliers[mi] * nums[n-1-(mi-ni)] + dp[mi+1][ni])
        
        return dp[0][0]




# iterative - BOTTOM UP - space optimized
# time:O(m^2), space:O(m)
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        # dp[index for m][index for n]
        dp = [0] * (m+1)

        for mi in range(m-1, -1, -1):
            for ni in range(mi+1):

                dp[ni] = max(multipliers[mi] * nums[ni]          + dp[ni+1], 
                             multipliers[mi] * nums[n-1-(mi-ni)] + dp[ni])
        
        return dp[0]



