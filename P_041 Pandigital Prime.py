from itertools import permutations
from pyprimes import isprime

for num_digits in range(9, 1, -1):
    sub_digit_set = [str(i) for i in range(1, num_digits+1)]
    for x in reversed([int("".join(i)) for i in permutations(sub_digit_set, num_digits)]):
        if isprime(x):
            print x
            exit()
