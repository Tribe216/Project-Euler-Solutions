from time import clock

start_time = clock()
for i in range(1,499):
    for j in range(i,998):
        if (i**2 + j**2) == (1000-i-j)**2:
                print i,j,1000-i-j
                print i**2, "+", j**2,"=", (1000-i-j)**2
                print "i * j * k", i*j*(1000-i-j)
                break

print clock() - start_time, "seconds"