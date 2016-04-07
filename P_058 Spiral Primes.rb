def is_prime?(num)
   Math.sqrt(num).floor.downto(2).each {|i| return false if num % i == 0}
   true
end

p_count = 0
total_count = 1
latest = 1

1.upto(1000000) do |ring|

    side_len_offset = ring * 2
    1.upto(4) do |iter|
        latest += side_len_offset
        p_count += 1 if is_prime?(latest)
        total_count += 1
    end

    percent_prime = 100.0 * p_count / total_count
    puts "#{(side_len_offset+1)} #{percent_prime}"
    if percent_prime < 10
        break
    end

end


