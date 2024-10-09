# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

# time:O(n), space:O(1)
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0
        result = 0

        for bracket in s:
            if bracket == "(":
                opening += 1
            else:
                opening -= 1
            if opening < 0:
                result += 1
                opening = 0
        return result + abs(opening)
