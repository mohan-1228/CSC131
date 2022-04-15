
"""
Name : Mohan Thapa
CSC 131 lab 004
"""
from functools import reduce
def evenFilter(dict):
    
    result = [dict[key] for key in dict if key%2 == 0]
    return result


def findMin(x, y):
    min  =  y if x > y else x  
    return min 

def main():
    '''generates the list '''
    a = list(range(1,11))  

    '''	Using the map and a lambda argument, write an expression that produces a list of the cubes of the values in a'''
    m = list(map(lambda x, : x**3,a))
    print(m)

    '''	Using the filter function and a lambda argument, write an expression that produces a list of the values in a that are divisible by 3'''
    f1 = list(filter( lambda x,: x%3==0, a))
    print(f1)

    '''	Using the reduce function and a lambda argument, write an expression that returns the result of concatenating all of the digits in a'''
    r1 = (reduce(lambda x, y: str(x)+str(y),a ))
    print(r1)
    
    '''	Using a list comprehension to produce a list of the cubes of the values in a'''
    m2 = [x**3 for x in a]
    print(m2)

    '''Using a list comprehension to produce a  list of the values in a that are divisible by 3'''
    f2 = [x for x in a if x%3==0]
    print(f2)

    '''Using a list comprehension to produce a list containing the cubes of the values in a that are divisible by '''
    a6 = [x**3 for x in a if x%3 ==0 ]
    print(a6)


   
    
    dict = {1: "one", 3: "three", 4: "four", 5: "five", 8: "eight", 10: "ten"}
    evenFilter(dict)
    print(evenFilter(dict))
    findMin(10, 20)
    print(findMin(90,20))
    






main()




