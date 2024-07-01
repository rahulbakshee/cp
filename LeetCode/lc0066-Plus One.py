# https://leetcode.com/problems/plus-one/description/

# converting given list to string and then int and then adding one 
# and then converting back to string and then list
# time:O(n), space:O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for d in digits:
            s += str(d)
        s = str(int(s)+1)
        return list(map(int, s))


# copied from https://leetcode.com/problems/plus-one/solutions/24085/simple-python-solution-with-explanation-plus-one/comments/222704
# time:O(n), space:O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1
        while digits[length] == 9:
            digits[length] = 0
            length -= 1
        if(length < 0):
            digits = [1] + digits
        else:
            digits[length] += 1
        return digits
