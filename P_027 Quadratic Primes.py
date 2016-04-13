def is_number_prime(num):
    if num < 2:
        return False
    # check for factors
    for i in range(2, int(num**0.5)):
        if (num % i) == 0:
            return False
    return True


def consecutive_primes(a, b):
    n = 0
    while True:
        expr = int(n**2 + (a * n) + b)
        if is_number_prime(expr):
            n += 1
        else:
            break
    return n


max_primes_set = [0, 0, 0]
for a in range(-999, 1000):
    for b in range(-999, 1000):
        top_n = consecutive_primes(a, b)
        if top_n > max_primes_set[0]:
            max_primes_set = [top_n, a, b]

print(max_primes_set)
print(max_primes_set[1] * max_primes_set[2])
