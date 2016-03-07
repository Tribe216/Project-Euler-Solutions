from math import factorial

result_list = []


def int_list_to_int(nums):
    return int(''.join(str(i) for i in nums))


def int_to_int_list(num):
    return [int(c) for c in list(str(num))]


def is_int_factorial_sum(num):
    global result_list
    digit_list = sorted(int_to_int_list(num))
    fact_sum = sum([factorial(i) for i in digit_list])
    if fact_sum == num:
        result_list.append(num)
        print num


def test_ints(max_num=1000000000):

    global result_list

    for num in xrange(10, max_num):
        is_int_factorial_sum(num)


test_ints()

print sum(result_list)
