# sorting - time:O(nlogn), space:O(n)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(point):
            x, y = point
            return x**2 + y**2

        points.sort(key=get_distance)

        return points[:k]


# heaps - time:O(nlogk), space:O(k)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(point):
            x, y = point
            return x**2 + y**2

        
        maxHeap = []
        for point in points:
            dist = get_distance(point)

            heapq.heappush(maxHeap, [-1*dist, point])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        result = []
        for _ in range(k):
            d, point = heapq.heappop(maxHeap)
            result.append(point)

        return result


# quick_select time:O(n) avg, O(n^2) worst, space:O(n)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(point):
            x, y = point
            return x**2 + y**2


        def quick_select(points, k):
            pivot = get_distance(random.choice(points))

            left, mid, right = [], [], []

            for point in points:
                d = get_distance(point)

                if d < pivot: # closer to origin
                    left.append(point)

                elif d > pivot: # farther from origin
                    right.append(point)
                
                else: # d == pivot
                    mid.append(point)

            # identify which sublist to focus on for 
            # the next round of recursion
            if k <= len(left):
                return quick_select(left, k)
            if k > len(left)+len(mid):
                return left + mid + quick_select(right, k-len(left)-len(mid))
            return left + mid
        
        return quick_select(points, k)
