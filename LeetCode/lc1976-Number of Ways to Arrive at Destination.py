# Let N be the number of nodes in the graph and E be the number of edges in the given road connections.

# Time Complexity: O(N+ElogE)
# Space complexity: O(N+E)


import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        MOD = 10**9+7

        # 1 - build the graph/adjacency list
        graph = defaultdict(list)
        for u,v,time in roads:
            graph[u].append([v,time])
            graph[v].append([u, time])

        # 2- initialize the distances dict for all the nodes
        times = {node:float("inf") for node in range(n)}
        times[0] = 0

        path_count = [0] * n
        path_count[0] = 1

        # 3 - use minHeap to get the minimum distances from source to destination nodes
        minHeap = [[0,0]] # [time, node]
        while minHeap:
            t, node = heapq.heappop(minHeap)

            # explore the neighbosing nodes of n
            for nei, dt in graph[node]:
                new_t = t+dt
                # update the time to reach that node in the times dictionary
                if new_t < times[nei]:
                    times[nei] = new_t
                    # and the path count
                    path_count[nei] = path_count[node]

                    # feed this neighbor with its time to the minHeap
                    heapq.heappush(minHeap, [new_t, nei])

                elif new_t == times[nei]:
                    path_count[nei] = (path_count[nei] + path_count[node]) % MOD

        return path_count[n-1]
