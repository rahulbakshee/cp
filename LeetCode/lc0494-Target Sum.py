# recursion
# time:O(2^n), space:O(n)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(index:int, curr_sum:int)->int:
            # base case
            if index == len(nums):
                return 1 if curr_sum == target else 0
                
            return backtrack(index+1, curr_sum+nums[index]) + backtrack(index+1, curr_sum-nums[index])
            
        
        
        return backtrack(0,0) #(index, curr_sum)

  
        
# recursion with memoization
# time:O(n.totalSum), space:(n.totalSum)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (index, curr_sum):count

        def backtrack(index, curr_sum):
            # base case - check already in memo
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            # base case - check index reached the end of nums
            if index == len(nums):
                return 1 if curr_sum == target else 0

            memo[(index, curr_sum)] = backtrack(index+1, curr_sum+nums[index]) + backtrack(index+1, curr_sum-nums[index])
            return memo[(index, curr_sum)]
        
        
        if not nums:
            return 0

        return backtrack(0,0)   


        
# top down DP
# time:O(n.totalSum), space:(n.totalSum)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums)+1)]

        dp[0][0] = 1 # dp[0 elements][0 sum] = 1 ways
        # 1 ways to have sum as 0 with first 0 elements

        for i in range(len(nums)):
            for curr_sum, count in dp[i].items():
                dp[i+1][curr_sum+nums[i]] += count
                dp[i+1][curr_sum-nums[i]] += count


        return dp[len(nums)][target]
                

        
# space optimized DP
# time:O(n.totalSum), space:(totalSum)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1 # dp[0 sum] = 1 ways
        # 1 ways to have sum as 0 with first 0 elements

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for curr_sum, count in dp.items():
                next_dp[curr_sum+nums[i]] += count
                next_dp[curr_sum-nums[i]] += count

            dp = next_dp


        return dp[target]
    
