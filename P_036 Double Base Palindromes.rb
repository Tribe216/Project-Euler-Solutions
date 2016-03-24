def get_palin_set(num_digits)

    if num_digits == 1
        return (1..9).to_a
    end

    middle_digits = num_digits%2==1 ? ('0'..'9').to_a : ['']
    pal_digits = num_digits / 2
    start_num = (10**(pal_digits-1)).to_s
    max_num = (10**(pal_digits) - 1).to_s

    puts start_num + " " + max_num

    ret_arr = []
    middle_digits.each do |mid|
        start_num.upto(max_num) do |pal_n|
            ret_arr << (pal_n + mid + pal_n.reverse).to_i
        end
    end

    return ret_arr
end

def check_binary_pal(num)
    b_num = num.to_s(2)
    return b_num == b_num.reverse
end



verified_palins = []
1.upto(6) do |digits|
    get_palin_set(digits).each do |d_pal|
        verified_palins << d_pal if check_binary_pal(d_pal)
    end
end

puts verified_palins.count
puts verified_palins.inject(0, :+)

