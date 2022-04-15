
import random
def value (matrix):
    for rowindex in range (len(matrix)):
        for columnindex in range (len(matrix[row])):
            matrix[rowindex][columnindex]= random.randit(1,100)
def display (matrix):
    for row in matrix:
        for value in row:
            print(value, end = " ")
        print()

def main():
    row = 10 
    column = 10
    m =[]
    for row in range (rows):
        m.append ([0]* column )
    
    display (m)
    value(m)
    print("list of random numbers")
    display (m)

main()
