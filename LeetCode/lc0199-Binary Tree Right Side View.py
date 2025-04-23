# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = deque([root])
        level = 0

        while q:
            for _ in range(len(q)):
                    
                node = q.popleft()
            
                if level == len(result):
                    result.append(node.val)
                    
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            level += 1

        return result

# DFS - recursive - time:O(n), space:O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node, level):
            if not node:
                return

            if level == len(result):
                result.append(node.val)

            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return result



# DFS - stack
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [[root, 0]] # node, level
        while stack:
            node, level = stack.pop()

            if level == len(result):
                result.append(node.val)
            
            # left first and then right child

            if node.left:
                stack.append([node.left, level+1])

            if node.right:
                stack.append([node.right, level+1])

        return result





