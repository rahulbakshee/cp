# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = [s for s in stones]
        d = {}
        counter = 0
        for s in stones:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        
        for j in jewels:
            if j in d.keys():
                counter += d[j]
                
        return counter
