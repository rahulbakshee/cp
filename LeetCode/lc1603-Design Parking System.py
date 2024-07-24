# time:O(1), space:O(1)
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

class ParkingSystem:
    def __init__(self, big:int, medium:int, small:int):
        self.big = big
        self.medium  = medium
        self.small = small

    def addCar(self, carType:int)->bool:
        """ Checks whether there is a parking space of carType 
        for the car that wants to get into the parking lot.
        """
        if carType == 1: #big
            if self.big -1 >= 0:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2: #medium
            if self.medium -1 >= 0:
                self.medium -= 1
                return True
            else:
                return False
        else: #small
            if self.small -1 >= 0:
                self.small -= 1
                return True
            else:
                return False
