# disjoint set - union find - time:O(n), space:O(n)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        # return false if can't complete
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                # return false if can't complete
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True


        # calling the fuinctuion
        for n1,n2 in edges:
            if not union(n1, n2):
                return [n1,n2]


# DFS - recursive - time:O(V+E), space:O(V+E)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # define DFS
        def dfs(node, parent):
            # returns True if cycle
            if visited[node]:
                return True

            # otherwise add to the visited
            visited[node] = True

            # process the node's neighbors
            for nei in adj[node]:
                if nei == parent:
                    continue

                if dfs(nei, node):
                    return True

            return False        
        
        # 1- create adjacency list
        adj = [[] for _ in range(len(edges)+1)]

        # 2- traverse edges and pass them to the DFs to check for cycles
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

            visited = [False] * (len(edges)+1)

            if dfs(a, -1):
                return [a,b]

        return []
