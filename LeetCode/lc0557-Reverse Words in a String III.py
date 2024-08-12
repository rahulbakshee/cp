# two pointers
# time:O(n), space:O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        
        left = 0
        for right in range(len(s)):
            if s[right] == " " or right == len(s)-1:
                temp_left, temp_right = left, right -1

                if right == len(s)-1:
                    temp_right = right

                # two pointers to reverse the word
                while temp_left < temp_right:
                    s[temp_left], s[temp_right] = s[temp_right], s[temp_left]
                    temp_left += 1
                    temp_right -= 1

                left = right +1

        return "".join(s)
