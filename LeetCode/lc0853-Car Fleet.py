# time:O(nlogn) for sorting, space:O(sorting + O(n))
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_sp = [[pos, sp] for pos, sp in zip(position, speed)]
        pos_sp = sorted(pos_sp, reverse=True, key=lambda x: x[0])

        for i in range(len(pos_sp)):
            stack.append(pos_sp[i])
            if len(stack) >= 2 and (((target-stack[-1][0])/stack[-1][1]) <= (target-stack[-2][0])/stack[-2][1]):
                stack.pop()
            
        return len(stack)
