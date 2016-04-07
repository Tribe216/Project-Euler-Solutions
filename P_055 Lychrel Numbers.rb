def reverse_and_add(num_s)
    r_num = num_s.reverse.to_i
    return ( r_num + num_s.to_i).to_s
end

l_counter = 0
1.upto(10000) do |start_num|
    l_indicator = true

    1.upto(50) do |_|
        num_str = start_num.to_s
        start_num = reverse_and_add(num_str)
        if start_num == start_num.reverse
            l_indicator = false
            break
        end
    end

    l_counter += 1 if l_indicator
end

puts l_counter