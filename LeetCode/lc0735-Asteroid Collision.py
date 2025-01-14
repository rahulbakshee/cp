# time:O(n), space:O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid <0 and stack[-1] > 0:
                if stack[-1] == -asteroid:
                    stack.pop()
                    break
                elif stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] > -asteroid:
                    break
            else:
                stack.append(asteroid)

        return stack
