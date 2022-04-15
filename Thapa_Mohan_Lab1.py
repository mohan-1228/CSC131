"""
Name : Mohan Thapa
CSC 131 lab 004
"""

def sumColumn(matrix,columnindex):
    numRows = len(matrix)
    
    total = 0 

    for i in range(numRows):

        total = total + matrix[i][columnindex]

        
    return total

def display(m):
    for row  in m:
        for value in row:
            print(value,end=" ") 
        print()


def getMatrix(numRows, numColumns):
    '''returns a matrix with the specified number of rows and columns'''
    m = [] # the 2D list (i.e., matrix), initially empty
    for row in range(numRows):
        matrix_dimensions_string = str(numRows) + "-by-" + str(numColumns)
        line = input("Enter a " + matrix_dimensions_string + " matrix row for row " + str(row) + ": ")
        line = line.split(" ")
        row = []
        for i in line :
            row.append (float(i))
        m.append(row)
        
    
        
    return m


def main():
    m = getMatrix(3, 4)
    print("\nThe matrix is")
    display(m)

    print()
    for col in range(len(m[0])):
        print("Sum of elements for column %d is %.2f" % (col, sumColumn(m,col)))          

main()
     

	
