"""
Algorithm
Initialize an empty string ans which would store the column title.

Do the following as long as columnNumber is greater than 0:

Subtract 1 from the columnNumber
Find the character corresponding to columnNumber % 26 and append it to the ans in the end.
Assign columnNumber to columnNumber / 26.
Reverse the string columnNumber and return it.
"""
# time:(logn base 26), space:O(1)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            result += chr(ord("A") + offset)
            columnNumber = columnNumber // 26

        return "".join(result[::-1])
