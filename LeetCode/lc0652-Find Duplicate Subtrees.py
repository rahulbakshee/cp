# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def dfs(node):
            # base case
            if not node:
                return "N"
            
            # traverse the left and right child in preorder [root, left, right]
            key = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            if len(hashmap[key]) == 1:
                result.append(node)
            hashmap[key].append(node)          
            
            return key
            
        hashmap = defaultdict(list)
        
        result = []
        dfs(root)
        return result
