# recursion + memoization
# time:O(2^n), space:O(n)
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def dp(index):
            # base case
            if index >= len(s):
                return 0
            
            missed = 1 + dp(index+1)

            for word in dictionary:
                if s[index:].startswith(word):
                    missed = min(missed, dp(index+len(word)))
            return missed
        return dp(0)


# bottom up - tabulation
# time:O(n^3), space:O(n+mk)
# Let N be the total characters in the string.
# Let M be the average length of the strings in dictionary.
# Let K be the length of the dictionary.
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set = set(dictionary)
        dp = [0] * (len(s)+1)
        for start in range(len(s)-1, -1, -1):
            dp[start] = 1 + dp[start+1]

            for end in range(start, len(s)):
                curr = s[start:end+1]
                if curr in dict_set:
                    dp[start] = min(dp[start], dp[end+1])

        return dp[0]
