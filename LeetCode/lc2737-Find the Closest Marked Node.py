# dijkstra algo
# Let n be the number of nodes and m be the number of edges in the graph.
# Time complexity: O((n+m)logn)
# Space complexity: O(n+m)


import heapq
class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        
        # build the graph/adjacency list from edges
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))


        # buidl the set of marked nodes
        markedSet = set(marked)

        # init dict for storing the shortest distcnces
        distance = {i:float("inf") for i in range(n)}
        distance[s] = 0

        # init heap with distance and node
        minHeap = [[0,s]]

        # dijkstra's algo
        while minHeap:
            dist, node = heapq.heappop(minHeap)
            
            # reached destination
            if node in markedSet:
                return distance[node]

            # explore its neighbors
            for nei, dw in graph[node]:
                new_dist = dist + dw

                if new_dist < distance[nei]:
                    distance[nei] = new_dist
                    # push into the heap
                    heapq.heappush(minHeap, (new_dist, nei))
           

        return -1
