
def get_next_substring(in_str, divisor)
    str_list = in_str.split("")
    return_set = []
    0.upto 9 do |d|
        d = d.to_s
        unless str_list.include?(d)
            next_3 = (d + in_str[0..1]).to_i
            if next_3 % divisor == 0
                return_set << (d + in_str)
            end
        end
    end
    return_set
end

results = []
set_17 = []

1.upto(1000/17) do |m|
    mult_str = (m*17).to_s.rjust(3, '0')
    if ("0".."9").all?{|c| mult_str.count(c) <= 1}
        set_17 << mult_str
    end
end

set_17.each do |i_17|
    set_13 = get_next_substring(i_17,13)
    set_13.each do |i_13|
        set_11 = get_next_substring(i_13,11)
        set_11.each do |i_11|
            set_7 = get_next_substring(i_11,7)
            set_7.each do |i_7|
                set_5 = get_next_substring(i_7,5)
                set_5.each do |i_5|
                    set_3 = get_next_substring(i_5,3)
                    set_3.each do |i_3|
                        set_2 = get_next_substring(i_3,2)
                        set_2.each do |i_2|
                            set_1 = get_next_substring(i_2,1)
                            results << set_1[0]
                        end
                    end
                end
            end
        end
    end
end

puts results
sum = 0
results.each {|r| sum += r.to_i}
puts sum