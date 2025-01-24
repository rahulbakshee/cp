# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time:O(n), space:O(n)
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, goLeft, steps):
            nonlocal pathlen
            # base case
            if not node:
                return 

            pathlen = max(pathlen, steps)
            if goLeft:
                dfs(node.left, False, steps+1)
                dfs(node.right, True, 1)
            else:
                dfs(node.left, False, 1)
                dfs(node.right, True, steps+1)
        
        pathlen = 0
        dfs(root, True, 0)
        return pathlen
