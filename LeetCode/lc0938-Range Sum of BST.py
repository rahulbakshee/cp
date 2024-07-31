# recursive DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            # base case
            if not node:
                return 0
            
            if node.val >= low and node.val <= high:
                return node.val+ dfs(node.left) + dfs(node.right)
            else:
                return dfs(node.left) + dfs(node.right)

        return dfs(root)

# BST - recursive DFS-
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            # base case
            if not node:
                return 0
            
            if node.val > high:
                return dfs(node.left)
            if node.val < low:
                return dfs(node.right)
            if node.val >= low and node.val <= high:
                return node.val + dfs(node.left) + dfs(node.right)
        return dfs(root)


# time:O(n), space:O(logn for binary tree or n  for unbalanced tree in worst case)
# BST - iterative - BFS
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        if not root:
            return result
        
        # BFS using queue
        from collections import deque
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                if low <= node.val <= high:
                    result += node.val
                if node.val > low:
                    q.append(node.left)
                if node.val < high:
                    q.append(node.right)
                
        return result
