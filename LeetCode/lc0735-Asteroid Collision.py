"""(Stack Simulation)
Use a stack to simulate asteroid movement and collision.
Push asteroids moving right (> 0) onto the stack.
When a left-moving asteroid (< 0) comes in, check for collisions with 
the stack’s top (which will be a right-moving asteroid)."""
# Overall cases
# 1- both moving same direction(positive, positive) - No collision
# 2- both moving same direction(negative, negative) - NO collision
# 3- both moving in opposite direction
    # 3.1- prev is positive, upcoming is negative - YES collision
    # 3.2- prev is negative, upcoming is positive - NO collision"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # This stores the current surviving asteroids

        for ast in asteroids:
            # While there is a possibility of collision:
            # current asteroid is moving left (negative) AND top of stack is moving right (positive)
            while stack and ast < 0 and stack[-1] > 0:
                if abs(ast) > abs(stack[-1]):
                    # Incoming asteroid is bigger, destroy the one on the stack and continue checking
                    stack.pop()
                    continue
                elif abs(ast) == abs(stack[-1]):
                    # Both are equal, both get destroyed
                    stack.pop()
                # In both above cases, current asteroid does not get added
                break
            else:
                # No collision, so just add asteroid to the stack
                stack.append(ast)

        return stack
