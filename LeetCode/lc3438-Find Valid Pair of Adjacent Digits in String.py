# time:O(n), space:O(n)
class Solution:
    def findValidPair(self, s: str) -> str:
        hashmap = Counter(s)
        
        for i in range(1, len(s)):
            if s[i-1]!=s[i] and hashmap[s[i-1]] == int(s[i-1]) and hashmap[s[i]] == int(s[i]):
                return s[i-1] + s[i]
                    
        return ""
