
import itertools
import operator
import math

def sum_of_factors(number):

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
    uniq_mults.sort()

    uniq_mults.pop()
    return sum(uniq_mults)

non_abundant_bits = []
for i in range(28124):
    non_abundant_bits.append(1)

print len(non_abundant_bits)
abundant_set = []

for i in range (28123):
    if i < sum_of_factors(i):
        abundant_set.append(i)
        for j in abundant_set:
            if (i+j < 28124):
                non_abundant_bits[i+j] = 0

non_abundant_sum = 0
for i in range (28124):
    if non_abundant_bits[i]:
        non_abundant_sum += i

print non_abundant_sum