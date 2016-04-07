#!/usr/bin/env python3


def check_if_integral(side_l, base_l):
    height = ((side_l**2) - (0.5*base_l)**2)**0.5
    if height.is_integer():
        height = int(height)
        if (base_l % 2 == 1) and (height % 2 == 1):
            return False
        else:
            print("Found: {} {} {}".format(side_l, side_l, base_l))
            return True

perimeter_sum = 0

for side_l in range(2, 333333334):
    if check_if_integral(side_l, side_l-1):
        perimeter_sum += (3*side_l - 1)
    if check_if_integral(side_l, side_l+1):
        perimeter_sum += (3*side_l + 1)

print(perimeter_sum)
