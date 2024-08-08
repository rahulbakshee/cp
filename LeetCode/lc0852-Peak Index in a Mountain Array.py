# time:O(n), space:O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                return i-1

# binary search
# time:O(nlogn), space:O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + (right-left)//2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid

        return left
    
