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

TOTAL_PRIMES = get_primes_up_to_max(100000)
t_primes = Set.new

def is_truncable?(num)
    num_str = num.to_s
    0.upto(max_num.length-2) do [offset]
        unless TOTAL_PRIMES.include? num_str[0..offset]
            && TOTAL_PRIMES.include? num_str[(offset+1)..(max_num.length-1)]
            return false
        end
    end

    return true
end


end

running_count = 0
running_sum = 0

TOTAL_PRIMES.each do |p|
    next if p < 10
    if is_truncable?(p)
        running_count +=1
        running_sum += p
    end
    if running_count == 11
        puts running_sum
        break
    end
end