# https://leetcode.com/problems/isomorphic-strings

# space:O(1),  time: O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2t, t2s = {},{}

        for i in range(len(s)):
            if s[i] in s2t:
                if s2t[s[i]] != t[i]:
                    return False
            if t[i] in t2s:
                if t2s[t[i]] != s[i]:
                    return False
            
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]

        return True