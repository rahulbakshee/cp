# https://leetcode.com/problems/walking-robot-simulation/solutions/5734055/simple-and-easy-solution-using-java-and-python-with-explanation/
# time:O(n+m), space:O(m) - m is the obstacles

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        directions_all = [(0,1), (1,0), (0,-1), (-1,0)]
        #                   N      E      S       W
        direction = 0
        x, y = 0,0
        max_distance = 0

        for command in commands:
            if command == -2: # Turn left 90 degrees.
                direction = (direction-1) %4

            elif command == -1: # Turn right 90 degrees.
                direction = (direction+1) %4
            
            else: # move by k in direction
                for _ in range(command):
                    nx = x + directions_all[direction][0]
                    ny = y + directions_all[direction][1]
                    # if obstacle
                    if (nx,ny) in obstacles:
                        break
                    x, y = nx, ny
                    max_distance = max(max_distance, x**2 + y**2) 

        return max_distance
