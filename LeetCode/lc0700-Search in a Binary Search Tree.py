# recursion 
# time: worst O(h) height of tree when tree is balanced, O(n) unbalanced
# space: worst O(h) height of tree when tree is balanced, O(n) unbalanced
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return 

        if val < root.val:
            return self.searchBST(root.left, val)
        
        elif val > root.val:
            return self.searchBST(root.right, val)
        
        return root




# iterative
# time:O(h) worst O(n)
# space:O(1)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case
        if not root or root.val == val:
            return root
        
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else: #root.val == val
                return root

        return root
