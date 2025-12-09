# recursion

class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_linear(houses):
            def dfs(i):
                if i >= len(nums):
                    return 0

                # max(not rob, rob)
                return max(dfs(i+1), nums[i] + dfs(i+2))

            if len(houses) == 1:
                return houses[0]

            if len(houses) == 2:
                return max(houses)
            return dfs(0)

        if len(nums) == 1:
            return nums[0]
    
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))



# recursion + memoization
class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_linear(houses):
            def dfs(i):
                if i in memo:
                    return memo[i]

                if i >= len(houses):
                    return 0

                # max(not rob, rob)
                memo[i] = max(dfs(i+1), houses[i] + dfs(i+2))
                return memo[i]

            if len(houses) == 1:
                return houses[0]

            if len(houses) == 2:
                return max(houses)

            memo = {}
            return dfs(0)

        if len(nums) == 1:
            return nums[0]
    
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))



class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_linear(houses):
            prev, curr = 0,0
            for h in houses:
                prev, curr = curr, max(curr, prev+h)

            return curr
            
        if len(nums) == 1:
            return nums[0]

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
