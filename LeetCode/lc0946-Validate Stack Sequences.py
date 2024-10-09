# time:O(n), space:O(n)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0

        for num in pushed:
            stack.append(num)

            while stack and popped[index] == stack[-1]:
                stack.pop()
                index += 1

        return len(stack) == 0
