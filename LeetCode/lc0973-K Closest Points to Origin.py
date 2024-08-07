# time:O(n logk) - k is the size of heap, n is the len of points
# space:O(n)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
            
        for point in points:
            dist = -1 * (point[0] **2 + point[1] **2)
            heapq.heappush(heap, [dist, point])

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            _, point = heapq.heappop(heap)
            result.append(point)

        return result
