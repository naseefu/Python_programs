class vehicle:
    def __int__(self,t,b):
        self.t = t
        self.b = b
    def getspecs(self):
        self.t = input("enter the number of tyres of the vehicle: ")
        self.b = input("what is the vehicle type, battery or Fuel?")
    def display(self):
        print("number of tyres in the vehicle is ",self.t)
        print("vehicle type is ",self.b)
class car(vehicle):
    def __int__(self,s):
        self.s = s
    def seat(self):
        self.s = input("enter the number of doors in the car:")
        print("the car has {} seats".format(self.s))
class bike(vehicle):
    def __int__(self,y):
        self.y = y
    def seata(self):
        self.y = input("what is the type of handle in bike:")
        print("the bike has {} seats".format(self.y))
c = bike()
c.getspecs()
c.display()
c.seata()