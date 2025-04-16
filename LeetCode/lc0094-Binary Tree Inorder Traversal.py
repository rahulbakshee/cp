
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# recursive
# time:O(n), space:O(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)

        helper(root)
        return result

# same as above
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            result = []

            # 1- left subtree
            if node.left:
                left_subtree = dfs(node.left)
                result.extend(left_subtree)

            # 2- root node's val
            result.append(node.val)

            # 3- right subtree
            if node.right:
                right_subtree = dfs(node.right)
                result.extend(right_subtree)

            return result

        if not root:
            return []

        return dfs(root)

# iterative
#time:O(n), space:O(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result
