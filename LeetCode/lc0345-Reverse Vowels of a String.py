# time:O(n), space:O(1)
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        s= list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"}


        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1

            # swap
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)
