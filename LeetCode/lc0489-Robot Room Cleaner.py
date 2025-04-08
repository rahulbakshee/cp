# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        def backtrack(r,c,d):
            visited.add((r,c))
            robot.clean()

            # explore neighbors
            for i in range(4):
                new_d = (d+i) %4
                new_r = r+directions[new_d][0]
                new_c = c+directions[new_d][1]

                # check for visited, 
                if (new_r,new_c) not in visited and robot.move():
                    backtrack(new_r,new_c,new_d)

                    # go back
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()

                # turn right
                robot.turnRight()


        visited = set()
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        backtrack(0,0,0) # x,y,d






















