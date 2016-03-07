from itertools import permutations

main_digit_set = range(1, 10)
product_set = set()


def int_list_to_int(nums):
    return int(''.join(str(i) for i in nums))


def int_to_int_list(num):
    return [int(c) for c in list(str(num))]


def get_pandigitals(m1, m2):

    global running_tally

    for part1 in permutations(main_digit_set, m1):
        working_set1 = main_digit_set[:]
        for r in list(part1):
            working_set1.remove(r)

        for part2 in permutations(working_set1, m2):
            working_set2 = working_set1[:]
            for y in list(part2):
                working_set2.remove(y)
            p1_int = int_list_to_int(part1)
            p2_int = int_list_to_int(part2)
            prod = p1_int * p2_int
            if sorted(int_to_int_list(prod)) == sorted(working_set2):
                print "Found one!: %d * %d = %d" % (p1_int, p2_int, prod)
                product_set.add(prod)


get_pandigitals(1, 4)
get_pandigitals(2, 3)

print sum(i for i in product_set)
