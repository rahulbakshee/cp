# BFS - queue - time:O(n), space:O(n)
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        max_level_sum = float("-inf")
        result = 0

        from collections import deque
        q = deque([root])
        while q:
            level += 1
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
            
                # add the children to q
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # check for max level sum after the for loop
            if level_sum > max_level_sum:
                result = level
                max_level_sum = level_sum

        return result


# DFS - recursive - time:O(n), space:O(n)
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node, level, sum_of_nodes_at_level):
            if not node:
                return

            if len(sum_of_nodes_at_level) == level:
                sum_of_nodes_at_level.append(node.val)

            else:
                sum_of_nodes_at_level[level] += node.val

            # call dfs on next level
            if node.left:
                dfs(node.left, level+1, sum_of_nodes_at_level)
            if node.right:
                dfs(node.right, level+1, sum_of_nodes_at_level)



        if not root:
            return 0            

        sum_of_nodes_at_level = []
        dfs(root, 0, sum_of_nodes_at_level)
        max_sum = float("-inf")
        result_level = 0

        for i in range(len(sum_of_nodes_at_level)):
            if sum_of_nodes_at_level[i] > max_sum:
                max_sum = sum_of_nodes_at_level[i]
                result_level = i+1

        return result_level
