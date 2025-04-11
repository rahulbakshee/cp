top down - memoization
# time:O(mn), space:O(mn)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        @cache
        def dp(i,j):
            # base case
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False


            # handle dot 
            match = False
            if i<m and (s[i] == p[j] or p[j] == "."):
                match = True

            # handle star
            if j+1<len(p) and p[j+1] == "*":
                # don't use the star
                use = dp(i, j+2)
                # use the star
                dont_use = match and dp(i+1, j)

                return use or dont_use
            
            # if no star
            # then check for simple match
            if match:
                return dp(i+1, j+1)

            return False

        return dp(0,0) # indexes for s and p






# bottom up - tabulation
# time:O(mn), space:O(mn)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                match = i<m and (s[i] == p[j] or p[j] == ".")

                # *
                if j+1 < n and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or (match and dp[i+1][j])
                else:
                    dp[i][j] = match and dp[i+1][j+1]


        return dp[0][0]




























