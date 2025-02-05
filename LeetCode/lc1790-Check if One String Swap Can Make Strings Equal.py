# time:O(n), space:O(1)
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        if s1 == s2:
            return True

        indexes = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indexes.append(i)
                if len(indexes) > 2:
                    return False
        
        if not (len(indexes) in [0,2]):
            return False

        if ((s1[indexes[0]] == s2[indexes[1]]) and (s1[indexes[1]] == s2[indexes[0]])):
            return True
        else:
            return False
