
import itertools
import operator
import math

pattern = []
current_divisor = 5
for i in range (10,0,-1):
    pattern.append(str(current_divisor/(10**i)))
    current_divisor = current_divisor % (10**i)


print "".join(pattern)
