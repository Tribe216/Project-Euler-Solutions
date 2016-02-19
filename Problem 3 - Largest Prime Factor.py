import sys
from time import clock
from time import sleep
from math import sqrt

start_time = clock()

initial_num = long(sys.argv[1])
factor_set = []
divisor = 2

while(True):
    
    if divisor > sqrt(initial_num):
        break;
    elif initial_num % divisor == 0:
        initial_num = initial_num / divisor
        factor_set.append(divisor)        
    else:
        divisor += 1

factor_set.append(initial_num)    
print clock() - start_time, "seconds"

print factor_set

    
