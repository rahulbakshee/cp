# time:O(2**n), space:O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        sol = []

        def backtrack(openn, close):
            if openn == close == n:
                result.append("".join(sol))
                return 
            
            if openn < n:
                sol.append("(")
                backtrack(openn+1, close)
                sol.pop()

            if openn > close:
                sol.append(")")
                backtrack(openn, close+1)
                sol.pop()

        
        backtrack(0,0)
        return result
