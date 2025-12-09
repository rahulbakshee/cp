
"""
nums   [2,7,9,3,1]
index  [0,1,2,3,4]


            0(2)
        2(11)       3(5)       4(3)
    4(12)                       

"""


# recursion
# time: O(2^n) - breadth ^ depth where n- len of nums
# space:O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i):
            # base 
            if i >= len(nums):
                return 0

            # not rob it
            amount = dfs(i+1)

            # rob it
            amount = max(amount, nums[i] + dfs(i+2))

            return amount
        
        return dfs(0)


# recursion + memoization - top down DP
# time:O(n), spacve:O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i):
            if i in memo:
                return memo[i]
                
            # base 
            if i >= len(nums):
                return 0

            # not rob it
            amount = dfs(i+1)

            # rob it
            amount = max(amount, nums[i] + dfs(i+2))

            memo[i] = amount
            return memo[i]       


        memo = {}
        return dfs(0)
        

# iterative - bottom up  - DP
# time:O(n), space:O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[-1]


# iterative - bottom up  - DP - space optimized
# time:O(n), space:O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            prev, curr = curr, max(nums[i]+prev, curr)

        return curr
