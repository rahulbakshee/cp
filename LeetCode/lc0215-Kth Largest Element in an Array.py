

# sorting
# time:O(nlogn), space:O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        return nums[k-1]


# time:O(nlogk), space:O(k)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return heapq.heappop(minHeap)


# Time complexity: O(n) on average, O(n^2) in the worst case
# space:O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quickSelect(left, k)
            
            if len(left)+len(mid) < k:
                return quickSelect(right, k-len(left)-len(mid))
            
            return pivot
        return quickSelect(nums, k)
