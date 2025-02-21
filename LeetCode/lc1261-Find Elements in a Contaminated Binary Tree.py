# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS - recursion
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.dfs(root, 0)

    def dfs(self, node, value):
        if not node:
            return

        # update seen set
        self.seen.add(value)
        
        # left child
        if node.left:
            self.dfs(node.left, 2*value+1)

        # right child
        if node.right:
            self.dfs(node.right, 2*value+2)

        

    def find(self, target: int) -> bool:
        return target in self.seen




# DFS - stack
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        if not root:
            return False
        self.stack = [[root, 0]]
        while self.stack:
            node, value = self.stack.pop()

            # update seen set
            self.seen.add(value)

            # left
            if node.left:
                self.stack.append([node.left, 2*value+1])
            
            # right
            if node.right:
                self.stack.append([node.right, 2*value+2])

    def find(self, target: int) -> bool:
        return target in self.seen


# BFS - queue
from collections import deque

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        if not root:
            return False

        q = deque([[root, 0]])
        while q:
            node, value = q.popleft()        
            
            # update seen set
            self.seen.add(value)

            # left
            if node.left:
                q.append([node.left, 2*value+1])
            
            # right
            if node.right:
                q.append([node.right, 2*value+2])

    def find(self, target: int) -> bool:
        return target in self.seen
        

