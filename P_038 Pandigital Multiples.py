all_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
largest_yet = 0
for c in range(9000, 9999):
    num_str = str(c) + str(c*2)
    if sorted(list(num_str)) == all_digits:
        if int(num_str) > largest_yet:
            largest_yet = int(num_str)

print(largest_yet)
