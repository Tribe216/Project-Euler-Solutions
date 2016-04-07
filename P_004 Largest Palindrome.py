import sys
from time import clock
from time import sleep

start_time = clock()

def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
    
largest_pal = False

for i in range(100,1000):
    for j in range(100,1000):
        if i<=j and str(i*j) == reverse(str(i*j)) and i*j > largest_pal:
            largest_pal = i*j
            
 
print clock() - start_time, "seconds"

print largest_pal



    
