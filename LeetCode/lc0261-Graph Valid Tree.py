# DFS - recursion
# time:O(E+V), space:O(E+V)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        # create adjacency list
        adj = dict()
        for i in range(n):
            adj[i] = []

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)


        # def dfs
        def dfs(i, prev):
            # base case
            if i in visited:
                return False
            
            # add to visited
            visited.add(i)

            # precess neighbors of the node in adj list
            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
                
            return True              
        
        visited = set()
        return dfs(0, -1) and len(visited) == n


# BFS - QUEUE
# time:O(E+V), space:O(E+V)
from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        # create adjacency list
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        visited.add(0)

        # bfs
        q = deque([[0,-1]])
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                q.append([nei, node])

        return len(visited) == n
