# time:O(n), space:O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1] * len(arr)
        
        for i in range(len(result)-2, -1, -1):
            result[i] = max(arr[i+1], result[i+1])

        return result
