# https://leetcode.com/problems/is-subsequence

# space: O(1), time: O(t)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        index_s = 0
        for index_t in range(len(t)):
            if t[index_t] == s[index_s]:
                index_s += 1

            if index_s == len(s):
                return True
        if index_s == len(s):
                return True
        else:
            return False
            