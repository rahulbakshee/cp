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


# ABOVE AND BELOW ARE SAME

# time:O(nlogn), space:O(n) - NEETCODE
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # reverse sorted
        pair = sorted([[position[i], speed[i]] for i in range(len(position))])[::-1]

        stack = []

        for p,s in pair:
            stack.append((target-p)/s)
            # collision - we start with greatest position car and then second greatest  
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

