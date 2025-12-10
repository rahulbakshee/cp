class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i1, i2):
            if i1 == len(word1) and i2 == len(word2):
                return 0

            if i1 == len(word1):
                return len(word2) - i2

            if i2 == len(word2):
                return len(word1) - i1

            result = float("inf")

            
            if word1[i1] == word2[i2]:
                result = min(result, dfs(i1+1, i2+1))

            else:
                # 1- insert
                result = min(result, 1+dfs(i1, i2+1))

                # 2 - delete
                result = min(result, 1+dfs(i1+1, i2))


                # 3  - replace
                result = min(result, 1+dfs(i1+1, i2+1))

            return result

        return dfs(0,0)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i1, i2):
            if (i1, i2) in memo:
                return memo[(i1, i2)]

            if i1 == len(word1) and i2 == len(word2):
                return 0

            if i1 == len(word1):
                return len(word2) - i2

            if i2 == len(word2):
                return len(word1) - i1

            result = float("inf")

            
            if word1[i1] == word2[i2]:
                result = min(result, dfs(i1+1, i2+1))

            else:
                # 1- insert
                result = min(result, 1+dfs(i1, i2+1))

                # 2 - delete
                result = min(result, 1+dfs(i1+1, i2))


                # 3  - replace
                result = min(result, 1+dfs(i1+1, i2+1))

            memo[(i1, i2)] = result
            return result
        
        memo = {}
        return dfs(0,0)





class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for c in range(n-1, -1, -1):
            dp[m][c] = 1 + dp[m][c+1]

        for r in range(m-1, -1, -1):
            dp[r][n] = 1 + dp[r+1][n]


        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]

                else:                    
                    dp[i][j] = 1 + min (dp[i+1][j], dp[i][j+1], dp[i+1][j+1])


        return dp[0][0]
