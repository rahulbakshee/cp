# recursion
# time:O(wordDict^s), space:O(s)
# s-len of string, w-len of wordDict, t-max len of word from wordDict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dp(i):
            # base case
            if i >= len(s):
                return True

            for word in wordDict:
                w = len(word)

                if i+w <= len(s) and s[i:i+w] == word:
                    if dp(i+w):
                        return True

            return False

        return dp(0)




# recursion + memoization - top down DP
# time:O(tsw), space:O(s), s-len of string, w-len of wordDict, t-max len of word from wordDict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dp(i, memo):
            if i in memo:
                return memo[i]

            # base case
            if i >= len(s):
                return True

            for word in wordDict:
                w = len(word)

                if i+w <= len(s) and s[i:i+w] == word:
                    if dp(i+w, memo):
                        memo[i] = True
                        return memo[i]

            memo[i] = False
            return memo[i]

        return dp(0, {})




# bottom up DP - tabulation
# time:O(tsw), space:O(s), s-len of string, w-len of wordDict, t-max len of word from wordDict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                w = len(word)

                if i+w <= len(s) and s[i:i+w] == word:
                    dp[i] = dp[i+w]

                if dp[i]:
                    break

        return dp[0]


