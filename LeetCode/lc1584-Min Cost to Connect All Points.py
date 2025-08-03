# time:O(n^2logn), space:O(n^2)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # 1 - adj list
        graph = {i:[] for i in range(n)} # i:list of [cost, node]

        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1, n):
                x2,y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)

                graph[i].append([dist, j])
                graph[j].append([dist, i])


        # 2 - prim's
        result = 0
        visited = set()
        minHeap = [[0,0]] # [cost, point]

        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue

            visited.add(i)
            result += cost

            for nei_cost, nei in graph[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [nei_cost, nei])


        return result
