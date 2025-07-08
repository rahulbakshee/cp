# bruteforce
"""
Algorithm
Find the shorter string among str1 and str2, without loss 
of generality, let it be str1. Start with base = str1, and 
check if both str1 and str2 are made of multiples of base. 
If so, return base. Otherwise, we shall try a shorter string 
by removing the last character from base. If we have checked 
all prefix strings without finding the GCD string, return "".
"""
# time:O(min(m,n)*(m+n)), space:O(min(m,n))
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        def valid(l):
            # l is the factor of lengths
            if l1 % l or l2 % l:
                return False

            # check if replicating the string till "l" index works
            f1, f2 = l1//l, l2//l
            base = str1[:l]
            return base * f1 == str1 and base * f2 == str2

        for i in range(min(l1, l2), 0, -1):
            if valid(i):
                return str1[:i]

        return ""


# using GCD function
"""
Algorithm
Check if the concatenations of str1 and str2 in different orders
 are the same. If not, return "".
Get the GCD gcdLength of the two lengths of str1 and str2.
Return the prefix string with a length of gcdLength of either
str1 or str2 as the answer.
"""
# time:O(m+n), space:O(m+n)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""

        # get the GCD of the two lengths
        max_len = gcd(len(str1), len(str2))
        return str1[:max_len]
