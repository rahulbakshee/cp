# BFS - using QUEUE - time:O(n), space:O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        # looks like we need to do level-order traversal
        from collections import deque
        q = deque([root])

        while q:
            rightSide = None
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
                    
            if rightSide:
                result.append(rightSide.val)
        return result


# DFS - recursive - time:O(n), space:O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node, level):
            if not node:
                return

            if level == len(result):
                result.append(node.val)

            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return result
