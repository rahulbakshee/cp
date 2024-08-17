# very slow(1004ms, beats 5%) - but runs
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        sol = []

        def dfs():
            # base case
            if len(sol) == k:
                result.append(sol.copy())
                return

            for num in range(1, n+1):
                if not sol or (sol and num > sol[-1]):
                    sol.append(num)
                    dfs()
                    sol.pop()
                    
        dfs()
        return result

# efficient solution - DFS- recusrion - time:O(n choose k), space:O(n)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        sol = []

        def dfs(start):
            # base case
            if len(sol) == k:
                result.append(sol.copy())
                return

            for num in range(start, n+1):
                sol.append(num)
                dfs(num+1)
                sol.pop()

        dfs(1)
        return result
        
