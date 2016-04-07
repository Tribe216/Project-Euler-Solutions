import sys
from time import clock
from time import sleep
from math import sqrt

start_time = clock()

high_val = long(sys.argv[1])

sum_of_squares = (high_val*(high_val+1)*(2*high_val+1))/6

square_of_sum = ((high_val**2 + high_val)/2)**2

print clock() - start_time, "seconds"

print str(square_of_sum-sum_of_squares)

    
