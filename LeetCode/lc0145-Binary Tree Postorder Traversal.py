# recursive
#time:O(n), space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def helper(node):
            if not node:
                return
            
            # go to left child
            helper(node.left)
            # go to left child
            helper(node.right)
            # add parent to the result
            result.append(node.val)

            
        helper(root)
        return result


# neetcod - REVISE
# iterative
# time:O(n), space:O(n)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        visit = [False]

        while stack:
            curr, v = stack.pop(), visit.pop()
            if curr:
                if v:
                    result.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        return result
