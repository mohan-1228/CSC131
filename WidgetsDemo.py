# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:06:42 2019

@author: ram0
"""

from tkinter import *
class WidgetsDemo:
    def __init__(self):
        
        window=Tk()
        window.title("Widgets Demo")
        frame1=Frame(window) # add a frame to a window
        frame1.pack()
        self.v1=IntVar()
        cbtBold=Checkbutton(frame1,text="Bold",variable=self.v1,command=self.processCheckbutton)
        self.v2=IntVar()
        rbRed=Radiobutton(frame1,text="Red",bg="red",variable=self.v2,value=1,command=self.processRadiobutton)
        rbYellow=Radiobutton(frame1,text="Yellow", bg="yellow", variable=self.v2, value=2,command=self.processRadiobutton)
        cbtBold.grid(row=1,column=1)
        rbRed.grid(row=1,column=2)
        rbYellow.grid(row=1,column=3)
        
        frame2=Frame(window)
        frame2.pack()
        label=Label(frame2,text="Enter your Name: ")
        self.name=StringVar()
        entryName=Entry(frame2,textvariable=self.name) # create an entry box
        btGetName=Button(frame2, text="Get Name",command=self.processButton)
        message=Message(frame2,text="It is a Widgets Demo")
        label.grid(row=1,column=1)
        entryName.grid(row=1,column=2)
        btGetName.grid(row=1,column=3)
        message.grid(row=1,column=4)
        
        # Add text
        text=Text(window)
        text.pack()
        text.insert(END,"Tip\nThe best way to learn Tkinter is to read")
        text.insert(END,"\nthese examples and use them ")
        text.insert(END,"\nto create your own applications")
        
        window.mainloop() # get an event loop started
    
    def processCheckbutton(self):
        print("check button is "+("checked " if self.v1.get()==1 else "unchecked"))
    
    def processRadiobutton(self):
        print("Red" if self.v2.get()==1 else "Yellow")
        
    def processButton(self):
        print("Your name is "+self.name.get())
        
WidgetsDemo() # create the Gui
    