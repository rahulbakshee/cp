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


# SIMPLER by ME
class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        if not nums:
            return [1]

        added = False
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 9:
                nums[i] = 0
                continue
            else:
                nums[i] += 1
                added = True
                break

        if not added:
            return [1] + nums
        else:
            return nums






# ignore below one, follow above simpler one

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
