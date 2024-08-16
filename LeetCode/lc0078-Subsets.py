# recusrion - backtracking 
# For Time it is O(n * 2^n) because there will be 2^n different subsets, and we have to create a copy of each one, which is O(n).

# For Space it is O(n) if you don't count the output array, because the size of the function call stack will be O(n).
# Meaning we have to call the recursive function n times in a row, before it returns.


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, sol = [], []

        def backtrack(i):
            if i >= len(nums):
                result.append(sol[:])
                return

            # take it
            sol.append(nums[i])
            backtrack(i+1)
            
            # don't take it
            sol.pop()
            backtrack(i+1)

        backtrack(0)
        return result
