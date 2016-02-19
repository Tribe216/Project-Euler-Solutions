from time import clock

start_time = clock()
total_sum,total_sum_5,total_sum_3 = 0,0,0


for i in range(5,1000,5):
    total_sum_5 += i

for i in range(3,1000,3):
    if (i % 5):
        total_sum_3 += i

print clock() - start_time, "seconds"
print "total:", total_sum_5 + total_sum_3

start_time = clock()
for i in range(1,1000,1):
    if ( not (i % 3) or not (i % 5)):
        total_sum += i
print clock() - start_time, "seconds"
print "total:", total_sum       
    
