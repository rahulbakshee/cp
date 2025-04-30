# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_num):
            nonlocal result
            
            if not node:
                return

            curr_num = curr_num * 10 + node.val

            if not node.left and not node.right:
                result += curr_num

            dfs(node.left, curr_num)
            dfs(node.right, curr_num)


        result = 0
        dfs(root, 0)
        return result





# iterative DFS - using stack
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        result = 0
        stack = [[root, 0]]

        while stack:
            node, curr_num = stack.pop()
            
            curr_num = curr_num * 10 + node.val

            if not node.left and not node.right:
                result += curr_num

            if node.left:
                stack.append([node.left, curr_num])

            if node.right:
                stack.append([node.right, curr_num])


        return result





# iterative BFS - using queue
from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0
        q = deque([[root, 0]])

        while q:
            node, curr_num = q.popleft()

            curr_num = curr_num *10 + node.val

            if not node.left and not node.right:
                result += curr_num

            if node.left:
                q.append([node.left, curr_num])

            if node.right:
                q.append([node.right, curr_num])


        return result
