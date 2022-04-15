#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 23:38:55 2021

@author: mohanthapa
"""

def sumDigits(n):
    
    
    sum = 0
    for digit in str(n):
        sum = sum + int(digit)
    return sum





def convertMillis(millis):
    seconds =(int(millis/1000)%60)
    minutes =(int(millis/(1000*60))%60)
    hours = (int(millis/(1000*60*60))%24)
    convert = (f"{hours}:{minutes}:{seconds}")
    
    
    return(convert)





def isValid(side1,side2,side3):
    if side1 + side2 > side3:
        return True 
    else:
        return False 
    
    
    

    
    


def myPi(i):
    a = 0
    b = i
    i =1
    

    for n in range(b):
       a = a + ((-1)**(i+1))/(2*i-1)
       i = i + 1
    a = a * 4
    total = round(a, 4)
    return(total)

    
    
    
    
def BMI(w,h):
    weight = (w * 0.45)
    height = (h * 0.02)
    BMI = weight/(height**2)
    if BMI<18.5:
        return("Underweight")
    elif BMI >= 18.5 or BMI <=24.9:
        return("Normal")
    elif BMI >= 25.0 or BMI <= 29.9:
        return("Overweight")
    elif BMI >=30:
        return("Obese")
        
    return(BMI)
    
    
    
    
    
    
import sys
 
def test(did_pass):
    """ Print the result of a test """
    linenum=sys._getframe(1).f_lineno
    if did_pass:
        msg="Test at line {0} ok.".format(linenum)
    else:
        msg="Test at line {0} failed.".format(linenum)
 
    print(msg)
   
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(sumDigits(142) == 7)
    test(isValid(1,3,1) == True)
    test(convertMillis(100000) == "0:1:40")
    test(myPi(101) == 3.1515)
    test(BMI(146,70) == "Normal")
 
test_suite()        # Here is the call to run the tests    
