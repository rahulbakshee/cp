# time:O(n**2), space:O(1)
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0

        for sep in range(len(s)-1):
            score = 0
        
            # left
            for l in range(sep+1):
                if s[l] == "0":
                    score += 1

            # right
            for r in range(sep+1, len(s)):
                if s[r] == "1":
                    score += 1
            
            max_score = max(max_score, score)

        return max_score



# time:O(n), space:O(1)
class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        max_score = 0
        # count the ones only. We don't count zeros because we need to count zeros for the left part
        for chr in s:
            if chr == "1":
                ones += 1
        
        # iterate ove the s, and move each chr into the left part
        for i in range(len(s)-1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            max_score = max(max_score, ones+zeros)
        return max_score

