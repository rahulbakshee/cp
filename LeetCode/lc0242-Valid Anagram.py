# https://leetcode.com/problems/valid-anagram/


# SORTING - time:O(nlogn), space:O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)



# space O(n), time O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        for si in s:
            if si in t:
                t = t.replace(si, "", 1)
            else:
                return False
        if len(t) == 0:
            return True
        else:
            return False

# space O(s), time O(s)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False        
        from collections import defaultdict

        sdict, tdict = defaultdict(int), defaultdict(int)
        for index in range(len(s)):
            sdict[s[index]] +=1
            tdict[t[index]] += 1

        if sdict == tdict:
            return True
        else:
            return False




# space O(s), time O(s)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(t) == Counter(s)

# NOT SURE
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# option1 - remove the unicode characters by using s[i].isalpha()
# option2 - keep unicode characters as well. maybe use ord()
