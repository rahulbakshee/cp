# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# did not understand much. followed the editorial.
# time:O(logn), space:O(h) - n-number of nodes in tree, h-height
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # one step right and then always left
        def successor(root):
            root = root.right
            while root.left:
                root = root.left
            return root.val

        # one step left and then always right
        def predecessor(root):
            root = root.left
            while root.right:
                root = root.right
            return root.val

        if not root:
            return 

        # delete from right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # node is a leaf
            if not root.left and not root.right:
                root = None
            # node is not leaf and has right child
            elif root.right:
                root.val = successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # node is not leaf and has left child
            else:
                root.val = predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root


# easy to understand
# https://leetcode.com/problems/delete-node-in-a-bst/solutions/821420/python-o-h-solution-explained/?envType=study-plan-v2&envId=leetcode-75
class Solution(object):
    def deleteNode(self, root, key):
        if not root: 
            return None
        
        if root.val == key:
            if not root.right: 
                return root.left
            
            if not root.left: 
                return root.right
            
            if root.left and root.right:
                temp = root.right
                while temp.left: 
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root
