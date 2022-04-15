"""
Name : Mohan Thapa
CSC 131 HW 3
"""



import math 
class Complex():
    
      def __init__(self, a = 0.0, b = 0.0 ):
          self.__realpart = a
          self.__impart = b

      def __str__(self):
        if (self.__impart==0 and self.__realpart==0):
            return "0"

        if(self.__realpart==0):
            return str(self.__impart)+"i"
        if(self.__impart ==0):
            return str(self.__realpart)
        else:
            return "(%s,%s)"%(str(self.__realpart),str(self.__impart)+"i" )
          
      def get_realpart(self):
          return self.__realpart
      def get_imaginarypart(self):
          return self.__impart
      
        
      def set_realpart(self,a):
          self.__realpart = a
          
      def set_imaginarypart(self,b):
          self.__impart = b
          
          
      def __add__(self,c):
          temp = Complex()
          temp.__realpart = self.__realpart + c.__realpart
          temp.__impart = self.__impart + c.__impart
          return temp
      
        
      def __sub__(self,c):
           temp = Complex()
           temp.__realpart = self.__realpart - c.__realpart
           temp.__impart = self.__impart - c.__impart
           return temp
           
           
      def __mul__(self,c):
          temp = Complex()
          temp.__realpart = self.__realpart * c.__realpart - self.__impart * c.__impart
          temp.__impart = self.__realpart * c.__impart + self.__impart * c.__realpart
          return temp
      
      def __truediv__(self,c):
          temp = Complex()
          temp.__realpart = (self.__realpart * c.__realpart + self.__impart * c.__impart) /(c.__realpart **2 + c.__impart **2)
          temp.__impart =  (self.__impart * c.__realpart - self.__realpart * c.__impart)/(c.__realpart **2 + c.__impart **2)
          return temp  

      def __abs__(self):
        length = math.sqrt((self.__realpart **2) + (self.__impart **2))
        return length


      def __lt__(self,c):
        if self.__abs__()<c.__abs__():
            return True
        else:
            return False 

      def __le__(self,c):
        if self.__abs__()<=c.__abs__():
            return True 
        else:
            return False 

      def __gt__(self,c):
        if self.__abs__()>c.__abs__():
            return True 
        else:
            return False

      def __ge__(self,c):
        if self.__abs__()>=c.__abs__():
            return True 
        else:
            return False


      def __eq__(self,c):
        if  type(self) == type(c) and self.__abs__()==c.__abs__():
            return True 
        else:
            return False


      def __ne__(self,c):
        return not self == c

def main():
    input_line = input("Enter the first complex number: ")
    input_line = list(map(float,input_line.split()))
    a, b = input_line[0], input_line[1]
    c1 = Complex(a, b)
    input_line = input("Enter the second complex number: ")
    input_line = list(map(float,input_line.split()))
    a, b = input_line[0], input_line[1]
    c2 = Complex(a, b)
    
    print()
    print("c1 is", c1)
    print("c2 is", c2)
    print("|" + str(c1) + "| = " + str(abs(c1)))
    print("|" + str(c2) + "| = " + str(abs(c2)))

    print(c1, " + ", c2, " = ", c1 + c2)
    print(c1, " - ", c2, " = ", c1 - c2)
    print(c1, " * ", c2, " = ", c1 * c2)
    print(c1, " / ", c2, " = ", c1 / c2)

    print("Is c1 < c2?", c1 < c2)
    print("Is c1 <= c2?", c1 <= c2)
    print("Is c1 > c2?", c1 > c2)
    print("Is c1 >= c2?", c1 >= c2)
    print("Is c1 == c2?", c1 == c2)
    print("Is c1 != c2?", c1 != c2)
    print("Is c1 == 'Hello There'?", c1 == 'Hello There')
    print("Is c1 != 'Hello There'?", c1 != 'Hello There')
    
main()


            
         
    
    
    
    
