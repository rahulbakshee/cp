# DFS - recursive
# time:O(n^2), space:O(n)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node):
            visited[node] = True
            for i in range(len(isConnected)):
                if isConnected[node][i] and not visited[i]:
                    dfs(i)


        result = 0
        visited = [False] * len(isConnected)
        for i in range(len(isConnected)):
            if not visited[i]:
                result += 1
                dfs(i)

        return result


# BFS - queue 
# time:O(n^2), space:O(n)
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(node):
            visited[node] = True

            q = deque([node])
            while q:
                node = q.popleft()

                for i in range(len(isConnected)):
                    if isConnected[node][i] == 1 and not visited[i]:
                        q.append(i)
                        visited[i] = True
        
        visited = [False] * len(isConnected)
        result = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                result += 1
                bfs(i)

        return result
