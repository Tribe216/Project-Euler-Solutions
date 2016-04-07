
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

amicable_pairs = []
for i in range(10001):
    if i == sum_of_factors(sum_of_factors(i)) and i != sum_of_factors(i) and i not in amicable_pairs:
        amicable_pairs.append(i)

print sum(amicable_pairs)
