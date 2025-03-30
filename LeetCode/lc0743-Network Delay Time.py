# Dijkstra using minHeap
# time:O(V+ElogV) space:O(V+E)
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1 - build the graph
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        # 2 - init distance vector
        distances = {node:float("inf") for node in range(1, n+1)}
        distances[k] = 0
        print(distances)

        # 3 - explore the neighbors
        minHeap = [[0, k]]

        while minHeap:
            d, node = heapq.heappop(minHeap)
            for nei, dw in graph[node]:
                new_d = d+dw
                if new_d < distances[nei]:
                    distances[nei] = new_d

                    heapq.heappush(minHeap, (new_d, nei))

        print(distances)
        value = max(list(distances.values()))
        if value != float("inf"):
            return value
        return -1
