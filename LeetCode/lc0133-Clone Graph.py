"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# DFS recursion
# time:O(V+E), space:O(V)
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            # create node
            copy = Node(node.val)
            oldToNew[node] = copy

            # create neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy       
        
        
        if not node:
            return
        oldToNew = {}
        return dfs(node)



# time:O(V+E), space:O(v)
# BFS - queue
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])
        
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                oldToNew[n].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]
