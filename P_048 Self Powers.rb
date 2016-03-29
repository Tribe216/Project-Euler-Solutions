the_sum = 0
1.upto 1000 do |i|
    powered = i**i
    the_sum += powered
end

puts the_sum.to_s[-10..-1]