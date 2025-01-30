class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return "0"
        abs_num = abs(num)
        result = ""

        while abs_num:
            result = str(abs_num%7) + result
            abs_num = abs_num // 7

        if num < 0:
            return "-" + result
        else:
            return result
