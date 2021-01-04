# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = []
        if x < 0:  return False
        if x == 0: return True
        while x > 0:
            r = x % 10
            l.append(r)
            x = x // 10

        counter = 0
        for i in range(0, len(l)//2):
            if l[i] != l[len(l) - i - 1]: 
                counter = 1
                break
        if counter == 0: return True
        else: return False
