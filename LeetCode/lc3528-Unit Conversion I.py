# recursive DFS - time:O(V+E), space:O(V)
class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        # 1- build the adj list
        # 2 - run DFS

        def dfs(node):
            for target, factor in graph[node]:
                result[target] = (result[node] * factor) %MOD
                dfs(target)


        graph = defaultdict(list)
        for source, target, factor in conversions:
            graph[source].append([target, factor])

        MOD = 10 **9 + 7
        n = len(conversions)
        result = [1] * (n+1)
        dfs(0)
        return result



# BFS - queue - time:O(V+E), space:O(V)
from collections import deque
class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        if not conversions:
            return []
        
        graph = defaultdict(list)
        for source, target, factor in conversions:
            graph[source].append([target, factor])

        MOD = 10 **9 + 7
        n = len(conversions)
        result = [1] * (n+1)

        q = deque([0])
        while q:
            node = q.popleft()
            for target, factor in graph[node]:
                result[target] = (result[node] * factor) % MOD

                # explore neighbors
                q.append(target)

        return result


# DFS - stack - time:O(V+E), space:O(V)
class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        if not conversions:
            return []
        
        graph = defaultdict(list)
        for source, target, factor in conversions:
            graph[source].append([target, factor])

        MOD = 10 **9 + 7
        n = len(conversions)
        result = [1] * (n+1)

        stack = [0]
        while stack:
            node = stack.pop()
            for target, factor in graph[node]:
                result[target] = (result[node] * factor) % MOD

                # explore neighbors
                stack.append(target)

        return result
