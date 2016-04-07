require 'set'

class Fixnum
    def is_prime?(prime_set = nil)
        if prime_set
            prime_set.include?(self)
        else
            Math.sqrt(self).floor.downto(2).each {|i| return false if self % i == 0}
            true
        end
    end
end


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



def get_replacement_nums(original_num, digit_to_replace)
    original_num = original_num.to_s
    digit_to_replace = digit_to_replace.to_s
    rep_array = []
    10.times do |r|
        rep_array << original_num.gsub(digit_to_replace, r.to_s).to_i
    end
    return rep_array
end


prime_set = get_primes_up_to_max(1000000)

prime_set.each do |prime|
    prime_string = prime.to_s
    digit_char_list = Set.new(prime_string.split(""))
    digit_char_list.select! {|c| ['0', '1', '2'].include?(c) }
    
    eight_family = false
    digit_char_list.each do |digit|
        rep_candidates = get_replacement_nums(prime_string, digit)
        if rep_candidates.count {|r| r.is_prime?(prime_set) && 
                                 r.to_s.length == prime.to_s.length} >= 8
            p prime_string, rep_candidates.select {|r| r.is_prime?(prime_set)}
            exit
        end
    end
end

