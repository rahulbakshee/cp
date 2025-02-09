class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        operations = 0
        prefix_sum = 0
        pq = []

        for num in nums:
            if num < 0:
                heapq.heappush(pq, num)

            prefix_sum += num
            if prefix_sum < 0:
                prefix_sum -= heapq.heappop(pq)
                operations += 1
        return operations
