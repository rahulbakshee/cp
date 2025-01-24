# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time:O(n), space:O(n)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum)->None:
            nonlocal result
            
            # base case
            if not node:
                return 

            # update current sum with current node val
            curr_sum += node.val

            if curr_sum == k:
                result += 1

            result += hashmap[curr_sum - k]
            hashmap[curr_sum] += 1

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            hashmap[curr_sum] -= 1


        if not root:
            return 0

        result = 0
        k = targetSum
        hashmap = defaultdict(int)
        dfs(root, 0)
        return result
