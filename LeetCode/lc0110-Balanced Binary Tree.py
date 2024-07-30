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
