# https://neetcode.io/problems/string-encode-and-decode
# https://leetcode.com/problems/encode-and-decode-strings/description/

# time-O(n) - n is the total number of characters in the input string
# space-O(1)
class Solution:

    def encode(self, strs: List[str]) -> str:
        outputs = ""
        for s in strs:
            outputs += str(len(s)) + "#" + s

        return outputs


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            result.append(s[j+1: j+1+length])
            i = j+1+length
        return result
        
