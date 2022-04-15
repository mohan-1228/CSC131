from  tkinter import *
from tkinter.messagebox import * 
class BMI:

    def __init__(self):
        
        self.window = Tk() # creating the main window
        self.window.title("BMI Calculator") # setting window title
        self.window.geometry("640x220") # setting window dimensions

        self.nameFrame = Frame(self.window)
        self.ageFrame = Frame(self.window)
        self.heightFrame = Frame(self.window)
        self.weightFrame = Frame(self.window)
        self.bmiFrame = Frame(self.window)
        self.ansFrame = Frame(self.window)
        self.butFrame = Frame(self.window)

       # creating a label and entry field for name
     
        self.namelabel = Label(self.nameFrame, text= "Name ").grid (row = 0, column = 0)
        self.nameEntry = Entry(self.nameFrame, width = 8).grid (row = 0, column = 1)
        
        


      # creating a label and entry field for age

        self.agelabel = Label(self.ageFrame, text= " Age").grid (row = 1, column = 0)
        self.ageEntry = Entry(self.ageFrame, width = 5).grid (row = 1 ,column = 1)
       

        # creating a label and entry field for height
        
        self.heightlabel = Label(self.heightFrame, text="Height in inches ").grid (row = 2,column = 0)
        self.heightEntry = Entry(self.heightFrame, width = 5).grid (row = 2,column = 1)
        #self.heightEntry.pack(side = 'left')


        # creating a label and entry field for weight
        
        self.weightlabel = Label(self.weightFrame, text = "Weight in pounds ").grid (row = 3,column = 0)
        self.weightEntry = Entry(self.weightFrame, width = 5).grid (row = 3,column = 1)
        #self.weightEntry.pack(side = 'left')


        # creating a label and entry field for displyaing BMI
        
        self.bmilabel = Label(self.bmiFrame, text = "BMI").grid (row = 4,column = 0)
        self.bmiEntry = Entry(self.bmiFrame, width = 5).grid (row = 4,column = 1)
        
        
        # calling CalcBMI() upon clicking 'calculate BMI' button
        self.calcBut = Button(self.butFrame, text = 'Calculate BMI', command = self.CalcBMI).grid(row = 6,column = 1) 

        # To terminate the program when user clicks on 'Quit'
        self.quitBut = Button(self.butFrame, text = 'Quit', command = self.window.destroy).grid(row= 6, column = 4) 
        
        
        

        self.nameFrame.pack()
        self.ageFrame.pack()
        self.heightFrame.pack()
        self.weightFrame.pack()
        self.bmiFrame.pack()
        self.ansFrame.pack()
        self.butFrame.pack()
        mainloop() # starting the application

    def CalcBMI(self):

        # Get values for height and weight

        self.height = float(self.heightEntry.get())
        self.weight = float(self.weightEntry.get())

        # convert inches to meters
        self.height = self.height*0.0254

        # convert pounds to Kilograms
        self.weight  = self.weight*0.4535
        
        # calculate BMI as weight in KGs / height*height in metres
        self.bmiEntry.insert(INSERT,str(round(self.weight/(self.height*self.height),2)))  

bmi = BMI() # initializing class object and thus calling init
