require 'set'

EXISTING_SET = [3, 7, 109, 673]

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

def is_prime?(num)
   Math.sqrt(num).floor.downto(2).each {|i| return false if num % i == 0}
   true
end

def prime_pair?(num1, num2)
    if is_prime?(( num1.to_s + num2.to_s).to_i) &&
       is_prime?(( num2.to_s + num1.to_s).to_i)
        return true
    else
        return false
    end
end

seek_set = get_primes_up_to_max(1000000)
seek_set.each do |p|
    next if p <= 673
    pr_set_ind = true
    EXISTING_SET.each do |e|
        if !prime_pair?(p,e)
            pr_set_ind = false
            break
        end
    end

    if pr_set_ind
        puts p
        break
    end
end