class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        
        for i in range(len(s)-k+1):
            if (i-1<0 or s[i] != s[i-1]): # left bound
                if (len(Counter(s[i:i+k])) == 1): # same char for k length
                    if (i+k >=len(s) or s[i+k-1] != s[i+k]): # right bound
                        return True

        return False
