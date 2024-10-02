# time:O(nlogn+n), space:O(n)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))
        rank_dict = dict()
        for rank, num in enumerate(sorted_arr):
            rank_dict[num] = rank+1
        
        result = [] 
        
        for num in arr:
            result.append(rank_dict[num])

        return result
