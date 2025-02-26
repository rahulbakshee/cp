class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []
        # prev = stack[-1]
        
        # Overall cases
        # 1- both moving same direction(positive, positive) - No collision
        # 2- both moving same direction(negative, negative) - NO collision
        # 3- both moving in opposite direction
            # 3.1- prev is positive, upcoming is negative - YES collision
            # 3.2- prev is negative, upcoming is positive - NO collision

        # stack = [1,2,3] , asteroid = -4
        # result = [-4]

        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
                continue

            # there is something ins stack
            # compare on conditions
            # 3.1
            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] > -1*ast:
                    break
                elif stack[-1] < -1*ast:
                    stack.pop()
                    continue
                else:
                    stack.pop()
                    break
            # 1,2,3.2
            else:
                stack.append(ast)


        return stack






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
