
# 1 - BFS - reverse the order depending on level before appending to final result
# Definition for a binary tree node.
# time:O(n), space:O(n) - n is total nodes in tree
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        q = deque([root])
        zigzag = False

        while q:
            
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            
            if zigzag:
                result.append(level)
            else:
                result.append(level[::-1])

            # change the zigzag pattern
            zigzag = not zigzag

        return result


# BFS - pop from left and pop from right for zigzag pattern
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        q = deque([root])
        zigzag = False

        while q:
            
            level = []
            for _ in range(len(q)):
        
                if zigzag:
                    node = q.pop()
                    level.append(node.val)

                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)

                else:
                    node = q.popleft()
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            # change the zigzag pattern
            zigzag = not zigzag

            result.append(level)


        return result
