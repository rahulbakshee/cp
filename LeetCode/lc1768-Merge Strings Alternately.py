class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        # loop over the word1
        # append char by char from word1 and word2 to the result
        # if any word is still remaining, then append it to the result

        # time:O(m+n) - m in len of word1, n is len of word2
        # space:O(1) assuming not counting the space for result 

        m, n = 0,0
        result = ""

        while m <len(word1) and n<len(word2):
            result += word1[m]
            result += word2[n] 
            m += 1
            n += 1
        if m<len(word1):
            result += word1[m:]
        if n<len(word2):
            result += word2[n:]
        
        return result
"""
word1 = "pq"
word2 = "abcd"

result = 
"""
