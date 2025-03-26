# dijkstra algo
# Let n be the number of nodes and m be the number of edges in the graph.
# Time complexity: O((n+m)logn)
# Space complexity: O(n+m)



class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        markedSet = set(marked)

        # build adjacenecy list
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v, w))
            
        
        # init the distances
        dist = [float("inf") for _ in range(n)]
        dist[s] = 0

        minHeap = [(0,s)]

        # dijkstra algo
        while minHeap:
            distance, node = heapq.heappop(minHeap)
            # if found marked node
            if node in markedSet:
                return distance


            # explore neighbors
            for nei, weight in graph[node]:
                new_distance = distance+weight

                if new_distance < dist[nei]:
                    dist[nei] = new_distance
                    heapq.heappush(minHeap, (new_distance, nei))


        return -1





