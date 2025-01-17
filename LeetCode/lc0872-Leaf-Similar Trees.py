# time:O(n+m), space:O(n+m)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def collectLeaves(node, result):
            if not node.left and not node.right:
                result.append(node.val)
                return result

            if node.left:
                collectLeaves(node.left, result)
            if node.right:
                collectLeaves(node.right, result)

            return result

        result1 = collectLeaves(root1, [])
        result2 = collectLeaves(root2, [])

        return result1 == result2
