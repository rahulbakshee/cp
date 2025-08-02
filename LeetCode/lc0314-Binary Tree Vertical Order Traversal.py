# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time:O(n), space:O(n)
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        min_col, max_col = 0,0
        q = deque([(root, 0)])
        hashmap = defaultdict(list)

        while q:
            node, col = q.popleft()
            hashmap[col].append(node.val)

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))

            
        result = []
        for i in range(min_col, max_col+1):
            result.append(hashmap[i])

        return result
