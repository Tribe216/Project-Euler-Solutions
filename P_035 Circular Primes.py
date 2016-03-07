def get_primes_up_to_max(max_num):
    primes_set = set()
    not_primes = set()
    curr_mult = 2

    for curr_mult in range(2, max_num):
        if curr_mult in not_primes:
            continue

        i = 1
        primes_set.add(curr_mult)
        while(i*curr_mult < max_num):
            not_primes.add(i*curr_mult)
            i += 1

    return primes_set


def is_number_prime(num):
    global prime_list

    if(num in prime_list):
        return True

    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            return False

    prime_list.append(num)
    return True


def get_rotations_of_int(num):
    ret_list = []

    num_s = str(num)
    for i in range(len(num_s)):
        sub_str_int = (num_s * 2)[i:i-len(num_s)]
        ret_list.append(int(sub_str_int))

    return ret_list


def has_even_digits(num):
    for a in [int(d) for d in str(num)]:
        if a % 2 == 0:
            return True
    return False


def main_function():
    primes = get_primes_up_to_max(1000000)
    counter = 1
    for num in xrange(3, 1000000, 2):
        is_circ = True
        if has_even_digits(num) is True:
            continue

        for rot in get_rotations_of_int(num):
            if rot not in primes:
                is_circ = False
                break
        if is_circ:
            print num
            counter += 1

    print str(counter)

if __name__ == '__main__':
    main_function()
