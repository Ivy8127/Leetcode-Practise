class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType: int) -> bool:
        match carType:
            case 1:
                self.big -=1
                return self.big >= 0
            case 2:
                self.medium -=1
                return self.medium >= 0
            case 3:
                self.small -=1
                return self.small >= 0
            case _:
                return "Invalid car Type"
            
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)