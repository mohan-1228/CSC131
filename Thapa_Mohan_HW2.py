"""
Name : Mohan Thapa
CSC 131 HW 2
"""





#function to read the text file from the directory
def open_file():       
    fd = open("input.txt","r")
    lst=[]
    for line in fd:
        line = line.strip().split(" ")
        L= list(map(lambda x: int(x), line))
        lst.append(L) # creates the list of numbers in board game.
        
    return lst
        
      
def toJump(L):#function to check for the basic case and recursive case.
  if len(L)==1:
    return L[0]
  if len(L)==2:
    return L[0] +L[1]
  if len(L)==3:
    return L[0] + L[2]

  jump_cost = L[0] + toJump(L[2:])#calculates the cost to jump.
  adjacent_cost = L[0] +toJump(L[1:])#calculte the cost to move to adjacent side.

  return min(jump_cost,adjacent_cost)# returns mimimum cost among given parameters


def main():#main function to call the function
    for i in open_file():
      print(toJump(i))
    
    

main() #calls the main function.


