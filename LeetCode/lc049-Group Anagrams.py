# https://leetcode.com/problems/group-anagrams/

import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            item = tuple(sorted(s)) 
            if item in d:
                d[item].append(s)
            else:
                d[item] = []
                d[item].append(s)
            
            #print(d)

        return d.values()
        
