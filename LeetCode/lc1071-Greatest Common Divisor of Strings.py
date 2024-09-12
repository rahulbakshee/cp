# time:O(min(m,n)*(m+n)), space:O(min(m+n))
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isValid(k):
            if len1%k or len2%k:
                return False

            n1, n2 = len1//k, len2//k
            base = str1[:k]
            return str1 == n1*base and str2 == n2*base 


        for i in range(min(len1, len2), 0, -1):
            if isValid(i):
                return str1[:i]

        return ""
