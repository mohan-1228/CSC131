"""
Name : Mohan Thapa
CSC 131 lab 7
"""

from tkinter import *
from  tkinter.messagebox import *
class Temprtature (Frame):
    def __init__ (self):
        Frame.__init__(self)
        self.master.title(" Temperature Conversion")
        self.grid()


    # creating the label and entry  field for  for fahrenheit
        self.fahrenheitlabel = Label(self, text="Fahrenheit", width = 15)
        self.fahrenheitlabel.grid(row = 0, column = 0 )
        self.fahrenheitVar = DoubleVar()
        self.fahrenheitVar.set(32.0)
        self.fahrenheitEntry = Entry(self, textvariable = self.fahrenheitVar,width = 15)
        self.fahrenheitEntry.grid(row = 1, column = 0 )




    # creating the label and entry  field for  for celsius
        self.celsiuslabel = Label(self, text="Celsius",width = 15)
        self.celsiuslabel.grid(row = 0, column = 1)
        self.celsiusVar = DoubleVar()
        self.celsiusEntry = Entry(self, textvariable = self.celsiusVar,width = 15)
        self.celsiusEntry.grid(row = 1, column = 1)



    #The Command Button
        self._button = Button(self, text = "Convert from Fahrenheit", command = self.to_celsius)
        self._button.grid(row = 2, column = 0 , columnspan = 1 )


        self._button = Button(self, text = "Convert from Celsius", command = self.to_fahrenheit)
        self._button.grid(row = 2, column = 1 , columnspan = 1 )





    
    def to_celsius(self):
        f = self.fahrenheitVar.get()
        c = (f - 32) * (5/9)
        self.celsiusVar.set(c)

    def to_fahrenheit(self):
        c = self.celsiusVar.get()
        f = c * (9/5) + 32
        self.fahrenheitVar.set(f)

    


def main():
    Temprtature().mainloop()
main()