# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:47:34 2019

@author: ram0
"""

from tkinter import Button,Tk
class ProcessButtonEvent:
    def __init__(self):
        window=Tk() # create a window
        btOK=Button(window,text="OK", fg="red", command=self.processOK)
        btCancel=Button(window, text="Cancel", bg="yellow",command=self.processCancel)
        btOK.pack() # put OK Button in window
        btCancel.pack() # do the same for the Cancel Button
        window.mainloop() # gets it started
    def processOK(self):
        print("OK Button was pressed")
    def processCancel(self):
        print("Cancel Button was pressed")
ProcessButtonEvent() # Create an object and invoke constructor