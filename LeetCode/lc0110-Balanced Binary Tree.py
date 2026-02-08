# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
# time:O(n), space:O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            # base case
            if not node:
                return [0, True] # [height, bool]

            left = height(node.left)
            right = height(node.right)

            balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1

            return [1+max(left[0], right[0]), balanced]
        return height(root)[1]


# Another solution
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs_helper(node):
            if not node:
                return [True, 0]
            
            if not node.left and not node.right:
                return [True, 1]

            left_tree = dfs_helper(node.left)
            right_tree = dfs_helper(node.right)

            balanced = (left_tree[0] and 
                        right_tree[0] and 
                        abs(left_tree[1] - right_tree[1]) <= 1)
            
            height = 1 + max(left_tree[1], right_tree[1])

            return [balanced, height]

        if not root:
            return True
        return dfs_helper(root)[0]
