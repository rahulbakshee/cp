# DFS
# time:O(n), space:O(n) 
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        hasParent = set(leftChild+ rightChild)
        hasParent.discard(-1)

        # check if root node present or not
        if len(hasParent) == n:
            return False

        # find the root
        root = -1
        for i in range(n):
            if i not in hasParent:
                root = i
                break

           
        # perform DFS to traverse the tree
        # check if cycle or not using visited
        visited = set()
        def dfs(i):
            # base case
            if i == -1:
                return True
            
            if i in visited:
                return False

            visited.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])


        return dfs(root) and len(visited) == n
