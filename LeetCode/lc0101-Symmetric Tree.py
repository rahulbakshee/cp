# recrursion
# time:O(n), space:O(n) for callstack
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def helper(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (left.val == right.val) and helper(left.left, right.right) and helper(left.right, right.left)

        
        # call helper
        return helper(root.left, root.right)


# iterative
# time:O(n), space:O(n) for queue
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque()
        q.append((root.left, root.right))

        while q:
            left, right = q.pop()

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            q.append((left.left, right.right))
            q.append((left.right, right.left))

        return True
