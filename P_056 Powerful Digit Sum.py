#!/usr/bin/env python3

top_sum = 0
for a in range(101):
    for b in range(101):
        pow_sum = 0
        for c in list(str(int(a**b))):
            pow_sum += int(c)
        if pow_sum > top_sum:
            top_sum = pow_sum
        print(a,b,pow_sum)

print(top_sum)
