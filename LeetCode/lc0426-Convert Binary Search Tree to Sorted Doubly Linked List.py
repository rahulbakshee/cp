"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        def link_inorder(node):
            if node:
                link_inorder(node.left)


                if not self.last:
                    self.first = node
                else:
                    node.left = self.last
                    self.last.right = node

                self.last = node

                link_inorder(node.right)                

        self.first = self.last = None

        link_inorder(root)

        self.first.left = self.last
        self.last.right = self.first

        return self.first
