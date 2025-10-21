# recursive  - DFS - time:O(n), space:O(n)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            nonlocal result
            
            if node:
                if low <= node.val <= high:
                    result += node.val

                if node.val > low:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
                    
        if not root:
            return 0
        result = 0
        dfs(root)    
        return result



# iterative  - DFS - time:O(n), space:O(n)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        result = 0

        stack = [root]
        while stack:
            node = stack.pop()

            if node:
                if low <= node.val <= high:
                    result += node.val

                if node.val > low:
                    stack.append(node.left)

                if node.val < high:
                    stack.append(node.right)
        return result
