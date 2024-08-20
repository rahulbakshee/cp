# time:O(nlogn) + O(n* 2**n)
# space:O(sorting) + O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates.sort()

        result = []
        sol = []

        def backtrack(i):
            # base case
            if sum(sol) == target:
                result.append(sol.copy())
                return
            if sum(sol) > target or i == len(candidates):
                return


            # take it
            sol.append(candidates[i])
            backtrack(i+1)
            sol.pop()

            # don't take it
            while i+1 <len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1)

        backtrack(0)
        return result
