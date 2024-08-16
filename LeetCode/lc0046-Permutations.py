# time:O(n! * n) - n for "if num not in sol"
# space:O(n! * n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        sol = []

        def dfs():
            # base case
            if len(sol) == len(nums):
                result.append(sol.copy())
                return

            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    dfs()
                    sol.pop()

        dfs()
        return result
        
