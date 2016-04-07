counter = 0
coins = {
    0: 1,
    1: 2,
    2: 5,
    3: 10,
    4: 20,
    5: 50,
    6: 100,
    7: 200
}


def get_factors_plus_zero(num, divisor):
    return range((num / divisor) + 1)


def coin_ways(rem, coin_index):
    global counter

    coin_val = coins[coin_index]
    coin_combos = get_factors_plus_zero(rem, coin_val)

    for i in coin_combos:
        loop_remainder = rem - (coin_val*i)
        # if remainder is zero, counter++
        if loop_remainder == 0 or coin_index-1 == 0:
            counter += 1
            continue
        coin_ways(loop_remainder, coin_index-1)


coin_ways(2000, 7)
print counter
