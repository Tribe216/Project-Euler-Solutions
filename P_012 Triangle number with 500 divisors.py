
import itertools
import operator
from time import clock
import math

def num_of_factors(number):

    divisor_set = []

    i=2
    while(number > 1):
        while (number % i == 0):
            divisor_set.append(i)
            number = number / i

        i=i+1

    combs = []
    for i in xrange(1, len(divisor_set)+1):
        els = [list(x) for x in itertools.combinations(divisor_set, i)]
        combs.extend(els)

    mult_combos = []
    for j in combs:
        mult_combos.append(reduce(operator.mul, j))
    mult_combos.append(1)

    uniq_mults = dict(map(None,mult_combos,[])).keys()
    # uniq_mults.sort()
    return len(uniq_mults)

start_time = clock()
incrementor=1
number = 0
while(1):
    number = number + incrementor
    incrementor +=1
    if (num_of_factors(number) > 500):
        print number, num_of_factors(number),clock() - start_time, "seconds"
        break