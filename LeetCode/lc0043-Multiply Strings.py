"""
reverse individual strings. use two pointers for each string. 
use nested for loops to multiple every digit from each string and 
keep on adding to the result array. check for leading zeros. 
convert array back to string.
"""

# time:O(mn), space:O(m+n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # check for empty input
        if len(num1) == 0 or len(num2) == 0:
            return ""

        # check for any string as Zero
        if num1 == "0" or num2 == "0":
            return "0"

        # result should be sum of lens of inputs
        result = [0] * (len(num1) + len(num2))

        # reverse the strings to work on indices from 0 to end
        num1, num2 = num1[::-1], num2[::-1]

        # loop over the two input 
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                result[i1+i2] += digit
                result[i1+i2+1] += result[i1+i2] // 10
                result[i1+i2] = result[i1+i2] %10

        # reverse back the string
        result = result[::-1]

        # check for leading zeros
        beg = 0
        while beg < len(result) and result[beg] == 0:
            beg += 1
        
        # convert into str
        result = map(str, result[beg:])

        return "".join(result)
