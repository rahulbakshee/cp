# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time:O(n), space:O(n)
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, isLeft, isRight):
            if not root:
                return
            
            # append the node.val to boundry if conditions met
            
            # 1- if left boundry node or leaf node
            if (not root.left and not root.right) or isLeft:
                boundry.append(root.val)
            
            # 2- if node is having both left n right child - pass on those children to DFS
            if root.left and root.right:
                dfs(root.left, isLeft, False)
                dfs(root.right, False, isRight)
            else:
                dfs(root.left, isLeft, isRight)
                dfs(root.right, isLeft, isRight)
            
            # 3- if the node is on the right boundry
            if (root.left or root.right) and isRight:
                boundry.append(root.val)          

        if not root:
            return []

        boundry = [root.val]
        # start from left side
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return boundry
