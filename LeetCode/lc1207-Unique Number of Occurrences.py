# time:O(n), space:O(n)
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dict = Counter(arr)
        print(arr_dict.values())
        
        return len(set(arr_dict.values())) == len(arr_dict.values())
