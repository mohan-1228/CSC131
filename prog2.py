#Python program to calculate the lifter's handicapped score.
#CSC 130 Fall 2021 Programming Assignment 2.
#Mohan Thapa

# inputs lifter's weight in kilogram
weight =  int(input('Enter a weight for lifter '))

# inputs squat score in kilogram
squat = int(input('Enter a squat score '))
        
#inputs benchpress score in kilogram
benchpress = int(input('Enter a benchpress score '))

#inputs deadlift score in kilogram 
deadlift =int(input('Enter a deadlift score '))


#calculates the handicap in based on lifter's weight

if 40 <= weight <= 125:
    handicap =((6.31926 - 0.262349) * weight ) + ((0.511550e-02) * ( weight ** 2)) - ((0.519738e-04) * (weight ** 3)) + ((0.267626e-06) * (weight ** 4)) - ((0.540132e-09) * (weight ** 5)) - ((0.728875e-13) *  (weight **6))
elif 125 < weight <= 135:
    handicap = ((0.5208 - 0.0012) * ( weight - 125 ))
elif 135 < weight <= 145:
    handicap = ((0.5088 - 0.0011) * ( weight - 135 ))
elif 145 < weight <= 155:
    handicap = ((0.4978 - 0.0010) * (weight - 145 ))
elif 155 < weight <= 165:
    handicap = ((0.4878 - 0.0009) * (weight - 155))
    

# calculates the lifter's handcap score 
score = ( squat + benchpress + deadlift ) * handicap 

#generates lifter's handicap score  as an output 
print ('The lifter handicap score  is' , score , 'kilogram')

                                                                                                                         
                                                                                                                         
                