# better solution from chatgpt
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, sol, curr_sum):
            # If the combination is of the right length and sums to `n`, add to result
            if len(sol) == k:
                if curr_sum == n:
                    result.append(sol.copy())
                return
            
            # Try numbers from `start` to 9
            for num in range(start, 10):
                if curr_sum + num > n:  # Prune early if sum exceeds `n`
                    break
                sol.append(num)
                backtrack(num + 1, sol, curr_sum + num)
                sol.pop()  # Undo the choice

        result = []
        backtrack(1, [], 0)
        return result




class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(i, sol):
            # base case
            if i>9 or len(sol)>k or sum(sol) > n:
                return 

            # success condition
            # check the length of current solution
            if len(sol) == k and sum(sol) == n:
                result.append(sol.copy())
                return

            for index in range(i+1, 10):
                # take it
                sol.append(index)
                backtrack(index, sol)
                    
                # don't take it
                sol.pop()
                
                

        result = []
        backtrack(0, [])
        return result
