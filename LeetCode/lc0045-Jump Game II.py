# recursion - time:O(2^n), space:O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        def dfs(i):
            # base case
            if i >= n-1:
                return 0

            min_jump = float("inf")
            max_steps = nums[i]

            for j in range(1, max_steps+1):
                jumps = dfs(i+j)
                min_jump = min(min_jump, 1+jumps)

            return min_jump
        
        return dfs(0)

# top down DP - time:O(n^2), space:O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        def dfs(i):
            if i in memo:
                return memo[i]

            # base case
            if i >= n-1:
                return 0

            min_jump = float("inf")
            max_steps = nums[i]

            for j in range(1, max_steps+1):
                jumps = dfs(i+j)
                min_jump = min(min_jump, 1+jumps)

            memo[i] = min_jump
            return min_jump
        
        memo = {}
        return dfs(0)


# bottom up DP - time:O(n^2), space:O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[-1] = 0


        for i in range(n-2, -1, -1):
            max_steps = nums[i]
            for j in range(1, max_steps+1):
                if i+j < n:
                    dp[i] = min(dp[i], 1+dp[i+j])

        return dp[0]




# greedy - time:O(n), space:O(1)
# 🔁 Greedy BFS-style Approach (Window Expansion):
"""You simulate jumps as levels or windows over the array —
 similar to breadth-first search (BFS).
 - Initialize a jump count and a window [left, right] that represents 
    all positions reachable with the current number of jumps.
 - While the right boundary hasn't reached the last index:
     - Scan all indices in the current window.
     - Track the farthest index you can reach from any position in that window.
 - After scanning the window:
     - Move the window to [right + 1, farthest].
     - Increment the jump count (you’re now on the next “level”).
 - Repeat until the farthest reachable index includes the last element.
 - Return the total number of jumps taken."""

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0          # counts number of jumps
        left, right = 0,0   # current jump window [left, right]

        while right < n-1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i+nums[i])
                
            left = right+1
            right = farthest
            result += 1

        return result
