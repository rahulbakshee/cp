# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

# time limit exceeded
# time:O(nk), space:O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_counter = 0

        vowels = {"a", "e", "i", "o", "u"}
        
        for i in range(len(s)-k+1):
            substring = s[i:i+k]
            counter = 0
            for j in range(k):
                if substring[j] in vowels:
                    counter += 1
            max_counter = max(max_counter, counter)

        return max_counter



# two pointers
# time:O(n), space:O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_count, count = 0, 0

        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            if i>=k and s[i-k] in vowels:
                count -= 1
            max_count = max(max_count, count)

        return max_count
