# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # 1-collect left_boundary
        def left_boundary(node):
            if not node:
                return 
            # if leaf node
            if not node.left and not node.right:
                return

            left.append(node.val)

            # if not leaf, start traversal from left child
            if node.left:
                left_boundary(node.left)
            else:
                left_boundary(node.right)          

        # 2-collect leaf nodes
        def leaf_nodes(node):
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.left:
                leaf_nodes(node.left)
            if node.right:
                leaf_nodes(node.right)

        # 3-collect right_boundary
        def right_boundary(node):
            if not node:
                return 
            # if leaf node
            if not node.left and not node.right:
                return
            
            # if not leaf, then start traversal from right child then left child
            if node.right:
                right_boundary(node.right)
            else:
                right_boundary(node.left)

            right.append(node.val)

        
        left, leaves, right = [], [], []
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        left_boundary(root.left)
        leaf_nodes(root)
        right_boundary(root.right)

        return [root.val] + left + leaves + right
















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
