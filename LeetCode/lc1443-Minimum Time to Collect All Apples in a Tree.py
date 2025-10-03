class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        def dfs(curr, prev):
            time = 0

            for child in graph[curr]:
                if child == prev:
                    continue

                childTime = dfs(child, curr)
                if childTime > 0 or hasApple[child]:
                    time += 2 + childTime

            return time


        return dfs(0, -1)
