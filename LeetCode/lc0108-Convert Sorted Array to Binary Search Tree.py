# time:O(n), space:O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(left, right):
            if left > right:
                return

            mid = (left+right)//2
            root = TreeNode(nums[mid])

            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)

            return root

        if not nums:
            return
        
        return helper(0, len(nums)-1)




# NOT EFFICIENT because I am passing entire array to function, but still runs
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(nodes):
            if not nodes:
                return
            
            n = len(nodes)

            root = TreeNode(nodes[n//2])
            root.left = dfs(nodes[:n//2])
            root.right = dfs(nodes[n//2+1:])

            return root

        return dfs(nums)

