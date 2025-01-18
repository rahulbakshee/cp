# using DFS - recursion
# time:O(n), space:O(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # looks like DFS - stack

        # base case
        if not root:
            return 0

        # if root present
        def dfs(node, max_val):
            if not node:
                return 0

            if node.val < max_val:
                result = 0
            else:
                result = 1
            max_val = max(max_val, node.val)
            result += dfs(node.left, max_val)
            result += dfs(node.right, max_val)
            
            return result
            
        return dfs(root, float("-inf"))

# using stack
# time:O(n), space:O(n)
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [[root, root.val]]
        result = 0
        while stack:
            node, max_so_far = stack.pop()
            if node.val>=max_so_far:
                result += 1
            max_so_far = max(max_so_far, node.val)

            if node.left:
                stack.append([node.left, max_so_far])
            if node.right:
                stack.append([node.right, max_so_far])

        return result
