# time:O(nlogn), space:O(n/sorting)
class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        if arr == brr:
            return 0

        without_sorting_cost = 0
        for i in range(len(arr)):
            without_sorting_cost += abs(arr[i] - brr[i])

        # check for cost when we sort the input        
        arr.sort()
        brr.sort()
        with_sorting_cost = 0
        for i in range(len(arr)):
            with_sorting_cost += abs(arr[i] - brr[i])

        return min(without_sorting_cost, with_sorting_cost+k)
