#!/usr/bin/env python3

count = 0
for pow_i in range(1, 100):
    for factor in range(9, 0, -1):
        if len(str(factor**pow_i)) == pow_i:
            print(str(factor**pow_i) + " " + str(factor) + " " + str(pow_i))
            count += 1

print(count)