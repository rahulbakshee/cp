# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS - recursive
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum)->bool:
            # base case
            if not node:
                return False
            
            currSum += node.val
            # only when we reach a leaf node
            if not node.left and not node.right:
                return currSum == targetSum
            
            # process
            return dfs(node.left, currSum) or dfs(node.right, currSum)
        

        if not root:
            return False

        return dfs(root, 0)


# iterative  - using stack
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # add the node to stack
        stack = [[root, 0]]

        # pop from stack and process it
        while stack:
            node, currSum = stack.pop()
            currSum += node.val
            if not node.left and not node.right and currSum == targetSum:
                return True
                    
            if node.left:
                stack.append([node.left, currSum])
            if node.right:
                stack.append([node.right, currSum])

        return False


        

# # iteratiev - BFS - using a QUEUE
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        from collections import deque

        if not root:
            return False

        q = deque([[root, 0]])
        while q:
            # pop from queue
            node, currSum = q.popleft()
            currSum += node.val
            
            # process it
            if not node.left and not node.right and currSum == targetSum:
                return True

            # append child again to the queue
            if node.left:
                q.append([node.left, currSum])
            if node.right:
                q.append([node.right, currSum])

        return False
