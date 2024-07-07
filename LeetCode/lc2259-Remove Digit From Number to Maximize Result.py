# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/

# time:O(n), space:O(1)
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        max_number = 0

        for i in range(len(number)):
            if number[i] == digit:
                curr_number = number[:i] + number[i+1:]
                max_number = max(max_number, int(curr_number))
        return str(max_number)
