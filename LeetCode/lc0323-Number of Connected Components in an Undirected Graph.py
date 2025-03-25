simple DFS
# time:O(V+E), space:O(V+E)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # 3 - define DFS to go over all the vertex
        def dfs(vertex, visited):
            if vertex in visited:
                return

            # add it to visited
            visited.add(vertex)

            # start exploring its neighbors
            for nei in graph[vertex]:
                if nei not in visited:
                    dfs(nei, visited)
        
        
        # 1 - build adjacenecy graph from edges
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        # 2 - process the nodes from 0 to n-1 using given n
        visited = set()
        components = 0
        for vertex in range(n):
            if vertex not in visited:
                dfs(vertex, visited)
                components += 1

        return components


# DFS - stack
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        for i in range(n):
            if i not in visited:
                components += 1
                stack = [i]
                visited.add(i)
                while stack:
                    vertex = stack.pop()
                
                    for nei in graph[vertex]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)


        return components
                

# BFS - queue
from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                components += 1

                q = deque([i])
                while q:
                    vertex = q.popleft()
                    for nei in graph[vertex]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)


        return components
