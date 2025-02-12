# time:O(haystack), space:O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if haystack == needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            # print(i)
            if haystack[i] == needle[0]:
                j = 0
                while j < len(needle) and haystack[i+j] == needle[j]:
                    j += 1
                if j == len(needle):
                    return i

        return -1




class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        nee = len(needle)
        hay = len(haystack)
        
        for i in range(hay):
            if haystack[i:i+nee] == needle:
                return i
            
        return -1
            
# time:O(needle_len*haystack_len), space:O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)

        for start in range(haystack_len-needle_len+1):
            for needle_index in range(needle_len):
                if haystack[start+needle_index] != needle[needle_index]:
                    break

                if needle_index == needle_len - 1:
                    return start

        return -1
