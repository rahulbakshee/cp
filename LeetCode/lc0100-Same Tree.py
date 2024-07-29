# DFS
# time:O(min(m, n))- min number of nodes in the tree, space:O(h) - height of tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both empty
        if not p and not q:
            return True
        
        # one of them empty
        if not p or not q:
            return False

        # check values
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
