# time:O(n), space:O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = -1

        for i in range(len(arr)-2, -1, -1):
            arr[i], maxx = max(maxx, arr[i+1]), arr[i]

        arr[-1] = -1
        return arr
