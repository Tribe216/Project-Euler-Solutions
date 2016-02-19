from time import sleep

fifth_sum_dict = {}
total_sum = 0
current_number = 10


def process_number(num_in):
    trunc_str_list = list(str(num_in).replace('0', ''))
    f_key_list = sorted(trunc_str_list)
    f_key_str = ''.join(f_key_list)

    if f_key_str not in fifth_sum_dict:
        fifth_sum_dict[f_key_str] = sum([int(s)**5 for s in f_key_list])

    return fifth_sum_dict[f_key_str]


while(1):
    f_sum = process_number(current_number)

    if current_number == f_sum:
        total_sum += current_number
        print 'Ctr: ' + str(current_number)\
            + ' f_sum: ' + str(f_sum)\
            + ' total: ' + str(total_sum)
        sleep(1)

    current_number += 1
