"""
Name : Mohan Thapa
CSC 131 lab 3
"""




def main():
    print(stutter("abc"))
    print(toNumber("ab3c7d1"))
    print(findMax([1,2,3,4,5,6]))
    print(findAverage([3,4,5,6,7,8]))
    



  
# a recursive function called stutter(aString) that returns a string with each character in its argument repeated.
def stutter(aString):
     if aString == "":
        return aString
     else:
        return aString[0]*2 + stutter(aString[1:])
        


#a recursive function called toNumber(aString) that returns the integer sum of all digit characters in a string.
def toNumber(aString):
    if aString == "":
        return 0
    elif aString[0].isdigit():
        return int(aString[0]) + toNumber(aString[1:])
    else:
        return toNumber(aString[1:])


#a recursive function called findMax(aList) that takes a list of numbers as an argument and returns the max value of all the values in the list.
def findMax(aList):
    if len(aList) <= 1:
        return aList[0]
    else:
        m = findMax(aList[1:])
        return m if m > aList[0] else aList[0]


#a recursive function called findAverage(aList) that takes a list of numbers as an argument and returns the average of the values in the list. 
def findAverage(aList):
    if len(aList)== 0:
        return 0
    else:
        
        
        return  (int(aList[0]) + findAverage(aList[1:])* (len(aList)-1)) / (len(aList))
        
        
    
    

        


main()