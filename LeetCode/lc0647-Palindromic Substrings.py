# n^2, 1
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            # odd length palindrome
            result += self.countPalindrome(s, i, i)

            # even lenght palindrome
            result += self.countPalindrome(s, i, i+1)

        return result


    def countPalindrome(self, s, left, right)->int:
        result = 0
        while left >=0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1

        return result
