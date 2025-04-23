# TLE - time:O(n^3), space:O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalindrome(left, right):
            while left<right:
                if s[left] != s[right]:
                    return False

                left += 1
                right-= 1

            return True

        result = s[0]
        result_len = 1

        for left in range(len(s)):
            for right in range(left+1, len(s)):
                if checkPalindrome(left, right):
                    if len(s[left:right+1]) > result_len:
                        result_len = len(s[left:right+1])
                        result = s[left:right+1]

        return result



# expand from center
# time:O(n^2), space:O(1)
# expand from center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_len = 0

        for i in range(len(s)):
            # odd len palindrome
            left, right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > result_len:
                    result_len = right-left+1
                    result = s[left:right+1]
                left -=1
                right += 1

            # even len palindrome
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > result_len:
                    result = s[left:right+1]
                    result_len = right-left+1

                left -= 1
                right += 1
        return result
