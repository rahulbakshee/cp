# time:O(nlogn), space:O(n)
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        counter1 = Counter(word1)
        counter2 = Counter(word2)


        return ((sorted(counter1.keys()) == sorted(counter2.keys())) and 
                (sorted(counter1.values()) == sorted(counter2.values())))
            
