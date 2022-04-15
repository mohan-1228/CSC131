"""
Name : Mohan Thapa
CSC 131 Lab 5
"""





class Point():


    COUNT = 0 


    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
        Point.COUNT += 1

    def __str__(self):
        return "(%s,%s)"%(self.x,self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self,x):
        self.x = x
    
    def setY(self,y):
        self.y = y


    def distanceFromPoint( self,aPoint):
        dx = self.x - aPoint.x
        dy = self.y - aPoint.y
        d = ((dx)**2 + (dy)**2)**0.5
        return d


    def distanceFromOrigin(aPoint):
        d = ((aPoint.x)**2 + (aPoint.y)**2)**0.5
        return d 



    def __lt__(self,aPoint):
        if self.distanceFromOrigin()<aPoint.distanceFromOrigin():
            return True
        else:
            return False 

    def __le__(self,aPoint):
        if self.distanceFromOrigin()<=aPoint.distanceFromOrigin():
            return True 
        else:
            return False 

    def __gt__(self,aPoint):
        if self.distanceFromOrigin()>aPoint.distanceFromOrigin():
            return True 
        else:
            return False

    def __ge__(self,aPoint):
        if self.distanceFromOrigin()>=aPoint.distanceFromOrigin():
            return True 
        else:
            return False


    def __eq__(self,aPoint):
        if type(self) == type(aPoint) and self.distanceFromOrigin()==aPoint.distanceFromOrigin():
            return True 
        else:
            return False


    def __ne__(self,aPoint):
        return not self == aPoint



def main():
    p1 = Point(3,4)
    print (p1)
    p2 = Point(3,0)
    print(p2.getX(),p2.getY())
    print("The distance between", p1, "and",p2,"is: ", p1.distanceFromPoint(p2))
    print("Testing the comparison operators in the order <, <=, >, >=, ==, != ")
    print("p1 < p2 ?",p1 < p2)
    print("p1 <= p2 ?",p1 <= p2)
    print("p1 > p2 ?",p1 >p2)
    print("p1 >= p2 ?",p1 >= p2)
    print("p1 == p2 ?",p1 == p2)
    print("p1 != p2 ?",p1 != p2)
    print("p1 == \"Hello?\"",p1 == "Hello")
    print("p1 != \"Hello\"?",p1 != "Hello")
    print("Number of point objects created is",Point.COUNT)

main()


