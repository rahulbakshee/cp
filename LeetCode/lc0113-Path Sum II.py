# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive DFS - time:O(n^2), space:O(n)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, node_list, node_sum):
            # base case
            if not node:
                return 
            
            # update node list and node value
            node_list.append(node.val)
            node_sum += node.val

            # check if the leaf node
            if not node.left and not node.right and node_sum == targetSum:
                result.append(node_list.copy())

            # if not leaf, keep on going to the child/next level
            if node.left:
                dfs(node.left, node_list, node_sum)
            if node.right:
                dfs(node.right, node_list, node_sum)

            # remove the just added node from the current solution
            node_list.pop()
        
        if not root:
            return []

        result = []
        dfs(root, [], 0)
        return result


# iterative using stack - time:O(n^2), space:O(n)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == targetSum:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res

# https://leetcode.com/problems/path-sum-ii/solutions/36829/python-solutions-recursively-bfs-queue-dfs-stack/
