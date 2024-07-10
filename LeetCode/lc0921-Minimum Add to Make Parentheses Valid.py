# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

# time:O(n), space:O(1)
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        result, bal = 0, 0
        for bracket in s:
            if bracket == "(":
                bal += 1
            else:
                bal -= 1
                if bal < 0:
                    result += 1
                    bal = 0
                
            

        return result + abs(bal)
      
