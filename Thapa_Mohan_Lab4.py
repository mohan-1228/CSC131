"""
Name : Mohan Thapa
CSC 131 Lab 4
"""



class Fan():#defining the class
    def __init__ (self, Radius, On = False, Speed = 1):#constructor for our fan class
        self.Radius = Radius
        self.On = On 
        self.Speed = Speed 

    def __str__(self):#string function to return string representation of output.
        if self.On == False:
          string = "Fan with radius " + str(self.Radius) +"\n Fan is  currently off "
        elif self.On == True:
            string = " Fan with radius " + str(self.Radius)+ "\n Fan is Currently on and is running at the speed " + str(self.Speed)
        return string

    def getRadius(self):#getter method for radius
        return self.Radius

    def getOn(self):#getter method for on.
        return self.On
    
    def getSpeed(self):#getter method for speed
        return self.Speed


   

    def setOn(self,On):#setter method for on 
        if On != True and On != False :
            print("The value "  + str(On) +   " is invalid. Value must be either True or False")
        self.Speed = On


    def setSpeed(self,Speed):#setter method for speed
        if Speed != 1 and Speed != 2 and Speed != 3 :
             print("The value "  + str(Speed) +   " is invalid. Value must be either 1 , 2, or 3")
        self.Speed = Speed


def main():
    fan1 = Fan(5)
    print(fan1)
    
    print()
    fan2 = Fan(12.5, True, 2)
    print(fan2)

    print("\nTesting the accessor methods on fan2")
    print(fan2.getRadius())
    print(fan2.getOn())
    print(fan2.getSpeed())
    

    print("\nTesting the mutator methods on fan2")
    fan2.setOn("off")
    fan2.setOn(False)
    fan2.setSpeed(5)
    fan2.setSpeed(3)

    print()
    print(fan2)

main() #This calls the main function 

    






