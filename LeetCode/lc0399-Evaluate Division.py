# time:O(V + E + Q), space:O(V + E)
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.weight = {}
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0
    
    def find(self, x):
        if x != self.parent[x]:
            orig_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.weight[x] *= self.weight[orig_parent]
        return self.parent[x]
    
    def union(self, x, y, value):
        self.add(x)
        self.add(y)
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.weight[root_x] = value * self.weight[y] / self.weight[x]
    
    def get_ratio(self, x, y):
        if x not in self.parent or y not in self.parent or self.find(x) != self.find(y):
            return -1.0
        return self.weight[x] / self.weight[y]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        
        for (a, b), value in zip(equations, values):
            uf.union(a, b, value)
        
        return [uf.get_ratio(a, b) for a, b in queries]




# DFS - recursive
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1-build graph
        graph = defaultdict(list)
        for i in range(len(equations)):
            n, d = equations[i]
            graph[n].append([d, values[i]])
            graph[d].append([n, 1./values[i]])

        # 2-define DFs - check whether there is path between sourc and target
        def dfs(source, target, visited):
            if source not in graph or target not in graph:
                return -1.

            if source == target:
                return 1.

            visited.add(source)

            for nei, w in graph[source]:
                if nei not in visited:
                    res = dfs(nei, target, visited)
                    if res != -1.:
                        return res * w                

            return -1.

        # 3-call dfs
        result = []
        for q1,q2 in queries:
            result.append(dfs(q1,q2, set()))

        return result

        

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1 - build the graph
        graph = defaultdict(list) # {n1:[[d1,val1], [d2,val2]], n2:...}
        for i in range(len(equations)):
            n, d = equations[i]
            graph[n].append([d, values[i]])
            graph[d].append([n, 1./values[i]])


        # 2-BFS - find path from source to target and multiply edges
        def bfs(source, target):
            # if any of the source/target not in adj list, return -1
            if source not in graph or target not in graph:
                return -1.

            visited = set()
            q = deque()

            q.append((source, 1))
            visited.add(source)

            while q:
                node, weight = q.popleft()
                if node == target:
                    return weight

                for nei, w in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, weight*w))

            return -1.

        # 3 call BFS-go over queries and feed a, b into BFS
        result = []
        for q1, q2 in queries:
            result.append(bfs(q1, q2))

        return result
