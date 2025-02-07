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
