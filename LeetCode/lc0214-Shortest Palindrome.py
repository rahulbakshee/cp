# time:O(n**2), space:O(n) 
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse_s = s[::-1]

        for i in range(len(s)):
            if s.startswith(reverse_s[i:]):
                return reverse_s[:i]+s

        return s



GO OVER THE DITORIAL TO SEE OTHER IMPLEMENTATIONS
