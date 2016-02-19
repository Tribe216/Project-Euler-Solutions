from time import clock

start_time = clock()

print reduce( lambda x,y: x+y, [ int(i) for i in list(str(2**1000)) ] )

print clock() - start_time, "seconds"