import sys
from time import clock
from time import sleep
from math import sqrt

start_time = clock()

high_val = long(sys.argv[1])

product = 1

for i in range(2,high_val+1):
    initial_num = i
    factor_set = []
    divisor = 2

    while(True):
        
        if divisor > initial_num:
            break;
        elif initial_num % divisor == 0:
            initial_num = initial_num / divisor
            factor_set.append(divisor)        
        else:
            divisor += 1     
    for j in factor_set:
        if product % j == 0:
            product = product / j
    product = product * i

print clock() - start_time, "seconds"

print product

    
