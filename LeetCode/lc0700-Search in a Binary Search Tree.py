# recursion 
# time: worst O(h) height of tree when tree is balanced, O(n) unbalanced
# space: worst O(h) height of tree when tree is balanced, O(n) unbalanced
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS - recursive  - time:O(n), space:O(n)
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

# DFS - stack - time:O(n), space:O(n)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return 
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                    
                if node.val>val:
                    stack.append(node.left)
                elif node.val<val:
                    stack.append(node.right)
                else:
                    return node

        return None

# BFS - queue, time:O(n), space:O(n)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return 
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                if node.val > val:
                    q.append(node.left)
                elif node.val < val:
                    q.append(node.right)
                else:
                    return node

        return
