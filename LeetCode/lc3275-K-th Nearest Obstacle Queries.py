# time:O(n logk), space:O(n+k)
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
                
        maxHeap = []
        result = []

        for query in queries:
            x, y = query
            distance = abs(x) + abs(y)
            heapq.heappush(maxHeap, -distance)
            
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)


            if len(maxHeap) < k:
                result.append(-1)
            else:
                result.append(-1*maxHeap[0])               
        return result



