# https://leetcode.com/problems/crawler-log-folder/description/

# time:O(n), space:O(1)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder = 0
        for log in logs:
            if log == "./":
                pass
            elif log == "../":
                if folder == 0:
                    pass
                else:
                    folder -= 1
            else:
                folder += 1 
        return abs(folder)


# using stack
# time:O(n), space:O(n)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if log == "./":
                pass
            elif log == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(log)
        return len(stack)
