# ✅ Quickly mention that brute-force/DP is possible, but greedy gives optimal O(n).

# ✅ Code greedy clearly.

# recursive backtracking - time:O(2^n), space:O(n)
# Use DFS to simulate all possible jump paths from the current index.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i >= len(nums)-1:
                return True

            # check for 0 steps
            if nums[i] == 0:
                return False

            max_jumps = nums[i]
            for j in range(1, max_jumps+1):
                if dfs(i+j):
                    return True
            return False

        return dfs(0)



# DP memoized top down- time:O(n^2), space:O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i in memo:
                return memo[i]
            # base case
            if i >= len(nums)-1:
                memo[i] = True
                return True
            
            # check for 0 steps
            if nums[i] == 0:
                memo[i] = False
                return False

            max_jumps = nums[i]
            for j in range(1, max_jumps+1):
                if dfs(i+j):
                    memo[i+j] = True
                    return True
            
            memo[i] = False
            return False
        
        memo = {}
        return dfs(0)


# DP bottom up - time:O(n^2), space:O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums)-2, -1, -1):
            max_jumps = nums[i]
            for j in range(1, max_jumps+1):
                if i+j >=len(nums)-1 or dp[i+j]:
                    dp[i] = True
                    break

        return dp[0]


# greedy - time:O(n), space:O(1)
# Idea is to keep moving goal post from right side to left 
# init goal at the last index
# iterate from last to first index backwards
# check if (curr index+jump at curr index) is greater than equal to goal
# if yes, move the goal to curr index
# return True if goal is at 0th index
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return  goal == 0 # see if goal reached 0th index or not


