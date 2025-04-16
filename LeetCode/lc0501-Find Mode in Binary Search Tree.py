# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive DFS
# time:O(n), space:O(n) - n - number of nodes in tree
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node):
            if node.left:
                helper(node.left)

            counter[node.val] += 1

            if node.right:
                helper(node.right)
        
        counter = defaultdict(int)

        if not root:
            return []
        
        helper(root)

        # print(counter)
        
        result = []
        max_freq = max(counter.values())
        for key, value in counter.items():
            if value == max_freq:
                result.append(key)

        return result


# iterative - DFS - stack
# time:O(n), space:O(n)
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        counter = defaultdict(int)
        result = []

        stack = [root]
        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)

            counter[node.val] += 1

            if node.right:
                stack.append(node.right)

        
        max_value = max(counter.values())

        for key, value in counter.items():
            if value == max_value:
                result.append(key)

        return result   



# iterative - BFS - queue
# time:O(n), space:O(n)

from collections import deque
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        counter = defaultdict(int)
        result = []

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)
            
            counter[node.val] += 1

            if node.right:
                q.append(node.right)
            
        max_value = max(counter.values())

        for key, value in counter.items():
            if value == max_value:
                result.append(key)

        return result   
