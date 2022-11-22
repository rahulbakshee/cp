# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

# time O(log n)
# space O(1)
class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num > 0:
            if num % 2 ==0 : # even
                num  = num //2
            else: # odd
                num = num -1
            counter += 1

        return counter

