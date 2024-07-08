# https://leetcode.com/problems/top-k-frequent-words/description/

# using hashmap/dictionary
# time:O(n logn n), space:O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        seen = dict()
        for word in words:
            if word in seen:
                seen[word] += 1
            else:
                seen[word] = 1
        
        # sort the dict
        result = sorted(seen, key=lambda word:(-seen[word], word))
        return result[:k]
