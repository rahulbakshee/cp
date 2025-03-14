# recursion
# time:O(2^(n+m)), space:O(n+m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dp(i,j):
            # base case
            if i >= n or j >= m:
                return 0 

            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            else:
                return max(dp(i, j+1), dp(i+1, j))            


        n = len(text1)
        m = len(text2)
        return dp(0,0)




# recursion + memoization
# time:O(mn), space:O(mn)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dp(i,j,memo):
            # base case
            if i >= n or j >= m:
                return 0 

            if (i,j) in memo:
                return memo[(i,j)]

            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dp(i+1, j+1,memo)
                return memo[(i,j)]
            else:
                memo[(i,j)] = max(dp(i, j+1,memo), dp(i+1, j,memo))            
                return memo[(i,j)]


        n = len(text1)
        m = len(text2)
        return dp(0,0,{})




# iterative - bottom up - tabulation
# time:O(mn), space:O(mn)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)
        
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], 
                                       dp[row][col+1])

        return dp[0][0]

        


# DID NOT UNDERSTAND FULLY - REVISIT
# iterative - bottom up - space optimized
# time:O(mn), space:O(min(m, n))
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # keep the shorter len text as text1
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        prev = [0] * (len(text1)+1)
        
        
        for col in range(len(text2)-1, -1, -1):
            
            curr = [0] * (len(text1)+1)

            for row in range(len(text1)-1, -1, -1):

                if text1[row] == text2[col]:
                    curr[row] = 1 + prev[row+1]
                else:
                    curr[row]= max(prev[row], curr[row+1])

            prev = curr

        return prev[0]

   
