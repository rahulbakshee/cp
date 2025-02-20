# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time:O(n), space:O(n)

# DFS recursion
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_bound, right_bound):
            # base case
            if not node:
                return True

            # check for boundariues (of BST)
            if not (left_bound<node.val<right_bound):
                return False

            return dfs(node.left, left_bound, node.val) and dfs(node.right, node.val, right_bound)

        if not root:
            return True
        
        return dfs(root, float("-inf"), float("inf"))

# DFS stack
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [[root, float(-inf), float("inf")]]
        while stack:
            node, left_bound, right_bound = stack.pop()

            if node:
                if not (left_bound < node.val < right_bound):
                    return False

                    
                stack.append([node.left, left_bound, node.val])
                stack.append([node.right, node.val, right_bound])

        return True

# BFS queue
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([[root, float(-inf), float("inf")]])
        while q:
            node, left_bound, right_bound = q.popleft()

            if node:
                if not (left_bound < node.val < right_bound):
                    return False

                    
                q.append([node.left, left_bound, node.val])
                q.append([node.right, node.val, right_bound])

        return True
