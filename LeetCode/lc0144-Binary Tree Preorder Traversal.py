# recursive
# time:O(n), space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def helper(node):
            if not node:
                return
            
            result.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return result


# iterative
# time:O(n), space:O(n)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                # add parent val to result
                result.append(curr.val)
                # update stack with right child
                stack.append(curr.right)
                # go to left
                curr = curr.left
            else:
                curr = stack.pop()

        return result


