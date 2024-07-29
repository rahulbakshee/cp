# recursive DFS
# time:O(n) - n being the number of nodes in the tree, space:O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)
        
        
    def helper(self, node):
        # base case
        if not node:
            return 0

        left_h = self.helper(node.left)
        right_h = self.helper(node.right)

        return max(left_h, right_h) + 1


# BFS - level order
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        from collections import deque
        q = deque([root])
        level = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            level += 1

        return level

        
        
# iterative DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        result = 1
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            
            if node:
                result = max(result, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return result
