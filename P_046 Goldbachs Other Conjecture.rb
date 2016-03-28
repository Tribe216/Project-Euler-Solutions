require 'set'

def get_primes_up_to_max(max_num)
    primes_set = Set.new
    not_primes = Set.new
    curr_mult = 2

    2.upto max_num-1 do |curr_mult|
        if not_primes.include? curr_mult
            next
        end

        primes_set.add(curr_mult)
        i = 1
        while(i*curr_mult < max_num)
            not_primes.add(i*curr_mult)
            i += 1
        end
    end

    return primes_set
end

primes = get_primes_up_to_max(100000)

goldbach_nums = Set.new
MAX_SQ = 1000

primes.each do |prime|
    1.upto MAX_SQ do |sq_val|
        goldbach_nums << (prime + 2*(sq_val**2))
    end
end

MAX_SEARCH = MAX_SQ
1.upto goldbach_nums.max/2 do |i|
    candidate = i*2 + 1
    next if primes.include?(candidate)
    next if goldbach_nums.include?(candidate)
    puts candidate
    break
end
