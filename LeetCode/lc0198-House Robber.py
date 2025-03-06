
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
        def dp(index):
            # base case
            if index >= len(nums):
                return 0

            return max(nums[index]+dp(index+2), dp(index+1))

        return max(dp(0), dp(1))




# recursion + memoization - top down DP
# time:O(n), spacve:O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(index, memo={}):
            # base case
            if index in memo:
                return memo[index]

            if index >= len(nums):
                return 0

            memo[index] = max(nums[index]+dp(index+2,memo), dp(index+1,memo))
            return memo[index]

        return max(dp(0,{}), dp(1,{}))
        

# iterative - bottom up  - DP
# time:O(n), space:O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[-1]

        # if nums has at least two numbers
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]




# iterative - bottom up  - DP - space optimized
# time:O(n), space:O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[-1]

        # if nums has at least two numbers
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr, prev = max(prev + nums[i], curr), curr

        return curr

