# DFS- time:O(V+E), space:O(V+E)
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # build adjacency list for each vertex
        graph = defaultdict(list)

        # build adjacenecy list from edges
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        completed_count = 0
        visited = set()

        def dfs(curr:int, info:List)->None:
            visited.add(curr)

            info[0] += 1
            info[1] += len(graph[curr])

            for nei in graph[curr]:
                if nei not in visited:
                    dfs(nei, info)

        for vertex in range(n):
            if vertex not in visited:
                component_info = [0,0]
                dfs(vertex, component_info)

                if component_info[0] * (component_info[0] - 1) == component_info[1]:
                    completed_count += 1

        return completed_count
