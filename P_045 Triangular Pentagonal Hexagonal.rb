tri_nums = Array.new
pent_nums = Array.new
hex_nums = Array.new

100000.times do |num|
    tri_result = num * (num+1)/2
    tri_nums << tri_result
    pent_result = num * (3*num - 1)/2
    pent_nums << pent_result
    hex_result = num * (2*num -1)
    hex_nums << hex_result

    if pent_nums.include?(tri_result) && hex_nums.include?(tri_result)
        puts tri_result
    end

end 