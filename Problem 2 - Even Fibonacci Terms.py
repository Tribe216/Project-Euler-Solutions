import sys
from time import clock

start_time = clock()

running_sum = 0
i_front = 1
i_back = 1

while ( i_front <= 4000000 ):
    if not (i_front % 2):
        running_sum += i_front

    i_front = i_front + i_back 
    i_back = i_front - i_back
    
    
print clock() - start_time, "seconds"
print running_sum , "\n\n"




start_time = clock()

running_sum = 0
i_front = 2
i_rear = 1

while ( i_front <= 4000000 ):
    running_sum += i_front
    i_rear = 2*i_front + i_rear
    i_front = 2*i_rear - i_front 
    
    
print clock() - start_time, "seconds"
print running_sum
    
