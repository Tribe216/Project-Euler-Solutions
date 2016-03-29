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

    return primes_set.sort.to_a
end


MAX_PRIME = 1000000

primes = get_primes_up_to_max(MAX_PRIME)

max_length = 0
max_sum = 0


primes.each.with_index do |p, i|
    
    break if primes[i+1] == nil || (p * max_length >= 1000000)
    local_sum = 0
    local_length = 0
    j = i
    puts p
    while local_sum < MAX_PRIME
        local_sum += primes[j]
        local_length += 1
        if primes.include?(local_sum) && local_sum > max_sum && local_length > max_length
            max_length = local_length
            max_sum = local_sum
            puts "#{max_length} #{max_sum}"
        end
        j += 1
    end
end

puts max_sum