# DFS - recursion
# time:O(V+E), space:O(V+E)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)


        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)


        components = 0
        visited = set()
        for node in range(1, n+1):
            if node not in visited:
                visited.add(node)
                dfs(node)
                components += 1

        return components



# DFS - iterative - stack
# time:O(V+E), space:O(V+E)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # build the graph
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)


        # stack and append to stack
        components = 0
        visited = set()
        for index in range(1, n+1):
            if index not in visited:
                visited.add(index)
                stack = [index]

                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)


                components += 1

        return components



# BFS - iterative - queue
# time:O(V+E), space:O(V+E)
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        # build the graph
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)

        # BFS - append to queue
        visited = set()
        components = 0
        for index in range(1, n+1):
            if index not in visited:
                visited.add(index)
                q = deque([index])

                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                components += 1

        return components
