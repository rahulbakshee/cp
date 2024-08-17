# time: roughly O(n**t)
# space:O(n) - callstack
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sol = []

        def dfs(i, curr_sum):
            # base case
            # reached target - add to final result
            if curr_sum == target:
                result.append(sol.copy())
                return
            
            # exceeded target - return
            if curr_sum > target or i >= len(candidates):
                return

            # use this element
            sol.append(candidates[i])
            dfs(i, curr_sum+candidates[i])

            # don't include this elements
            sol.pop()
            dfs(i+1, curr_sum)


        dfs(i=0, curr_sum=0)
        return result
