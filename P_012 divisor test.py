#-------------------------------------------------------------------------------
# Name:        Project Euler Problem 11
# Purpose:
#
# Author:      bhm7
#
# Created:     18/12/2013
# Copyright:   (c) bhm7 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import itertools
import operator

counter = 0
number = 0
num_divisors = 0
max_divisors = 0
divisor_set = []

number = 15
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
uniq_mults.sort()
print len(uniq_mults)
