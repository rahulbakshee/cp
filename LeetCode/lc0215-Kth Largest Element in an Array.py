

# sorting
# time:O(n logn ), space:O(sorting)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]



# time:O(k + (n-k) log k)
# O(k) for heapifying the first k elements into heap
# loop over (n-k) elements to push and pop from heap O(log k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            heapq.heappushpop(heap, n)
        return heap[0]
