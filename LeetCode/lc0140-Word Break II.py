# backtracking - recursion
# time:O(n.2^n), space:O(n.2^n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def dp(i, sol):
            # 
            if i >= len(s):
                result.append(" ".join(sol))
                return


            for word in wordDict:
                w = len(word)

                if i+w <= len(s) and s[i:i+w] == word:
                    sol.append(word)
                    dp(i+w, sol)
                    sol.pop()



        result = []
        dp(0,[])
        return result


# memoization
# time:O(n.2^n), space:O(n.2^n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        @cache
        def dp(i, sol):
            # 
            if i >= len(s):
                result.append(" ".join(sol))
                return


            for word in wordDict:
                w = len(word)

                if i+w <= len(s) and s[i:i+w] == word:
                    
                    dp(i+w, sol+(word,))
                    
        
        result = []
        dp(0,())
        return result

# exponential - I DID IT MYSELF
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dp(i, sol):
            if i >= len(s):
                result.append(" ".join(sol))
                return


            for word in wordDict:
                w = len(word)
                if i+w<=len(s) and s[i:i+w] == word:
                    dp(i+w, sol + [word])
                    
            
        result = []
        dp(0, [])
        return result     


