# DFS - recursion
# time:O(n), space:O(n)
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a,b) for a,b in connections}
        neighbors = {city:[] for city in range(n)}
        visited = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)


        def dfs(city):
            nonlocal changes

            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                
                # check if neighbor can reach city 0
                if (neighbor, city) not in edges:
                    changes += 1

                visited.add(neighbor)

                dfs(neighbor)
        
        
        visited.add(0)
        dfs(0)
        return changes


# BFS - queue
# time:O(n), space:O(n)
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append((v,1))
            adj[v].append((u,0))

        visited = [False] * n
        q = deque([0])
        visited[0] = True
        changes = 0

        while q:
            node = q.popleft()
            for neighbor, isForward in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    changes += isForward
                    q.append(neighbor)

        return changes
