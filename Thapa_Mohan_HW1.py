"""
Name : Mohan Thapa
CSC 131 HW 1
"""
def checkRepetation(l):      #checking reperation of  numbers in matrix.
    for a in range(len(l)):
        for b in range(a+1,len(l)):
            if l[a]==l[b]:
                return True
    return False

def open_file():       #opening and reading the text file.
    fd = open("magic.txt","r")
    for line in fd:
        line = line.split()
        row = list(map(lambda x: int(x), line))
        if checkRepetation(row):   
            print("invalid")
            continue
        r1 = row[0:3]
        r2 = row [3:6]
        r3 = row[6:9]
        m =[r1,r2,r3]   # creating 3x3 matrix from the line of text file.
        
            
        print("valid") if sumColumn(m) and sumrow(m) else print("invalid")   # printing the reasult.
    fd.close()





def sumrow(m):         #calculating the sum of  each rows  
    for a in m:
        if sum(a)!=15:
            if m[0][0] + m[1][1] + m[2][2] != 15:  #checking sum of major diagonal.
                if m[0][2] + m[1][1] + m[2][0] != 15: #checking sum of minor diagonal
                 return False
    return True


def sumColumn(m):      # calculating the sum of  each column.
    row = len(m)
    for i in range(len(m[0])):
        total = 0
        for j in range(row):
            total = total + m[j][i]
        if total != 15:           #checking  sum of each colum is 15 r not
            return False
    return True



def main():             #main functon 
    open_file()
   
    
main()
    





    

       
