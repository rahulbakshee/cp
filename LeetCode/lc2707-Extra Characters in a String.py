# code is very similar to LIS-longest increasing subsequence
# recursion - time:O(n*2^n + mk), space:O(n+ mk)
# n-len of s, m-words in dictionary, k-avg len of word in dict
# DP - memoization - time:O(n^3 + mk), space:O(n+mk)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(s):
                memo[i] = 0
                return 0

            result = 1 + dfs(i+1) # skip curr char

            for j in range(i, len(s)):            # O(n)
                if s[i:j+1] in dictionary_set:    # O(n)
                    result = min(result, dfs(j+1))

            memo[i] = result
            return result

        dictionary_set = set(dictionary)

        memo = {}
        return dfs(0)                             # O(n)

# bottom up - tabulation
# time:O(n^3), space:O(n+mk)
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



# using Trie - time:O(n^2+mk), space:O(n+mk)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word:str):
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]

        curr.endOfWord = True

    def search(self, word:str):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        return curr.endOfWord

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        
        # defin DFS using Trie nodes for searching the prefixes from s
        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(s):
                memo[i] = 0
                return 0

            result = 1 + dfs(i+1)   # skip curr char

            # use trie
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]

                # check for end of word after loop ends
                if curr.endOfWord:
                    result = min(result, dfs(j+1))
                
            memo[i] = result
            return result
        
        memo = {}
        return dfs(0)
