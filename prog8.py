
from tkinter import *
from  tkinter.messagebox import * 
class BMI:

    def __init__(self):
        
        self.window = Tk() 
        self.window.title("BMI Calculator")
        self.window.geometry("640x220") 

        self.nameFrame = Frame(self.window)
        self.ageFrame = Frame(self.window)
        self.heightFrame = Frame(self.window)
        self.weightFrame = Frame(self.window)
        self.bmiFrame = Frame(self.window)
        self.statusFrame = Frame(self.window)
        self.ansFrame = Frame(self.window)
        self.butFrame = Frame(self.window)

        
        #creating a label and entry field for name

        self.namelabel = Label(self.nameFrame, text="Name")
        self.nameEntry = Entry(self.nameFrame, width = 10)
        self.namelabel.pack(side = 'left')
        self.nameEntry.pack(side = 'left')


        #creating a label and entry field for age

        self.agelabel = Label(self.ageFrame, text="Age")
        self.ageEntry = Entry(self.ageFrame, width = 10)
        self.agelabel.pack(side = 'left')
        self.ageEntry.pack(side = 'left')

       

        # creating a label and entry field for height
        
        self.heightlabel = Label(self.heightFrame, text="Height")
        self.heightEntry = Entry(self.heightFrame, width = 10)
        self.heightlabel.pack(side = 'left')
        self.heightEntry.pack(side = 'left')

        # creating a label and entry field for weight
        
        self.weightlabel = Label(self.weightFrame, text = "Weight")
        self.weightEntry = Entry(self.weightFrame, width = 10)
        self.weightlabel.pack(side = 'left')
        self.weightEntry.pack(side = 'left')

        # creating a label and entry field for displyaing BMI
        
        self.bmilabel = Label(self.bmiFrame, text = "BMI")
        self.bmiEntry = Entry(self.bmiFrame, width = 10)
        self.bmilabel.pack(side = 'left')
        self.bmiEntry.pack(side = 'left')


        # creating a label and entry field for displyaing Status


        self.statuslabel = Label(self.statusFrame, text = "Status")
        self.statusEntry = Entry(self.statusFrame, width = 10)
        self.statuslabel.pack(side = 'left')
        self.statusEntry.pack(side = 'left')
        
        # calling CalcBMI() upon clicking 'calculate BMI' button
        self.calcBut = Button(self.butFrame, text = 'Calculate BMI', command = self.CalcBMI ) 
        
        # To terminate the program when user clicks on 'Quit'
        self.quitBut = Button(self.butFrame, text = 'Quit', command = self.window.destroy ) 
        
        self.calcBut.pack(side='left',padx='20')
        self.quitBut.pack(side='right',padx='20')

        self.nameFrame.pack()
        self.ageFrame.pack()
        self.heightFrame.pack()
        self.weightFrame.pack()
        self.bmiFrame.pack()
        self.statusFrame.pack()
        self.ansFrame.pack()
        self.butFrame.pack()
        mainloop() # starting the application

    def CalcBMI(self):

       
        try:
            self.height = float(self.heightEntry.get())
            self.weight = float(self.weightEntry.get())

       
            
            self.bmi = (self.weight * 703 )/(self.height*self.height)
            if self.bmi < 18.5:
                self.status = (" Underweight")
            elif self.bmi >= 18.5 and self.bmi <= 24.9:
                self.status = (" Normal")
            elif self.bmi >= 25.0 and self.bmi <= 29.9:
                self.status = (" Overweight")
            elif self.bmi >=30:
                self.status = (" Obese")
       
            self.bmiEntry.insert(INSERT,str(round(self.weight* 703/(self.height*self.height),2))) 
            self.statusEntry.insert(INSERT,str(self.status)) 
            

        except:
            showerror(message="Error: Bad Format", parent = self)
                
    
                    


    
       

      

bmi = BMI() 
