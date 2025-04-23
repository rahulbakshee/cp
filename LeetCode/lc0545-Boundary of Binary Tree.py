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

        if not root.left and not root.right:
            return [root.val]

        def collect_left_nodes(node):
            if not node:
                return 
            
            # if its a leaf node
            if not node.left and not node.right:
                return

            left_nodes.append(node.val)

            if node.left:
                collect_left_nodes(node.left)
            else:
                collect_left_nodes(node.right)

        def collect_leaves(node):
            if not node:
                return
            
            # if a leaf, then append to the result array
            if not node.left and not node.right:
                leaves.append(node.val)

            if node.left:
                collect_leaves(node.left)

            if node.right:
                collect_leaves(node.right)


        def collect_right_nodes(node):
            if not node:
                return
            
            # if leaf node then return
            if not node.left and not node.right:
                return

            if node.right:
                collect_right_nodes(node.right)
            else:
                collect_right_nodes(node.left)

            right_nodes.append(node.val)
            

        left_nodes, leaves, right_nodes = [],[],[]

        collect_left_nodes(root.left)
        collect_leaves(root)
        collect_right_nodes(root.right)

        return [root.val] + left_nodes + leaves + right_nodes
















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
