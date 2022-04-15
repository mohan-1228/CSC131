 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 23:12:00 2021

@author: mohanthapa
"""

from tkinter import *
from tkinter import messagebox

class BMI() :
#constructor for employee
    master = Tk();
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
  
  
def __init__(self):
    self.make_widgets();

#CLEAR FORM INPUT
def clear(self):
    self.e3.delete(0,END)
    self.e1.delete(0,END)
    self.e2.delete(0,END)
    self.e2.insert(0,"")
    self.e1.insert(0,"")
  
  
#COMPUTE THE bmi
def compute(self):
    number1 = 0;
    number2 = 0;
try :
    number1 = float(self.e1.get());
    number2 = float(self.e2.get());
    self.e3.delete(0,END)
    result = str(number2/(number1*number1)*703); #Imperial BMI Formula
    messagebox.showinfo("Calculated BMI", result)
    self.clear();
except:
    messagebox.showinfo("Error", "Error in calculating BMI")

  
#ADD WIDGETS TO THE FORM
def make_widgets(self):
#add label using grid layout
    Label(self.master, text="Enter your height : ").grid(row=0, column=0)
    Label(self.master, text="Enter your weight : ").grid(row=1, column=0)

    self.e1.grid(row=0, column=1,)
    self.e2.grid(row=1, column=1)
    Button(self.master, text='Calculate BMI',command=self.compute).grid(row=2, column=1, sticky=W, pady=4)
    mainloop( )
  
  
  
#CALLING CLASS FOR MAIN
bmi = BMI();