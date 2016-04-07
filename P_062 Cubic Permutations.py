#!/usr/bin/env python3

sorted_cubevals = {}
for a in range(10000000):
    cube = int(a**3)
    sorted_cube_string = ''.join(sorted(list(str(cube))))

    if sorted_cube_string not in sorted_cubevals:
        sorted_cubevals[sorted_cube_string] = {"count": 1, "min": cube}
    else:
        sorted_cubevals[sorted_cube_string]["count"] += 1

    if sorted_cubevals[sorted_cube_string]["count"] == 5:
        print(sorted_cubevals[sorted_cube_string]["min"])
        break
