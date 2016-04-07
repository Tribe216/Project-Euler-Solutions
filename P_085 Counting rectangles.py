#!/usr/bin/env python3


def dots_under_xy(t_l, t_h, x, y):
    return ((t_l - x) * (t_h - y))


def num_rectanges(t_l, t_h):
    rect_sum = 0
    for x in range(t_l):
        for y in range(t_h):
            rect_sum += dots_under_xy(t_l, t_h, x, y)
    return rect_sum


best_grid = [0, 0, 0]

for a in range(5, 100):
    for b in range(5, 100):
        nr = num_rectanges(a, b)
        if abs(nr - 2000000) < abs(best_grid[2] - 2000000):
            best_grid = [a, b, nr]
            print(best_grid)

print(best_grid)
