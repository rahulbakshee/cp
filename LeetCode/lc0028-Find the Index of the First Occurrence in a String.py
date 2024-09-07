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
