

class BMI ():
    def __init__(self, name = "", age = 0, w = 0.0, h = 0.0 ):
        self.__Name = name
        self.__Age = age
        self.__Weight = w
        self.__Height = h
        
        
   
    def get_Name(self):
        return self.__Name
    def get_Age(self):
        return self.__Age
    def get_Weight(self):
        return self.__Weight 
    def get_Height(self):
        return self.__Height
    
    def get_BMI (self):
        ans = (self.__Weight * 703)/(self.__Height * self.__Height)
        return  round(ans,1)

    
        
    
        
    def get_Status(self):
        BMI = self.get_BMI()
        if BMI<18.5:
            Status = ("Underweight")
        elif BMI >= 18.5 and BMI <= 24.9:
            Status = ("Normal")
        elif BMI >= 25.0 and BMI <= 29.9:
            Status = ("Overweight")
        elif BMI >=30:
            Status =("Obese")
        return Status
   
 
def main():
    bmi1=BMI("John Doe",18,145,70)
    print("The BMI for ",bmi1.get_Name(), " is ",bmi1.get_BMI(),bmi1.get_Status())
    bmi2=BMI("Sue Doe",19,103,68)
    print("The BMI for ",bmi2.get_Name(), " is ",bmi2.get_BMI(),bmi2.get_Status())
    bmi3=BMI("Pete Doe",50,217,70)
    print("The BMI for ",bmi3.get_Name(), " is ",bmi3.get_BMI(),bmi3.get_Status())
 
main()

        