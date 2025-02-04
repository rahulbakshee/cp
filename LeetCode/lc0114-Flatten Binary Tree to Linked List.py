# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time:O(n), space:O(n)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flattenTree(node):
            if not node:
                return

            # leaf node
            if not node.left and not node.right:
                return node

            # recursively flatten left subtree
            leftTail = flattenTree(node.left)

            # recursively flatten right subtree
            rightTail = flattenTree(node.right)

            # bring all left tree nodes to right side
            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            return rightTail if rightTail else leftTail
        
        if not root:
            return 
        flattenTree(root)
