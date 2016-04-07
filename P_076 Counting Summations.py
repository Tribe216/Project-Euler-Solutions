#!/usr/bin/env python3

master_array_list = {}
master_counter = 0


def get_higher_level(num_arr_list):
    next_level_array_list = []
    global master_counter
    print(len(num_arr_list))

    for num_arr_str in num_arr_list:
        num_arr = [int(c) for c in list(num_arr_str)]
        for l in range(len(num_arr)-1):

            proposed_new_array = num_arr[:]
            sum_val = num_arr[l] + num_arr[l+1]
            proposed_new_array[l] = sum_val
            del(proposed_new_array[l+1])
            proposed_new_array.sort()
            prop_str = "".join([str(c) for c in proposed_new_array])

            if prop_str not in next_level_array_list:
                next_level_array_list.append(prop_str)
                master_counter += 1

    return next_level_array_list

initial_num = 100
starting_arr = [[1 for _ in range(initial_num)]]
master_array_list = starting_arr[:]
for _ in range(initial_num-2):
    starting_arr = get_higher_level(starting_arr)

print(master_counter)
