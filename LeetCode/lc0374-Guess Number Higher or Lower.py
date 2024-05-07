# https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# time limit exceeded
# time-O(n), space-O(1)
# class Solution:
#     def guessNumber(self, n: int) -> int:
#         for i in range(1, n+1):
#             if guess(i) == 0:
#                 return i


# binary search
# time-O(logn), space(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right-left)//2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                pass
        return left

