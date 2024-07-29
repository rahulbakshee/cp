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



        
        
