"""
Name : Mohan Thapa
CSC 131 lab 004
"""




def getmatrix(rowindex,colindex):
    lst = []
    for row in range (rowindex):
        r = input("Enter {}X{} matrix for row{}:".format (rowindex,colindex ,row))
        s = r.split( " " )
        m = []
        for i in s :
            m.append (float(i))
        lst.append(m)
        m = [] 
    return lst


def display(lst2d):
    for i in lst2d:
        for j in i:
            print(j,end=" ") 
        print()

def sumcolumn (lst2d):
    row_index = len(lst2d)
    col_index = len(lst2d[0])
    total = 0 

    for i in range(col_index):
        for j in range(row_index):
            total = total + lst2d[j][i]

        print("sum of column  {} is {}".format(i,total))
        total = 0 



def main():
    i = getmatrix(3,4)
    display(i)
    print(" ")
    sumcolumn(i) 
main()   
