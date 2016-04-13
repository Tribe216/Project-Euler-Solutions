from pyprimes import isprime


def get_factors(initial_num):
    divisor = 2
    factor_set = set()
    while(True):

        if divisor > initial_num ** 0.5:
            break
        elif initial_num % divisor == 0:
            initial_num = initial_num / divisor
            factor_set.add(divisor)
        else:
            divisor += 1

    factor_set.add(initial_num)
    return len(factor_set)

start_num = 1

for i in range(300000):
    pf = [get_factors(x) for x in range(i, i+4)]
    if pf == [4, 4, 4, 4]:
        print i, pf

"""
while True:
    if num_prime_factors(start_num) >= 4:
        if num_prime_factors(start_num+1) >= 4:
            print start_num
            if num_prime_factors(start_num+2) >= 4:
                exit()
    start_num += 1"""
